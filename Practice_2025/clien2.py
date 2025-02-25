from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('192.168.0.91',5566))
    #定义一个二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open(f'D:/study/coding/Github Repos/Python-learning/Practice_2025/{filename}', 'wb') as f:
        f.write(b64decode(filedata))
    print('图片已保存')

if __name__ == '__main__':
    main()

