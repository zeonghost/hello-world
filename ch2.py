#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import schedule
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase import firebase

Relay_Ch2 = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch2,GPIO.OUT)

GPIO.output(Relay_Ch2,GPIO.HIGH)

newdb = firebase.FirebaseApplication('https://aquaculture-7393d.firebaseio.com/')

exit_code = os.system('ping -c 1 www.google.com')
if exit_code:
    gap1 = 60
    gap2 = 1800
else:
    gap1 = newdb.get('pi1-pond1', 'gap1')
    gap2 = newdb.get('pi1-pond1', 'gap2')

while True:
    exit_code = os.system('ping -c 1 www.google.com')
    if exit_code:
        GPIO.output(Relay_Ch2,GPIO.LOW)
        print("Channel 2:ON")
        time.sleep(gap1)
        GPIO.output(Relay_Ch2,GPIO.HIGH)
        print("Channe2 2:OFF")
        time.sleep(gap2)
    else:
        c=newdb.get('pi1-pond1', "auto")
        if c == 1:
            gap1 = newdb.get('pi1-pond1', 'gap1')
            gap2 = newdb.get('pi1-pond1', 'gap2')
            print('Gap1: ')
            print(gap1)
            print('Gap2: ')
            print(gap2)
            GPIO.output(Relay_Ch2,GPIO.LOW)
            print("Channel 2:ON")
            newdb.put('pi1-pond1',"ch2",1)
            time.sleep(gap1)
            GPIO.output(Relay_Ch2,GPIO.HIGH)
            print("Channel 2:OFF")
            newdb.put('pi1-pond1',"ch2",0)
            time.sleep(gap2)
        else:
            gap1 = newdb.get('pi1-pond1', 'gap1')
            gap2 = newdb.get('pi1-pond1', 'gap2')
            print('Gap1: ')
            print(gap1)
            print('Gap2: ')
            print(gap2)
            GPIO.output(Relay_Ch2,GPIO.LOW)
            newdb.put('pi1-pond1',"ch2",1)
            print("Channel 2:ON")
            time.sleep(gap1)
            GPIO.output(Relay_Ch2,GPIO.HIGH)
            newdb.put('pi1-pond1',"ch2",0)
            print("Channe2 2:OFF")
            time.sleep(gap2)
        
    
