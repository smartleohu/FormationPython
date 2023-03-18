import datetime
import functools
import time
from typing import Callable


class EvaluationTime:
    def __init__(self, fct_name):
        self._fct_name = fct_name
        self._init_time = datetime.datetime.now()

    def __enter__(self):
        print(f"Started: {self._fct_name} at {self._init_time}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Finished: {self._fct_name} in "
              f"{datetime.datetime.now() - self._init_time}")


def timing(fct: Callable):
    @functools.wraps(fct)
    def fct_wrapper(*args, **kwargs):
        with EvaluationTime(fct.__qualname__):
            return fct(*args, **kwargs)

    return fct_wrapper


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
