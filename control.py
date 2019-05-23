#!/usr/bin/env python
import temp
import tempuplode
import RPi.GPIO as GPIO
import time
#declear of relay
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase import firebase
#firebase = firebase.FirebaseApplication('https://testproject-9c322.firebaseio.com/')
newdb = firebase.FirebaseApplication('https://aquaculture-7393d.firebaseio.com/')

#cred = credentials.Certificate("./aquaculture-7393d-firebase-adminsdk-xy9ar-5a66acf0d0.json")
#firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://aquaculture-7393d.firebaseio.com'
#})
#ref = db.reference('pi1-pond1')
#declear firebase address

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
#relay

high=newdb.get('pi1-pond1', "high")
low=newdb.get('pi1-pond1', "low")

#high=ref.get('high')
#low=ref.get('low')

b=300

while True:
    a=temp.getTemp()
    tempuplode.calTemp()
    if b != a:
        newdb.put('pi1-pond1',"temp",a)
        #ref.update({'temp': a})
        b=a
    c=newdb.get('pi1-pond1', "auto")
    #c=ref.get('auto')
    if c == 0:
        print("Automatic: off");
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
            newdb.put('pi1-pond1',"ch1",1)
            #ref.update({'ch1', 1})
        else:
            GPIO.output(Relay_Ch1,GPIO.HIGH)
            print("Channel 1:OFF")
            newdb.put('pi1-pond1',"ch1",0)
            #ref.update('ch1', 0)
    time.sleep(5)
    

    

