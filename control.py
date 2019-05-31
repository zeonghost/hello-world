#!/usr/bin/env python
import temp
import tempuplode
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
#firebase = firebase.FirebaseApplication('https://testproject-9c322.firebaseio.com/')
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

high=newdb.get('pi1-pond1', "high")
low=newdb.get('pi1-pond1', "low")

b=300
'''
def ch2On():
    GPIO.output(Relay_Ch2,GPIO.LOW)
    print("Channel 2: ON")
    newdb.put('pi1-pond1',"ch2",1)
    time.sleep(60);
    GPIO.output(Relay_Ch2,GPIO.HIGH)
    print("Channel 2: OFF")
    newdb.put('pi1-pond1',"ch2",0)

def ch2Off():
    GPIO.output(Relay_Ch2,GPIO.HIGH)
    print("Channel 2: OFF")
    newdb.put('pi1-pond1',"ch2",0)
'''

def run_threaded(job_func):
     job_thread = threading.Thread(target=job_func)
     job_thread.start()
    

schedule.every().hour.at(":00").do(run_threaded, tempuplode.up)
schedule.every(10).minutes.do(run_threaded, tempuplode.upa)
#schedule.every(1).minutes.do(run_threaded, ch2On)
#schedule.every(2).minutes.do(run_threaded, ch2Off)

while True:
    a=temp.getTemp()
    tempuplode.rec()
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
        schedule.run_pending()
        high=newdb.get('pi1-pond1', "high")
        low=newdb.get('pi1-pond1', "low")
        if b != a:
            newdb.put('pi1-pond1',"temp",a)
            b=a
        c=newdb.get('pi1-pond1', "au to")
        if c == 0:
            print("Automatic: off");
            d = newdb.get('pi1-pond1', "ch1")
            e = newdb.get('pi1-pond1', "ch2")
            if d == 1:
                GPIO.output(Relay_Ch1,GPIO.LOW)
                print("Channel 1:ON")
            else:
                GPIO.output(Relay_Ch1,GPIO.HIGH)
                print("Channel 1:OFF")
            if e == 1:
                GPIO.output(Relay_Ch2,GPIO.LOW)
                print("Channel 2:ON")
            else:
                GPIO.output(Relay_Ch2,GPIO.HIGH)
                print("Channel 2:OFF")
        else:
            if a > high or a < low:
                GPIO.output(Relay_Ch1,GPIO.LOW)
                print("Channel 1:ON")
                newdb.put('pi1-pond1',"ch1",1)
            else:
                GPIO.output(Relay_Ch1,GPIO.HIGH)
                print("Channel 1:OFF")
                newdb.put('pi1-pond1',"ch1",0)
        time.sleep(1)
    
