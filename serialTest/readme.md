### TurtleBot��������
ssh��turtlebotPC�ɓ��荞��.
usr:turtlebot  
pass:turtlebot

pyserial�����ĂȂ��݂���
```
pythonbrew use 3.3.1
pip install pyserial
```

```python
import serial
path = input("please input path")
baudRate = 57600
ser = serial.Serial(path,baudRate) # automatically port open

#serial�ł̒l���M
ser.write(chr(number).encode())
```

### operation ��{
* init:128
usage:[init][mode]

 + mode
  - full:132
  - safe:131

* led:139

* drive:137
usage:[drive][vel_high][vel_low][rad_high][rad_low]

vel:-500 ~ 500 [mm/s]
rad:-2000 ~ 2000 [mm(?)]

�P����16�i���ł��͈̔͂̐���\�������ok�D
������bit���]����+=1����D
1data������32bit�Ȃ̂Œ��ӁD

���Ǘ^����number��int�Ȃ̂ŁC
��{�I�ɂ͐������̂܂ܑłĂ�ok�ȋC������.

0~255: 0,vel  
256~500: 1,vel-256  

-1~-256:255,256 - abs(vel)  
-257~-500:254,256 - abs(vel-255)
