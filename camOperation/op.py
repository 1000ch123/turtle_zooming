# coding:UTF-8
# initialize
import serial
import struct as st
path = "/dev/" + input("please input path:/dev/")
print("port:",path)
baudRate = 57600
ser = serial.Serial(path,baudRate)

def sendBytes(ls):
  ser.write(bytes(ls))

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

def back():
  sendBytes([137,255,156,128,0])
  sendBytes([156,254,212])
  sendBytes([137,0,0,128,0])
  print("moveBackward:30cm")

def vel_forward():
  sendBytes([137,0,100,128,0])
  print("spd:100[mm/s]")

def vel_backward():
  sendBytes([137,255,156,128,0])
  print("spd:-100[mm/s]")

def stop():
  sendBytes([137,0,0,128,0])
  print("spd:stop")

def ccw(deg=360):
  sendBytes([137,0,100,0,1])
  sendBytes([157,0,90])
  sendBytes([137,0,0,128,0])
  print("rotate_CCW")

def cw(deg=360):
  sendBytes([137,0,100,255,255])
  sendBytes([157,255,165])
  sendBytes([137,0,0,128,0])
  print("rotate_CW")

def close():
  ser.close()
  print("close connection")
