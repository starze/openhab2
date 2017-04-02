#!/usr/bin/env python3
# -*- coding: ISO-8859-1 -*-
# https://github.com/starze/openhab2 
# https://github.com/roggmaeh/nilan-openhab

import minimalmodbus
import serial
import os, sys
import csv
import httplib2

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 30, mode='rtu') # port name, slave address (in decimal)
instrument.serial.port
instrument.serial.baudrate = 19200   # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout  = 2   # seconds
#instrument.debug = True

h = httplib2.Http()

with open('nilan_modbus.csv') as csvfile:

	reader = csv.DictReader(csvfile, delimiter=',')
	for row in reader:
		if row['Register Type'] == "Input":
			fc = 4
		elif row['Register Type'] == "Holding":
			fc = 3
		
		if row['Unit'] == "text" or row['Unit'] == "ascii":
			strRet = instrument.read_string(int(row['Address']), numberOfRegisters=1, functioncode=fc)
			lst = list(strRet)
			strRet = lst[1] + lst[0]
		elif row['Scale'] == "100":
			strRet = instrument.read_register(int(row['Address']), numberOfDecimals=2, functioncode=fc)
		else:
			strRet = instrument.read_register(int(row['Address']), numberOfDecimals=0, functioncode=fc)
		
		if row['Unit'] == "%" or row['Unit'] == "°C":
			print("%s: %s %s" % (row['Name'], strRet, row['Unit']))
			h.request("http://localhost:8080/rest/items/" + row['Name'] + "/state", "PUT", body=str(strRet))
		else:
			print("%s: %s" % (row['Name'], strRet))
			h.request("http://localhost:8080/rest/items/" + row['Name'] + "/state", "PUT", body=str(strRet))
