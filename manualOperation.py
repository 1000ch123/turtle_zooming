# coding:UTF-8
# initialize
import serial
ser = serial.Serial("/dev/ttyUSB1",57600)
ser.open()

# easy sender
def sendBytes(ls):
  for val in ls:
    ser.write(chr(val))


