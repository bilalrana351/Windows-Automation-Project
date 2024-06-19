import os
import fnmatch
import string

def find_file(filename, exceptions):
    """
    Searches for a file in the entire file system and returns the full path if found.

    Args:
    filename (str): The name of the file to search for.

    Returns:
    str: The full path of the file if found, otherwise an empty string.
    """

    # Get all drives existing on the system
    drives = [f"{letter}:\\" for letter in string.ascii_uppercase if os.path.exists(f"{letter}:\\")]

    # Search for the file in all drives
    for drive in drives:
        # Start search from the Users folder on C: drive
        if drive == "C:\\":
            start_folder = os.path.join(drive, "Users")
        else:
            start_folder = drive

        for root, dirs, files in os.walk(start_folder):
            for name in files:
                full_path = os.path.join(root, name)
                if fnmatch.fnmatch(name, filename) and not any(ex in full_path for ex in exceptions):
                    return full_path
    return ""

# Example usage
"""
file_to_search = "audio.py"
exceptions = ["C:\\Program Files\\CodeBlocks\\MinGW\\opt\\lib\\python2.7\\email\\mime\\audio.py"]
file_path = find_file(file_to_search, exceptions)
if file_path:
    print(f"File found: {file_path}")
else:
    print("File not found")
"""