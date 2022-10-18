import socket

if __name__ == '__main__':

    host = '10.182.235.133'
    port = 9222
    num = 5
    something = b'214214'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
    s.connect((host, port))
    s.send(something)  # 向server发送something
    content = s.recv(num)  # 从server接收num个字节
    print(content.decode('utf-8'))
    s.close()  # 关闭连接
