### python-oscでosc通信使うまで
#### 準備
pythonのバージョンを3.3にしましょう．  
python2系とpython3系の両立はできるみたい．winで確認済み.  
python3をインストールついでにsetuptools導入．次いでpipインストール．  
pipのインストールは公式サイトを参考．easy_install pipではダメでした．なんで？  

#### server:受信する方
usage  
python server.py [--ip address] [--port portnum]

はじめに処理用関数を定義．
メイン中でディスパッチャにルーティング処理登録．
サーバインスタンス生成．ここでディスパッチャを登録．
server起動！

jsの無名関数の素晴らしさがわかる．

#### client:送信する方
usage  
python client.py [--ip address] [--port portnum]

当然だけどサーバとそろえましょう．

基本的にはクライアントインスタンスを生成．  
任意タイミングで適宜メッセージを作成，sendすればよい．

### iosからosc受信するまで
ipアドレスを毎回確認するのが面倒．
```python
import socket
socket.gethostbyname(socket.gethostname())
```
らしい．  
しかしこれで取得できるのはethernetIPみたい．

### turtlebotPCにiphoneから飛ばすまで
#####turtlebot側(server)
```
# baffalo-G-BB64につなぎましょう
cd masa/turtle_zooming/oscTest
pythonbrew use 3.3.1 #3.3.2が見つからないようなので.
python server.py --ip 192.168.11.xx --port 12345
```

##### iphone側(client)  
**wifi:Baffalo-G-BB64につなぐ！**  
まずXCodeで
```
_host = @"192.168.11.xx" //上と揃える
_port = @"12345"
```
基本的にこの状態でつながるはず．．なのだが．．

* konashiが反応しない！  
iPhoneとkonashiがつながってない．bluetooth周りのエラーのよう．
対応策不明．一応本体電源切ってうんぬんすると治ったり治らなかったり．

* ubuntuに値が飛んでない！  
wifi確認．Baffalo-g-bb64につながっているか？ipは正しいか？
