#!/usr/bin/env python
import gc
import pymodbus
import serial.rs485
from pymodbus.client.common import *
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, stopbits = 1, bytesize = 8,  parity='N', baudrate= 9600)
client.connect()

def getTemp():
    rr = client.read_holding_registers(7, 1, unit=1)
    #print "The temperature is ", rr.registers[0] / 10.0,"Celsius"
    a=rr.registers[0]
    del rr.registers[0]
    gc.collect()
    return a

