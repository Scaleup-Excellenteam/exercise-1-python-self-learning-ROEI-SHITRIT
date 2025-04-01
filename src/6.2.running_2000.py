import time

def timer(func, *args, **kargs):
    start = time.time()
    result = func(*args, **kargs)
    end = time.time()

    return end - start

if __name__ == '__main__':
   print(timer(zip, [1, 2, 3], [4, 5, 6]))
