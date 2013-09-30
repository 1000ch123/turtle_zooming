#coding:utf-8

"""
This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=12345,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.UDPClient(args.ip, args.port)

  key = input("command?:") 
  while True:
    if key == "l":
      print("send:/left")
      msg = osc_message_builder.OscMessageBuilder(address = "/left")
      msg = msg.build()
      client.send(msg)
      time.sleep(3)   
    elif key == "r":
      print("send:/right")
      msg = osc_message_builder.OscMessageBuilder(address = "/right")
      msg = msg.build()
      client.send(msg)
      time.sleep(3) 
    elif key == "f":
      print("send:/vel_forward")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_forward")
      msg = msg.build()
      client.send(msg)
      time.sleep(3) 
    elif key == "b":
      print("send:/vel_backward")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_backward")
      msg = msg.build()
      client.send(msg)
      time.sleep(3) 
    elif key == "s":
      print("send:/vel_stop")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_stop")
      msg = msg.build()
      client.send(msg)
      time.sleep(3) 
    elif key == "q":
      print("finish client")
      break
    else:
      print("wrong message.please input[l/r/q]")
      pass
    key = input("command?:[l(eft)/r(ight)/q(uit)]")

