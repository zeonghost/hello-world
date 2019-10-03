#!/usr/bin/python

import os
import subprocess
import threading

def m1():
    res = subprocess.Popen('ps -ef | grep control', stdout=subprocess.PIPE, shell=True)
    attn=res.stdout.readlines()
    count=len(attn)
    if count<3:
        os.system('sudo python /home/pi/control.py')
    
while True:
    m1()

