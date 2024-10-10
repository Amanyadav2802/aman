from time import sleep
from threading import *

class helo(Thread):
    def run(self):
        for i in range(5):
            print('hello')
class hi(Thread):
    def run(self):
        for i in range(5):
            print('hii')
t1.helo()
t2.hii()
t1.start()
t2.start()