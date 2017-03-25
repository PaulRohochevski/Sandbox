import threading
from time import sleep, localtime

global_list = []


def calculator():
    print("Thread 2 started")
    sleep(3)
    global_list.append("Result")


thr1 = threading.Thread(target=calculator)
thr1.setDaemon(True)
thr1.start()
sleep(3)
print ("Global list content is: {}".format(global_list))
