import re
def long_cat_is_long(txt):
    """
       Counts the length of each unique word in the given text.

       Args:
           txt (str): The input text.

       Returns:
           dict: A dictionary where keys are words (only letters) and values are their lengths.

       Example:
           #>>> count_words("Hello world! This is a test.")
           {'hello': 5, 'world': 5, 'this': 4, 'is': 2, 'a': 1, 'test': 4}
       """
    
    words = txt.lower().split()
    only_words = {word[:-1] if not re.match("^[A-Za-z]+$", word) else word for word in words}
    return {word:len(word) for word in only_words}



text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

if __name__ == '__main__':
    print(count_words(text))
