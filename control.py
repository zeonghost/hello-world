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

GPIO.output(Relay_Ch1,GPIO.HIGH)
GPIO.output(Relay_Ch2,GPIO.HIGH)
GPIO.output(Relay_Ch3,GPIO.HIGH)
#relay setup defult off

high=400
low=200

b=300
e=0

while True:
    a=temp.getTemp()
    #tempuplode.rec()
    exit_code = os.system('ping -c 1 www.google.com')
    if exit_code:
        print("No Internet Connection, Offline Model")
        if a > high or a < low:
            GPIO.output(Relay_Ch1,GPIO.LOW)
            print("Channel 1:ON")
        else:
            GPIO.output(Relay_Ch1,GPIO.HIGH)
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
            if d == 1:
                GPIO.output(Relay_Ch1,GPIO.LOW)
                print("Channel 1:ON")
            else:
                GPIO.output(Relay_Ch1,GPIO.HIGH)
                print("Channel 1:OFF")
        else:
            if a > high or a < low:
                GPIO.output(Relay_Ch1,GPIO.LOW)
                print("Channel 1:ON")
                if e != 1:
                     newdb.put('pi1-push',"warn",1)
                     newdb.put('pi1-pond1',"ch1",1)
                e = 1
            else:
                GPIO.output(Relay_Ch1,GPIO.HIGH)
                print("Channel 1:OFF")
                if e != 0:
                     newdb.put('pi1-pond1',"ch1",0)
                e = 0
        time.sleep(1)
    

    

