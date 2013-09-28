# coding:UTF-8
# initialize
import serial
import struct as st
path = "/dev/" + input("please input path:/dev/")
print("port:",path)
baudRate = 57600
ser = serial.Serial(path,baudRate)

def sendBytes(ls):
  for val in ls:
    #binary = st.pack("!L",val)
    #ser.write(binary)
    #ser.write(chr(val).encode())
    tmp = bytes([val])
    print("send:",val," as:",tmp)
    ser.write(tmp)

def init():
  sendBytes([128,131])
  print("init:send(128,131)")

def led1on():
  sendBytes([139,8,0,255])
  print("led on:send(139,8,0,255)")

def go():
  sendBytes([137,0,100,128,0])
  sendBytes([156,1,44])
  sendBytes([137,0,0,128,0])
  print("moveForward:30cm")

def goFast():
  sendBytes([137,0,200,128,0])
  sendBytes([156,1,44])
  sendBytes([137,0,0,128,0])
  print("moveForwardFast:30cm")

def goSlow():
  sendBytes([137,0,50,128,0])
  sendBytes([156,1,44])
  sendBytes([137,0,0,128,0])
  print("moveForwardFast:30cm")

def back():
  sendBytes([137,255,156,128,0])
  sendBytes([156,254,212])
  sendBytes([137,0,0,128,0])
  print("moveBackward:30cm")

def backFast():
  sendBytes([137,255,56,128,0])
  sendBytes([156,254,212])
  sendBytes([137,0,0,128,0])
  print("moveBackward:30cm")

def backSlow():
  sendBytes([137,255,206,128,0])
  sendBytes([156,254,212])
  sendBytes([137,0,0,128,0])
  print("moveBackward:30cm")

def ccw(deg=360):
  sendBytes([137,0,100,0,1])
  sendBytes([157,0,90])
  sendBytes([137,0,0,128,0])
  print("rotate_CCW")

def cw(deg=360):
  #ìÆÇ´Ç™Ç®Ç©ÇµÇ¢ÅDíºêiÇµÇƒÇÈ
  sendBytes([137,0,100,255,255])
  sendBytes([157,255,165])
  sendBytes([137,0,0,128,0])
  print("rotate_CW")

def connect():
  ser = serial.Serial(path,baudRate)

def close():
  ser.close()
  print("close connection")
