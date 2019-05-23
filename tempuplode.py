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

new = []

#cred = credentials.Certificate("./serviceKey.json")
#app = firebase_admin.initialize_app(cred)
#store = firestore.client()


newdb = firebase.FirebaseApplication('https://aquaculture-7393d.firebaseio.com/')
#firebase = firebase.FirebaseApplication('https://testproject-9c322.firebaseio.com/')

with open('save.txt', 'r+') as f:
    line=f.readline()
    if line != "":
        line=line.replace("\n", "")
        line=line.strip()
        line=line.replace(' ', '')
        c=line.replace("\r", "")
        c=int(c)
        new.append(c)

def calTemp():
    if len(new) > 50:
        nsum=0
        nsum+=sum(new)
        average=nsum/len(new)
        #data={u'val' :average}
        #doc_ref = store.collection(u'pi/pi1/pond1/temp')
        #doc_ref.add({u'val': average, u'time': (datetime.now()-timedelta(hours=8))})
        #data={u(datetime.now()-timedelta(hours=8)): average}
        #store.collection(u'pi/pi1/pond1').document(u'temp').set(data)
        #firebase.put('pi1-temp', datetime.now()-timedelta(hours=8), average)
        #newdb.put("/pi1-temp", datetime.now().strftime("%b%d%Y-%H%S"), average)
        #newdb.post("/pi1-temp", {"val":average, "time":datetime.now().strftime("%b%d%Y-%H:%M")})
        newdb.post("/pi1-temp", {"val":average, "time":time.mktime(datetime.now().timetuple())})
        print('uplode to database')
        new[:]=[]
        os.remove("save.txt")
    else:
        a=temp.getTemp()
        print(a)
        new.append(a)
        b=str(a)
        with open("save.txt", "a") as f:
            f.writelines([b, '\n'])
        time.sleep(5)


