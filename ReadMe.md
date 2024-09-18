# File Management Automation Project

## Overview

This Python program automates file organization by actively monitoring a specified source directory (e.g., Downloads).
It detects new files and automatically categorizes them based on their file type (Image, Video, Audio, Document).
The program creates the necessary directories for each file type and moves the incoming files to their respective directories.
If a duplicate file already exists, it renames the new file to ensure uniqueness.

## Key Features
  - **Real-time Monitoring:** The program listens for file system events in a specified directory and reacts instantly to new files.
  - **Automatic File Organization:** Incoming files are categorized and moved into directories based on their type (Image, Video, Audio, Document).
  - **Duplicate Handling:** If a file with the same name exists, the program renames the incoming file (e.g, **`file.txt`** becomes **`file(1).txt`**.

## Methods:
  - `on_modified`:
      - Monitors the source directory for file changes and iterates through the incoming files.
  - `check_file_type`:
      - Determines the file type (Image, Video, Audio, Document) and generates a specific file path based on the type.
  - `move_file`:
      - Creates the required directory if it doesn't exist, checks for duplicate files, and moves the incoming file to the appropriate directory.
  - `make_unique_name`:
      - Renames a file if a duplicate exists by appending a unique identifier (e.g., file.txt → file(1).txt).

## Libraries:
  - `time`: Used for time and sleeping operations.
  - `logging`: Tracks file operations and logs important events.
  - `shutil`: Handles file operations, including moving files.
  - `mimetypes`: Determines the file type based on the file's MIME type.
  - `os`: Provides functions for interacting with the file system.
  - `watchdog`: Monitors the file system for changes in real-time.

## How to Run
  - `python3 fileManagement.py`
