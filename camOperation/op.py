# coding:UTF-8
# initialize
import serial
import struct as st
path = "/dev/" + input("please input path:/dev/")
print("port:",path)
baudRate = 57600
ser = serial.Serial(path,baudRate)

# util
def sendBytes(ls):
  ser.write(bytes(ls))

# base 
def init():
  sendBytes([128,131])
  print("init:send(128,131)")

def led1on():
  sendBytes([139,8,0,255])
  print("led on:send(139,8,0,255)")

# lenŽw’è
def go(length=10):
  sendBytes([137,0,100,128,0])
  sendBytes([156,0,length])
  sendBytes([137,0,0,128,0])
  print("move_go:",length)

def back(length=10):
  sendBytes([137,255,156,128,0])
  sendBytes([156,255,255 - length])
  sendBytes([137,0,0,128,0])
  print("move_back:",length)

def ccw(deg=10):
  sendBytes([137,0,100,0,1])
  sendBytes([157,0,deg])
  sendBytes([137,0,0,128,0])
  print("rotate_CCW")

def cw(deg=10):
  sendBytes([137,0,100,255,255])
  sendBytes([157,255,255-deg])
  sendBytes([137,0,0,128,0])
  print("rotate_CW")

#velŽw’è
def vel_forward(vel=100):
  sendBytes([137,0,vel,128,0])
  print("spd:",vel,"[mm/s]")

def vel_backward(vel=100):
  sendBytes([137,255,255-vel,128,0])
  print("spd:-",vel,"[mm/s]")

def vel_ccw(vel=100):
  sendBytes([137,0,vel,0,1])
  print("spd:",vel,"[ccw]")

def vel_cw(vel=100):
  sendBytes([137,0,vel,255,255])
  print("spd:",vel,"[cw]")

def stop():
  sendBytes([137,0,0,128,0])
  print("spd:stop")

#connection
def close():
  ser.close()
  print("close connection")
