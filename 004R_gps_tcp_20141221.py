#!/usr/bin/python
#written by Aneesh PA, on 21 Dec 2014
#reads gps data from serial interface, rapi's gpio and
#pushes relevant fields into a string, which is then 
#written to a file 
#Also gets a snap from cam every 10 seconds and then
#saves it into the pic folder
#also sets the timestamp of rapi using gps

import datetime 	#just for testing
import serial
import time
from pynmea import nmea
import subprocess
#import picamera
import socket
import sys
 
serial_port="/dev/ttyAMA0"
baudrate=9600
server_addr=('***.***.***.***',53005)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)


def getGpsData():
    '''Writes latest gps string to the file'''
    appId = "A"         #A = GPS tracker
    messageId = "A"     # A = GPS data, B = storing GPS data
    Imei = "355435047096119"    #IMEI 15 chars
    GpsFix ="0"     #A=DataValid,B=invalid,X=GPSnotworkin,M = Masked
    GpsTime = "000000"  #hhmmss, use GPRMC
    GpsDate = "000000"  #ddmmyy, use GPRMC
    Lati = "0000.0000"  #ddmm.mmmm, use GGA
    NorthSouth = "0"    #N or S, use GGA
    Longi = "0000.0000" #ddmm.mmmm, use GGA
    EastWest = "0"      #E or W, use GGA
    Sog = "000000"      #speed over ground, use GPVTG
    Cog = "000000"      #course over ground, use GPVTG
    Sats = "00"       #no of satellites, use GPGGA
    Hdop = "0000"     #Horizontal dilution of precision, use GPGGA
    StrengthQual = "0000"   #signal strength and qual. of gprs
    PowerMode = "0"      #
    BatLevel = "000"
    AiVal = "0000"
    AiVal2 = "0000"
    #DailyDist = ""
    #OdoDist = ""
    DiStat = "0000"
    CrLf = '\n'+'\t'
    gpgga = nmea.GPGGA()
    gpgll = nmea.GPGLL()
    gpvtg = nmea.GPVTG()
    gprmc = nmea.GPRMC()
    ser = serial.Serial(serial_port, baudrate, timeout=5)
    #camera = picamera.PiCamera()
    for i in range(10):
	try:
            data = ser.readline()
        except serial.serialutil.SerialException:
	    pass
	if data.startswith('$GPGGA'):
            gpgga.parse(data)			#ref nmea
            Lati = gpgga.latitude
            Longi = gpgga.longitude
            Sats = gpgga.num_sats
            GpsFix = gpgga.timestamp
            NorthSouth = gpgga.lat_direction
            EastWest = gpgga.lon_direction
            Sats = gpgga.num_sats
            Hdop = gpgga.horizontal_dil
	    print "gpgga", Lati, Longi, Sats, GpsFix, Hdop
	elif data.startswith('$GPGLL'):
            gpgll.parse(data)
            klist = data.split(",")
            GpsFix = klist[6]
	    print "gpgll", GpsFix
	elif data.startswith('$GPVTG'):
            gpvtg.parse(data)
            Cog = gpvtg.true_track        
            Sog = gpvtg.spd_over_grnd_kts
	    print "gpvtg", Cog, Sog
	elif data.startswith('$GPRMC'):
            gprmc.parse(data)
            GpsDate = gprmc.datestamp
            GpsTime = gprmc.timestamp
	    print "gprmc", GpsTime, GpsDate
    msgString = appId + messageId + Imei + GpsFix + GpsTime + \
      	GpsDate + Lati + NorthSouth + Longi + EastWest + \
      	Sog + Cog + Sats + Hdop + StrengthQual + PowerMode + \
      	BatLevel + AiVal + AiVal2 + DiStat + CrLf
    print >>sys.stderr, msgString
    ser.close()
    #sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.connect(server_addr)
    print >>sys.stderr, 'sending ...'
    try:
        sock.sendall(msgString)
    finally:
        print >>sys.stderr, 'closing socket'
        #sock.close()


if __name__== '__main__':
    while 1:
        getGpsData()
	time.sleep(10)


