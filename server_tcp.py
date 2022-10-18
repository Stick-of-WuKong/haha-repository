import socket

if __name__ == '__main__':
    host = '10.182.235.133'
    port = 9222
    num = 5
    something = b'233233'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
    s.bind((host, port))  # 绑定监听ip和port
    s.listen(num)  # 监听，num为最大连接数量
    sock, addr = s.accept()  # 接受连接，获取sock和连接方的ip
    content = sock.recv(num)
    print(content.decode('utf-8'))
    sock.send(something)
    sock.close()
