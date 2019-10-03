#!/usr/bin/python

import os
import subprocess
import threading

def m3():
    res = subprocess.Popen('ps -ef | grep tempuplode', stdout=subprocess.PIPE, shell=True)
    attn=res.stdout.readlines()
    count=len(attn)
    if count<3:
        os.system('sudo python /home/pi/tempuplode.py')

while True:
    m3()
