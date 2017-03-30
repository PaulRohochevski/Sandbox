import threading
from time import sleep

e = threading.Event()


def waiter():
    while True:
        print("Starting waiting for the event")
        while not e.is_set():
            pass
        print("Event occurred, clearing!!!")
        e.clear()
        sleep(2)


def setter():
    while True:
        sleep(3)
        print("Event is set, leaving")
        e.set()


t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)
t1.start()
t2.start()
