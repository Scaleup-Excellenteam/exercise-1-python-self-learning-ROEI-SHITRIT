def interleave(*iterable):
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
    i=0
    lst=list(iterable)
    try:
     while len(lst)>0:
        for item in iterable:
            if i < len(item):
                yield item[i]
            else:
                lst.remove(item)
        i+=1
    except ValueError:
        exit(-1)

if __name__ == '__main__':
  interleave('abc', [1, 2, 3], ('!', '@', '#'))