import threading
from time import sleep
from random import randint

l = threading.Lock()


def pinger():
    l.acquire()
    t_name = threading.currentThread().getName()
    for _ in xrange(randint(3, 5)):
        print ("Hello from {}".format(t_name))
        sleep(1)
    l.release()


tp = [threading.Thread(target=pinger, name=_) for _ in xrange(1, 6)]
for thread in tp:
    thread.start()
