### python-osc��osc�ʐM�g���܂�
#### ����
python�̃o�[�W������3.3�ɂ��܂��傤�D  
python2�n��python3�n�̗����͂ł���݂����Dwin�Ŋm�F�ς�.  
python3���C���X�g�[�����ł�setuptools�����D������pip�C���X�g�[���D  
pip�̃C���X�g�[���͌����T�C�g���Q�l�Deasy_install pip�ł̓_���ł����D�Ȃ�ŁH  

#### server:��M�����
usage  
python server.py [--ip address] [--port portnum]

�͂��߂ɏ����p�֐����`�D
���C�����Ńf�B�X�p�b�`���Ƀ��[�e�B���O�����o�^�D
�T�[�o�C���X�^���X�����D�����Ńf�B�X�p�b�`����o�^�D
server�N���I

js�̖����֐��̑f���炵�����킩��D

#### client:���M�����
usage  
python client.py [--ip address] [--port portnum]

���R�����ǃT�[�o�Ƃ��낦�܂��傤�D

��{�I�ɂ̓N���C�A���g�C���X�^���X�𐶐��D  
�C�Ӄ^�C�~���O�œK�X���b�Z�[�W���쐬�Csend����΂悢�D

### ios����osc��M����܂�
ip�A�h���X�𖈉�m�F����̂��ʓ|�D
```python
import socket
socket.gethostbyname(socket.gethostname())
```
�炵���D  
����������Ŏ擾�ł���̂�ethernetIP�݂����D

### turtlebotPC��iphone�����΂��܂�
#####turtlebot��(server)
```
# baffalo-G-BB64�ɂȂ��܂��傤
cd masa/turtle_zooming/oscTest
pythonbrew use 3.3.1 #3.3.2��������Ȃ��悤�Ȃ̂�.
python server.py --ip 192.168.11.xx --port 12345
```

##### iphone��(client)  
**wifi:Baffalo-G-BB64�ɂȂ��I**  
�܂�XCode��
```
_host = @"192.168.11.xx" //��Ƒ�����
_port = @"12345"
```
��{�I�ɂ��̏�ԂłȂ���͂��D�D�Ȃ̂����D�D

* konashi���������Ȃ��I  
iPhone��konashi���Ȃ����ĂȂ��Dbluetooth����̃G���[�̂悤�D
�Ή����s���D�ꉞ�{�̓d���؂��Ă���ʂ񂷂�Ǝ������莡��Ȃ�������D

* ubuntu�ɒl�����łȂ��I  
wifi�m�F�DBaffalo-g-bb64�ɂȂ����Ă��邩�Hip�͐��������H
