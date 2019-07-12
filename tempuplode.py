#!/usr/bin/env python
from firebase import firebase
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import time
from datetime import datetime, timedelta
import temp
import sys
import os
import schedule
import threading

new = []
new1 = []

newdb = firebase.FirebaseApplication('https://aquaculture-7393d.firebaseio.com/')


with open('save.txt', 'r+') as f:
    line=f.readline()
    if line != "":
        line=line.replace("\n", "")
        line=line.strip()
        line=line.replace(' ', '')
        c=line.replace("\r", "")
        c=int(c)
        new.append(c)
        
with open('save1.txt', 'r+') as f2:
    line1=f2.readline()
    if line1 != "":
        line1=line1.replace("\n", "")
        line1=line1.strip()
        line1=line1.replace(' ', '')
        d=line1.replace("\r", "")
        d=int(d)
        new1.append(d)
        

def up():
    nsum=0
    nsum+=sum(new)
    average=nsum/len(new)
    #newdb.post("/pi1-temp-fore", {"val":average, "time":time.mktime(datetime.now().timetuple())})
    newdb.post("/pi1-forecast-test", {"val":average, "date": time.strftime("%b %d, %Y", time.localtime()),"time":time.strftime("%I:%M %p", time.localtime())})
    print('uplode to database')
    new[:]=[]
    open('save.txt', 'w').close()
    print("save.txt has been clear")


def upa():
    nsum1=0
    nsum1+=sum(new1)
    average1=nsum1/len(new1)
    newdb.post("/pi1-temp", {"val":average1, "time":time.mktime(datetime.now().timetuple())})
    print('uplode to database')
    new1[:]=[]
    open('save1.txt', 'w').close()
    print("save1.txt has been clear")

def rec():
    a=temp.getTemp()
    print(a)
    new.append(a)
    new1.append(a)
    b=str(a)
    with open("save.txt", "a") as f:
        f.writelines([b, '\n'])
    with open("save1.txt", "a") as f1:
        f1.writelines([b, '\n'])

def run_threaded(job_func):
     job_thread = threading.Thread(target=job_func)
     job_thread.start()
    
schedule.every().hour.at(":00").do(run_threaded, up)
schedule.every(10).minutes.do(run_threaded, upa)

while True:
    rec()
    time.sleep(1)
    schedule.run_pending()
    


