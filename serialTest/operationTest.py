#coding:utf-8


# easy sender
def sendBytes(serial,ls):
  for val in ls:
    serial.write(chr(val).encode())

if __name__ == "__main__":
  # initialize
  import serial
  portPath = "/dev" + input("please input port path:/dev")
  print("port path " + portPath)
  ser = serial.Serial(portPath,57600)
  #ser.open()

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
