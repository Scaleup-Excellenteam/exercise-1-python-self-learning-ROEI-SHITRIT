"""Joins multiple lists into one, inserting a separator between them if provided."""
def cup_of_join(*lists,sep=""):
    """
      Merges multiple lists into a single list, inserting a separator between them.

      Args:
          *lists (list): Multiple lists to be joined.
          sep (str, optional): A separator to be placed between the lists. Defaults to "-".

      Returns:
          list: A list that contains all elements from the input lists, with the separator placed between them.

      Raises:
          SystemExit: If a non-list argument is passed.

      Example:
          #>>> join([1, 2], [3, 4], [5, 6], sep=",")
          [1, 2, ',', 3, 4, ',', 5, 6]

          #>>> join([1, 2], [3, 4], [5, 6])
          [1, 2, '-', 3, 4, '-', 5, 6]
      """
    result = []
    i=0
    if len(lists)==0:
        return  None
    for lst in lists:
        if not isinstance(lst, list):
            return None
        result+=lst
        if i<len(lists) and sep != "":
            result.append(sep)
        i += 1
    return result

if __name__ == '__main__':
    cup_of_join([1, 2], [8], [9, 5, 6], sep='@')
