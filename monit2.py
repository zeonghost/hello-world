#!/usr/bin/python

import os
import subprocess
import threading

def m2():
    res1 = subprocess.Popen('ps -ef | grep ch2', stdout=subprocess.PIPE, shell=True)
    attn1=res1.stdout.readlines()
    count1=len(attn1)
    if count1<3:
        os.system('sudo python /home/pi/ch2.py')

while True:
    m2()
