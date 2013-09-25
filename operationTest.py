#coding:utf-8


# easy sender
def sendBytes(ls):
  for val in ls:
    ser.write(chr(val))

if __name__ == "__main__":
  # initialize
  import serial
  ser = serial.Serial("/dev/ttyUSB0",57600)
  ser.open()

  # setup
  sendBytes([128,131])

  # led
  sendBytes([139,8,0,255])

  # move
  sendBytes([137,0,100,128,0])
  sendBytes([156,1,44])
  sendBytes([137,0,0,128,0])
