# FileHandlingProject
This is the repository  which showcases my integration of Python concepts while making a useful CRUD operation based File Handling Project

File Handling CRUD Project (Python)

A beginner-friendly Python project that demonstrates CRUD (Create, Read, Update, Delete) operations using Python's built-in file handling capabilities and the pathlib module. This project provides a simple command-line interface for managing files inside a dedicated project directory while reinforcing core Python concepts such as functions, exception handling, file operations, and path management.

 Features:
 
 Create new files with custom content
 Read the contents of existing files
 Update files by:
Renaming the file
Overwriting existing content
Appending new content
 Delete files safely
 Automatically display all available files and folders before every operation
 Exception handling for invalid inputs and file-related errors
 Cross-platform path handling using Python's pathlib module
 Technologies Used
Python 3
pathlib
File Handling
Exception Handling
Command Line Interface (CLI)
 Project Structure
mega_project-file/
│
├── main.py
├── README.md
└── (Files created during execution)

 How It Works

The application provides a menu-driven interface where the user can choose one of the following operations:

Create a File
Read a File
Update a File
Rename File
Overwrite Content
Append Content
Delete a File

Before each operation, the program displays the available files and folders to make navigation easier.

 Learning Outcomes

This project helped reinforce important Python concepts including:

File Handling (open, read, write, append)
pathlib for modern file path management
Functions and modular programming
Exception handling with try-except
Conditional statements
User input handling
Building a menu-driven CLI application
 Sample Output
Press 1 for creating a file
Press 2 for reading a file
Press 3 for updating a file
Press 4 for deleting a file

Enter your choice: 1

Please tell your file name: notes.txt
Write something in this file:
Hello World

FILE CREATED SUCCESSFULLY
 Future Improvements
Search files by name
Copy and move files
Delete folders recursively
Support nested directories
Add colored terminal output
Logging system
File metadata (size, creation date, last modified)
GUI version using Tkinter or CustomTkinter
