from PIL import Image
import numpy as np

def remember_remember(path):
    """
       Decodes a secret message embedded in a black-and-white image by locating black pixels in each column.

       The function opens an image from the given file path, iterates through each column, and checks for the
       row index of the black pixel (value 1). The row indices are then converted to characters (using the `chr` function)
       to reveal the hidden message.

       Args:
           path (str): The file path of the encoded image.

       Returns:
           str: The decoded message from the image.

       Example:
           #>>> remember_remember("encrypted_message.png")
           "Hello"
       """
    image=0
    result =""
    try:
        image = Image.open(path)
    except FileNotFoundError:
        exit(-1)
    image_array = np.array(image)
    for col in range(image_array.shape[1]):
        row_idx = np.where(image_array[:, col] == 1)[0]

        if len(row_idx) > 0:
            result += chr(row_idx[0])  

    return result

if __name__ == '__main__':
  remember_remember("code.png")
