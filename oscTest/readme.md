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
