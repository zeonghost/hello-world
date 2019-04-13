#!/usr/bin/env python
import pymodbus
import serial.rs485
from pymodbus.client.common import *
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import RPi.GPIO as GPIO
import time

Relay_Ch1 = 26
Relay_Ch2 = 20
Relay_Ch3 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)

client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, stopbits = 1, bytesize = 8,  parity='N', baudrate= 9600)
client.connect()


while True:
    rr = client.read_holding_registers(7, 1, unit=1)
    print "The temperature is ", rr.registers[0] / 10.0,"Celsius"
    a=rr.registers[0]
    if a > 320 or a < 290 :
        GPIO.output(Relay_Ch1,GPIO.LOW)
        print("Channel 1:The Common Contact is access to the Normal Open Contact!")
        time.sleep(0.5)
    else:
        GPIO.output(Relay_Ch1,GPIO.HIGH)
        print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(0.5)
    
