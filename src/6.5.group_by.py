from collections import defaultdict


def group_by(func,iterable):
    """
       Groups elements of the iterable by the result of applying the given function to each element.

       The function applies `func` to each item in the `iterable`, and uses the result as the key in the returned dictionary.
       The value associated with each key is a list of all elements from the iterable that produced that key.

       Args:
           func (function): A function to apply to each element of the iterable.
           iterable (iterable): The iterable to be processed.

       Returns:
           dict: A dictionary where keys are the results of applying `func` to each element,
                 and values are lists of elements that produced those results.

       Example:
           #>>> group_by(len, ["hi", "bye", "yo", "try"])
           {2: ['hi', 'yo'], 3: ['bye', 'try']}
       """
    my_dict = defaultdict(list)
    for item in iterable:
        my_dict[func(item)].append(item)
    return my_dict
print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == '__main__':
    group_by(len, ["hi", "bye", "yo", "try"])