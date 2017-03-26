#!C:\Python27\python.exe
import time, sys


def my_funk():
    while True:
        try:
            time.sleep(100)
        except KeyboardInterrupt:
            print("You have 3 attempts left")
            try:
                time.sleep(100)
            except KeyboardInterrupt:
                print("You have 2 attempts left")
                try:
                    time.sleep(100)
                except KeyboardInterrupt:
                    print("You have 1 attempts left")
                    exit_condition = input("Are you sure you want to exit (y/n)")
                    if exit_condition == "y":
                        sys.exit(1)
                    else:
                        pass
        finally:
            pass


my_funk()
