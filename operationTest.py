#coding:utf-8


# easy sender
def sendBytes(ser,ls):
  for val in ls:
    ser.write(chr(val))

if __name__ == "__main__":
  # initialize
  import serial
  portPath = raw_input("please input port path")
  ser = serial.Serial(portPath,57600)
  ser.open()

  # setup
  sendBytes(ser,[128,131])

  # led
  sendBytes(ser,[139,8,0,255])

  # move
  sendBytes(ser,[137,0,100,128,0])
  sendBytes(ser,[156,1,44])
  sendBytes(ser,[137,0,0,128,0])

  # close
  ser.close()
