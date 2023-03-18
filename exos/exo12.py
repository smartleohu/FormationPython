import functools
import time
from typing import Callable


def timing(func: Callable):
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


@timing
def pause(t: float):
    """
    Pause function
    :param t: second
    :return:
    """
    print("Begin ...")
    time.sleep(t)  # Pause de t secondes
    print("End!")


if __name__ == '__main__':
    pause(t=2)
    print(pause.__doc__)
