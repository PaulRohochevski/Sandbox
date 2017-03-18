"""
Check how long the function sleeps.
"""
import check_python_version
from time import time


# This func is a decorator
def print_sleep(func):
    def wrapper():
        start_time = time()
        func()
        end_time = time()
        sleep_time = end_time - start_time
        print(sleep_time)

    return wrapper


# Checking sleep time
@print_sleep
def sleep():
    from random import randint
    from time import sleep
    sleep(randint(1, 5))


sleep()
