import time

def timer(func,*values):
    start = time.time()
    print(x)
    end = time.time()
    return end-start

if __name__ == '__main__':
   print(timer(zip, [1, 2, 3], [4, 5, 6]))