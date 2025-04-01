"""Extracts hidden messages from a binary file based on a specific pattern."""
import os
import re
def read_file_in_chunks():
    """
      Reads a binary file in chunks of 1024 bytes.

      Args:
          path (str): The path to the binary file to be read.

      Yields:
          bytes: A chunk of the file content.

      Raises:
          FileNotFoundError: If the specified file is not found, exits with code -1.
      """
    try:
        path = os.path.abspath('./logo.jpg')
        with open(path, "rb") as file:
            chunk_size = 1024
            chunk = 1
            while chunk:
                chunk = file.read(chunk_size)
                yield chunk
    except FileNotFoundError:
        return None

def parsle_tongue():
    """
        Extracts and prints secret messages from a binary file.

        Args:
            path (str): The path to the binary file to be analyzed.

        The function reads the file in chunks and searches for secret messages.
        A secret message is defined as a sequence of at least 5 lowercase English letters followed by '!'.

        Example:
            If the file contains "hello!world!", the function will print:

            hello!
            world!
        """
    secret_pattern = re.compile(br'[a-z]{5,}!')
    result = []
    for chunk in read_file_in_chunks():
        secrets = secret_pattern.findall(chunk)
        for secret in secrets:
            result.append((secret.decode('utf-8'))[:-1])

    return result

if __name__ == '__main__':
    print(parsle_tongue())
