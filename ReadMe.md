File Management Project
  - The program actively listens to file system event in a source directory (Downloads etc.) and react to it.
  - The program checks the incoming file's file type if Image, Video, Audio, and Document. Creates a directory for each file type.
  - Move the incoming file to its respective director
  - Rename the incoming file if duplicate exists.
      - ex. file.txt to file(1).txt

  - Methods:
      - on_modified: Iterate through the files in the source directory
      - check_file_type: Checks the file's file type. Creates a file path specific to file type.
      - move_file: Creates a directory given a file path. Checks for dupe file. Move the file to its respective directory.
      - make_unique_name: If dupes exists, rename the incoming file with a unique file.
   
  - Libraries:
      - time
      - logging
      - shutil
      - mimetypes
      - os
      - watchdog
