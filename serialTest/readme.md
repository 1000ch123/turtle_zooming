### TurtleBot動かすよ
sshでturtlebotPCに入り込む.
usr:turtlebot  
pass:turtlebot

pyserial入ってないみたい
```
pythonbrew use 3.3.1
pip install pyserial
```

```python
import serial
path = input("please input path")
baudRate = 57600
ser = serial.Serial(path,baudRate) # automatically port open

#serialでの値送信
ser.write(chr(number).encode())
```

### operation 基本
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

単純に16進数でこの範囲の数を表現すればok．
負数はbit反転して+=1する．
1dataあたり32bitなので注意．

結局与えるnumberはintなので，
基本的には数字そのまま打てばokな気がする.

0~255: 0,vel  
256~500: 1,vel-256  

-1~-256:255,256 - abs(vel)  
-257~-500:254,256 - abs(vel-255)
