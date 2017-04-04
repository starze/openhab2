#!/usr/bin/env python3
# -*- coding: ISO-8859-1 -*-
# https://github.com/starze/openhab2 
# https://github.com/roggmaeh/nilan-openhab

import os, sys
import csv

celsius = chr(176) + "C"

with open('nilan_modbus.csv') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',')
	for row in reader:
		if row['Unit'] == "text" or row['Unit'] == "ascii":
			print("String\t%s\t\t\"%s [%ss]\" (gNilanInput)" % (row['Name'], row['Description'], chr(37)))
		elif row['Unit'] == "%":
			print("Number\t%s\t\t\"%s [%s.1f] %s\" (gNilanInput)" % (row['Name'], row['Description'], chr(37), chr(37)))
		elif row['Unit'] == celsius or row['Unit'] == "°C":
			print("Number\t%s\t\t\"%s [%s.1f] %sC\" <temperature> (gNilanInput)" % (row['Name'], row['Description'], chr(37), chr(176)))
		else:
			print("Number\t%s\t\t\"%s [%sd]\" (gNilanInput)" % (row['Name'], row['Description'], chr(37)))
