import time
import logging
from shutil import move
from mimetypes import guess_type
from os import scandir, mkdir
from os.path import expanduser, splitext, exists, join
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

'''
os.path.expanduser is used to expand the tilde(~) symbol in a file
to the full path of the user's home directory. Or else the tilde(~)
will be treated as part of the string.
'''
src_dir = expanduser("~/Desktop/Downloads")

class FileHandler(FileSystemEventHandler):   

    """
    Iterate through the files in the source directory.
    """
    def on_modified(self, event):
        with scandir(src_dir) as files: #os.scandir() is a directory iterator
            for file in files:
                filename = file.name
                if file.is_file() and not filename.startswith('.'): #Check is the file is not a directory and not a hidden file.
                    print(filename + "\n")
                    self.check_file_type(filename, entry=file)
    """
    Checks each file for its file type.
    Creates a folder inside the source directory for each specific file type.
    Calls the move_file function
    """
    def check_file_type(self, filename, entry):
        file_type = guess_type(filename)[0]

        #checks the file type and creates a folder base on that file type
        if file_type is not None:
            if file_type.startswith("image/"):
                dest_path = src_dir + "/Images"
            elif file_type.startswith("video/"):
                dest_path = src_dir + "/Videos"
            elif file_type.startswith("audio/"):
                dest_path = src_dir + "/Audios"
            elif file_type.startswith("application/") or file_type.startswith("text/"):
                dest_path = src_dir + "/Documents"
            else:
                dest_path = src_dir + "/Misc"
        else:
            dest_path = src_dir + "/Misc"

        self.move_file(dest_path, filename, entry)

        #logs the event happening
        logging.info(f"Moved file: {filename}")
    
    def move_file(self, dest_path, filename, entry):

        #creates the directory if not exists (base on file type)
        if not exists(dest_path):
            mkdir(dest_path)

        #checks for file duplicates
        if exists(f"{dest_path}/{filename}"):
            filename = self.make_unique_name(dest_path, filename)

        #move the new file to the destination
        move(entry, join(dest_path, filename))
        
        
    """
    Rename the incoming file with a unique name
    """
    def make_unique_name(self, dest, filename):
        name, extension = splitext(filename)
        counter = 1
        while exists(join(dest,filename)):
            filename = f"{name}({str(counter)}){extension}"
            counter += 1
        return filename
    
if __name__ == "__main__":
   
    #actively listen for file system events and react to them
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = src_dir
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
