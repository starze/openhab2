#!/usr/bin/env python

import minimalmodbus
import serial

__author__  = "Nick Ma"

class Nilan( minimalmodbus.Instrument ):
    """Instrument class for nilan heat pump. 
    communication via RS485 
    """
    
    HOLDINGREG_OFFSET = 10000

    def __init__(self, portname, slaveaddress=30):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

        self.serial.baudrate = 19200
        self.serial.parity = serial.PARITY_EVEN
        self.serial.timeout = 1.0  #timeout to 1000ms because I discovered roundtrip times as high as 898.5 ms

        self.mode = minimalmodbus.MODE_RTU
        
    
    def is_manual_loop1(self):
        """Return True if loop1 is in manual mode."""
        return self.read_register(273, 1) > 0
    
     
    def get_t11Top(self):
        """Return the setpoint (SP) target for loop1."""
        return self.read_register(211, numberOfDecimals=2, 
            signed=True, functioncode=4)
   
    def get_userVent(self):
        """This is a holding register -> functioncode=3"""
        return self.read_register(1003, numberOfDecimals=0, signed=False, functioncode=3) 

    def set_userVent(self, speed=2):
	if (speed<0) or (speed>4):
            return
        return self.write_register(1003, speed)

    
########################
## Testing the module ##
########################

if __name__ == '__main__':
    NILAN_SERIAL_PORT = '/dev/ttyUSB0'

    print( 'TESTING Nilan Connection')

    n = Nilan(NILAN_SERIAL_PORT)
    n.debug = True
    print(n)

    ## starting demo
    old_userVent_value = n.get_userVent()
    print( 'old userVentSet:             {0}'.format( old_userVent_value ))

    n.debug = False
    new_designated_userVent = 1 if old_userVent_value==2 else 2
    n.set_userVent(new_designated_userVent)
    print( 'new userVentSet:             {0}'.format( n.get_userVent()       ))

    print( 'Connection to the Nilan instrument looks good!' )

pass    
