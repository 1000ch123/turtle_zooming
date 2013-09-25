#coding:utf-8

# initialize
import serial
ser = serial.Serial("/dev/ttfUSB0",57600)
ser.open()

# setup
sendBytes([128])
sendBytes([131])

# led
sendBytes([139,8,0,255])

# easy sender
def sendBytes(ls):
  for val in ls:
    ser.write(chr(val))
