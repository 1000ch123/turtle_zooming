# coding:UTF-8
# initialize
import serial
path = "/dev/" + input("please input path:/dev/")
print("port:",path)
baudRate = 57600
ser = serial.Serial(path,baudRate)
#ser.open()

def sendBytes(ls):
  for val in ls:
    ser.write(chr(val).encode())

def init():
  sendBytes([128,131])
  print("init:send(128,131)")

def led1on():
  sendBytes([139,8,0,255])
  print("led on:send(139,8,0,255)")

def moveForward():
  sendBytes([137,0,100,128,0])
  sendBytes([156,1,44])
  sendBytes([137,0,0,128,0])
  print("moveForward:30cm")

def moveBackward():
  sendBytes([137,255, 156,128,0])
  sendBytes([156,1,44])
  sendBytes([137,0,0,128,0])
  print("moveBackward:30cm")


def close():
  ser.close()
  print("close connection")
