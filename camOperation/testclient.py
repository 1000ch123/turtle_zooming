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

  key = input("command?:[(h)elp]") 
  while True:
    if key == "l":
      print("send:/vel_ccw")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_ccw")
      msg = msg.build()
      client.send(msg)
      time.sleep(1)
    elif key == "r":
      print("send:/vel_cw")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_cw")
      msg = msg.build()
      client.send(msg)
      time.sleep(1) 
    elif key == "f":
      print("send:/vel_forward")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_forward")
      msg = msg.build()
      client.send(msg)
      time.sleep(1) 
    elif key == "b":
      print("send:/vel_backward")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_backward")
      msg = msg.build()
      client.send(msg)
      time.sleep(1) 
    elif key == "s":
      print("send:/vel_stop")
      msg = osc_message_builder.OscMessageBuilder(address = "/vel_stop")
      msg = msg.build()
      client.send(msg)
      time.sleep(1) 
    elif key == "q":
      print("finish client")
      break
    elif key == "h":
      str = """
      Command List
      f :forward
      b :back
      s :stop

      l :ccw
      r :cw
      
      q :quit
      h :help

      each sleep time:0.1[sec]
      """
      print(str)
    else:
      print("wrong message.please look [h]elp")
      pass
    key = input("command?:[(h)elp]")

