from socket import socket, AF_INET, SOCK_STREAM
from base64 import b64encode
from json import dumps
from threading import Thread

def main():

    #自定义线程类
    class FileTransferThread(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'nft1.jpg'
            #JSON是纯文本不能携带二进制数据
            #所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            #通过dump函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    #1.创建套接字对象并指定用哪种传输服务
    server = socket()
    server.bind(('192.168.0.91',5566))
    server.listen(512)
    print('服务器启动开始监听...')
    with open('nft.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        print(f'地址为{addr}的用户已连接')
        #启动一个线程来处理客户请求
        FileTransferThread(client).start()
if __name__ == '__main__':
    main()

