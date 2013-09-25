# coding:UTF-8
# easy sender
def sendBytes(ls):
  for val in ls:
    ser.write(chr(val))

# initialize
import serial
ser = serial.Serial("/dev/ttyUSB0",57600)
ser.open()


