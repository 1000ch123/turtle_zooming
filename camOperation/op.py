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
def go():
  vel=50
  length=20
  sendBytes([137,0,vel,128,0])
  sendBytes([156,0,length])
  sendBytes([137,0,0,128,0])
  print("move_go:")

def back():
  vel= 255 - 200
  length= 255 - 20
  sendBytes([137,255,vel,128,0])
  sendBytes([156,255,length])
  sendBytes([137,0,0,128,0])
  print("move_back:")

def ccw():
  sendBytes([137,0,100,0,1])
  sendBytes([157,0,45])
  sendBytes([137,0,0,128,0])
  print("rotate_CCW")

def cw():
  sendBytes([137,0,100,255,255])
  sendBytes([157,255,210])
  sendBytes([137,0,0,128,0])
  print("rotate_CW")

#velŽw’è
def vel_forward():
  sendBytes([137,0,100,128,0])
  print("spd:100[mm/s]")

def vel_backward():
  sendBytes([137,255,155,128,0])
  print("spd:-100[mm/s]")

def vel_ccw():
  sendBytes([137,0,100,0,1])
  print("spd:100[ccw]")

def vel_cw():
  sendBytes([137,0,100,255,255])
  print("spd:100[cw]")

def stop():
  sendBytes([137,0,0,128,0])
  print("spd:stop")

#connection
def close():
  ser.close()
  print("close connection")
