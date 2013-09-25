#coding:utf-8


# easy sender
def sendBytes(ls):
  for val in ls:
    ser.write(chr(val))

if __name__ == "__main__"
  # initialize
  import serial
  ser = serial.Serial("/dev/ttyUSB0",57600)
  ser.open()

  # setup
  sendBytes([128])
  sendBytes([131])

  # led
  sendBytes([139,8,0,255])


