"""Write a python program to print the contents of a directory using the os module.
Search online for the function which does that."""
import os

def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        items = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Specify the path to the directory you want to print
directory_path = "/python"

# Call the function to print the directory contents
print_directory_contents(directory_path)
