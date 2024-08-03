from threading import *
import threading
from time import sleep

lock = threading.Lock()


class Example(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print("lock acquired")
            print("hello from Example")
            sleep(1)
            lock.release()


class ExampleTwo(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print("lock acquired")
            print("hello from Example Two")
            sleep(1)
            lock.release()


example = Example()
exampleTwo = ExampleTwo()
example.start()
sleep(0.1)
exampleTwo.start()
# example.join()
# exampleTwo.join()
