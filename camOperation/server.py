#coding:utf-8

#util
import argparse
import math
import socket

#osc
from pythonosc import dispatcher
from pythonosc import osc_server

#serial
import op 

# OSC
def print_filter(args,val,count):
  print("here:",count,":",val)

def print_lenseValue(args):
  print("lense:",args[0])

def vel_ccw(args):
  print("vel_ccw")
  #todo:go_front
  op.vel_ccw()
  
def vel_cw(args):
  print("vel_cw")
  #todo:_go_back
  op.vel_cw()

def vel_forward(args):
  print("vel_forward")
  op.vel_forward()

def vel_backward(args):
  print("vel_backward")
  op.vel_backward()

def vel_stop(args):
  print("vel_stop")
  op.stop()

def finish_connect(args):
  print("client disconnected. Bye.")

if __name__ == "__main__":
  #serial
  op.init()
  
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
  dispatcher.map("/vel_ccw" ,vel_ccw ,"L")
  dispatcher.map("/vel_cw"  ,vel_cw,"R")
  dispatcher.map("/vel_forward",vel_forward,"f")
  dispatcher.map("/vel_backward",vel_backward,"b")
  dispatcher.map("/vel_stop",vel_stop,"s")
  dispatcher.map("/finish",finish_connect,"q")
  
  # make server
  print("ip:",host," port",args.port)
  server = osc_server.ThreadingOSCUDPServer(
      (host, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
