"""Measures the execution time of a given function."""
import time

def running_2000(func, *args, **kargs):
    """
    Measures the execution time of a function by running it with the given arguments.

    Args:
        func (callable): The function to be executed.
        *args: Positional arguments to pass to the function.
        **kargs: Keyword arguments to pass to the function.

    Returns:
        float: The time taken to execute the function in seconds.

    Example:
        #>>> running_2000(zip, [1, 2, 3], [4, 5, 6])
        1.1920928955078125e-05
    """
    start = time.time()
    func(*args, **kargs)
    end = time.time()

    return (end - start) * 1000  # Convert to milliseconds

if __name__ == '__main__':
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
