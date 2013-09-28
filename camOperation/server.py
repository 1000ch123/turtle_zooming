#coding:utf-8

#util
import argparse
import math
import socket

#osc
from pythonosc import dispatcher
from pythonosc import osc_server

#serial
import serial
import struct as st

# serial
def sendBytes(ls):
  for val in ls:
    #binary = st.pack("!L",val)
    #ser.write(binary)
    ser.write(chr(val).encode())
    #ser.write(str(val).encode())

def initTurtle():
  sendBytes([128,131])
  print("init:send(128,131)")

def goFront():
  sendBytes([137,0,100,128,0])
  sendBytes([156,1,44])
  sendBytes([137,0,0,128,0])
  print("moveForward:30cm")

def goBack():
  sendBytes([137,255,156,128,0])
  sendBytes([156,254,212])
  sendBytes([137,0,0,128,0])
  print("moveBackward:30cm")

def turnCCW(deg=360):
  sendBytes([137,0,100,0,1])
  sendBytes([157,0,90])
  sendBytes([137,0,0,128,0])
  print("rotate_CCW")

def turnCW(deg=360):
  sendBytes([137,0,100,255,255])
  sendBytes([157,255,165])
  sendBytes([137,0,0,128,0])
  print("rotate_CW")

# OSC
def print_filter(args,val,count):
  print("here:",count,":",val)

def print_lenseValue(args):
  print("lense:",args[0])

def lense_left(args):
  print("lense_left")
  #todo:go_front
  #wainÇÕÇ≥ÇﬁÇ©ÇÁëÂè‰ïvÇ©ÅH
  goFront()

def lense_right(args):
  print("lense_right")
  #todo:_go_back
  turnCCW()

if __name__ == "__main__":
  #serialInit
  path = "/dev/" + input("please input path:/dev/")
  print("port:",path)
  baudRate = 57600
  ser = serial.Serial(path,baudRate)
    
  # parse input args
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=12345, help="The port to listen on")
  args = parser.parse_args()
  
  if args.ip == "127.0.0.1":
    host = socket.gethostbyname(socket.gethostname())
  else:
    host = args.ip
  print("hostAddress:",host)
  
  # dispatcher
  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/debug", print)
  dispatcher.map("/filter",print_filter,"arg1")
  dispatcher.map("/left" ,lense_left ,"L")
  dispatcher.map("/right",lense_right,"R")

  # make server
  print("ip:",host," port",args.port)
  server = osc_server.ThreadingOSCUDPServer(
      (host, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
