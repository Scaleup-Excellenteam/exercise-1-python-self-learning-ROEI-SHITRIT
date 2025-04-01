"""Interleaves multiple iterables, either as a generator or returning a list."""
from itertools import zip_longest


def generator_interleave(*iterable):
    """
       Mixes multiple iterables by taking one element from each in order.

       Args:
           *iterable: One or more iterables whose elements will be interleaved.

       Yields:
           Elements from the input iterables in an interleaved order.

       Example:
          # >>> list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
           ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    """
    i = 0
    lst_to_send = list(iterable)
    try:
        while len(lst) > 0:
            for item in lst:
                if i < len(item):
                    yield item[i]
                else:
                    lst_to_send.remove(item)
            i += 1
    except ValueError:
        return None


def interleave(*iterable):
    return [item for it in zip_longest(*iterable) for item in it if item is not None]


if __name__ == '__main__':
    print(list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#', '*'))))
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
