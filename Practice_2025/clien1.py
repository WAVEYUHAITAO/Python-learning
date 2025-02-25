from socket import socket


def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    try:
        client = socket()
        client.connect(('192.168.0.91', 6789))
        print(client.recv(1024).decode('utf-8'))
    except ConnectionRefusedError:
        print('目标服务器不存在')


if __name__ == '__main__':
    main()
