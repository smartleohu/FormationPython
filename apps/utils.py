import functools
import time


def timing(func):
    """
    Mesure execution time.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        wrapper function in timing
        :param args:
        :param kwargs:
        :return:
        """
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Elapsed time : {end_time - start_time :1.3f}s")

    return wrapper
