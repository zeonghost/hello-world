#!/usr/bin/python

import os
from multiprocessing import Process

def m1():
    os.system('sudo python /home/pi/monit.py')

def m2():
    os.system('sudo python /home/pi/monit2.py')

def m3():
    os.system('sudo python /home/pi/monit3.py')

if __name__ == "__main__":
    proc1 = Process(target = m1)
    proc2 = Process(target = m2)
    proc3 = Process(target = m3)

    proc1.start()
    proc2.start()
    proc3.start()
    proc1.join()
    proc2.join()
    proc3.join()
