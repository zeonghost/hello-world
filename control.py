#!/usr/bin/env python
import temp
#import tempuplode
import RPi.GPIO as GPIO
import time
import schedule
import os
import threading
#declear of relay
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase import firebase

newdb = firebase.FirebaseApplication('https://aquaculture-7393d.firebaseio.com/')

Relay_Ch1 = 26
Relay_Ch2 = 20
Relay_Ch3 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)

high=400
low=200

b=300

while True:
    a=temp.getTemp()
    exit_code = os.system('ping -c 1 www.google.com')
    if exit_code:
        print("No Internet Connection, Offline Model")
        if a > high or a < low:
            GPIO.output(Relay_Ch3,GPIO.LOW)
            print("Channel 1:ON")
        else:
            GPIO.output(Relay_Ch3,GPIO.HIGH)
            print("Channel 1:OFF")
    else:
        high=newdb.get('pi1-pond1', "high")
        low=newdb.get('pi1-pond1', "low")
        if b != a:
            newdb.put('pi1-pond1',"temp",a)
            b=a
        c=newdb.get('pi1-pond1', "auto")
        if c == 0:
            print("Automatic: off");
            high=newdb.get('pi1-pond1', "high")
            low=newdb.get('pi1-pond1', "low")
            d = newdb.get('pi1-pond1', "ch1")
            if a > high or a < low:
                newdb.put('pi1-push',"warn",1)
            if d == 1:
                GPIO.output(Relay_Ch3,GPIO.LOW)
                print("Channel 1:ON")
            else:
                GPIO.output(Relay_Ch3,GPIO.HIGH)
                print("Channel 1:OFF")
            f = newdb.get('pi1-pond1', "ch3")
            if f == 1:
                GPIO.output(Relay_Ch1,GPIO.LOW)
                print("Channel 3:ON")
            else:
                GPIO.output(Relay_Ch1,GPIO.HIGH)
                print("Channel 3:OFF")
            g = newdb.get('pi1-pond1', "ch2")
            if g == 1:
                GPIO.output(Relay_Ch2,GPIO.LOW)
                print("Channel 2:ON")
            else:
                GPIO.output(Relay_Ch2,GPIO.HIGH)
                print("Channel 2:OFF")
        else:
            if a > high or a < low:
                GPIO.output(Relay_Ch3,GPIO.LOW)
                print("Channel 1:ON")
                newdb.put('pi1-push',"warn",1)
                newdb.put('pi1-pond1',"ch1",1)
            else:
                GPIO.output(Relay_Ch3,GPIO.HIGH)
                print("Channel 1:OFF")
                newdb.put('pi1-pond1',"ch1",0)
        time.sleep(1)
    

    

