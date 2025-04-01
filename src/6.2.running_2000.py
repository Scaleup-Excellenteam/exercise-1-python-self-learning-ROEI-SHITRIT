import time

def running_2000(func,*values):
    start = time.time()
    end = time.time()
    return end-start

if __name__ == '__main__':
   print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
