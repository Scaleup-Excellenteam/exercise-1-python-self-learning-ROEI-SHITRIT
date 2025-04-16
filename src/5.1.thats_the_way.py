"""
This module scans a given directory and returns a list of file names that start with 'deep'.
"""

import os


def thats_the_way(path):
    """
    Returns a list of all file names in the given directory that start with 'deep'.

    Args:
        path (str): The directory path to scan.

    Returns:
        list: A list of file names in the directory, or an empty list if an error occurs.

    Raises:
        FileNotFoundError: If the specified path does not exist.
        PermissionError: If access to the directory is denied.

    Examples:
        #>>> thats_the_way("images")
        ['deep_blue.jpg', 'deep_space.png']

        #>>> thats_the_way("non_existing_folder")
        Error: The path 'non_existing_folder' does not exist.
        []
    """
    try:
        return [
            entry.name for entry in os.scandir(path)
            if entry.is_file() and entry.name.startswith("deep")
        ]
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied for path '{path}'.")
        return []


if __name__ == '__main__':
    thats_the_way("your_directory_path_here")
