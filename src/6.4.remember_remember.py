from PIL import Image


def remember_remember(path):
    """
       Decodes a secret message embedded in a black-and-white image by locating black pixels in each column.

       The function opens an image from the given file path, iterates through each column, and checks for the
       row index of the black pixel (value 1).
       The row indices are then converted to characters (using the `chr` function)
       to reveal the hidden message.

       Args:
           path (str): The file path of the encoded image.

       Returns:
           str: The decoded message from the image.

       Example:
           #>>> remember_remember("encrypted_message.png")
           "Hello"
       """

    result = ""

    try:
        # Open the image and convert it to black and white (L mode)
        image = Image.open(path).convert('1')  # '1' mode is for 1-bit pixels (black and white)
    except FileNotFoundError:
        print("file not found")

    # Get the width and height of the image
    width, height = image.size

    # Iterate through each column
    for col in range(width):
        for row in range(height):
            pixel = image.getpixel((col, row))
            if pixel == 0:
                result += chr(row)  

    return result

  if __name__ == '__main__':
  print(remember_remember("code.png"))
