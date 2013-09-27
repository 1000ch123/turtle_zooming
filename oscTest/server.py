#coding:utf-8
import argparse
import math
import socket

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def print_lenseValue(args,argv):
  print("here",args[0])

if __name__ == "__main__":
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
  dispatcher.map("/volume", print_volume_handler, "Volume")
  dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)
  dispatcher.map("/filter",print_lenseValue,"arg1","arg2","arg3")
  dispatcher.map("/left",print_lenseValue,"L")
  dispatcher.map("/right",print_lenseValue,"R")

  # make server
  print("ip:",host," port",args.port)
  server = osc_server.ThreadingOSCUDPServer(
      (host, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
