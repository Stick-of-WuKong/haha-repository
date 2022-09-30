'''
Author: yhh
Date: 2022-09-26 17:51:20
LastEditTime: 2022-09-27 14:17:38
LastEditors: yhh
Description: 
FilePath: \PythonFile\week6\server.py
yhh
'''
from http import server
import threading
import socket
import os
from time import sleep

class Server():
    def __init__(self,address,port) -> None:
        self.address = address
        self.port = port
        # self.socket_list = []
        self.addr_list = []
        self.connect()

    def connect(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建socket
            s.bind((self.address, self.port)) # 绑定监听ip和port
        except Exception as e:
            print(e,"Bind Error!")
            s.close()
            return
        try:
            num = int(input('Input the max number of sockets for the client:'))
            if(num<=0):
                print("Numeric Error!Set the default number to be 10!")
                num = 10
        except Exception as e:
            print('Type error!Set the default number to be 10!')
            num = 10
        s.listen(num)  # 监听，num为最大连接数量
        while True:
            self.show_addr_list()
            print('Listening ...')
            sock, addr = s.accept()  # 接受连接，获取sock和连接方的ip  对于接受到的socket建立线程来处理
            print(f'Connect {addr}!')
            # self.socket_list.append(sock)
            self.addr_list.append(addr[0]+":"+str(addr[1]))
            address = addr[0]+":"+str(addr[1])
            t1 = threading.Thread(target=Dataflow, args=(sock, address,self.addr_list),name=address)
            t1.setDaemon(True)
            t1.start()

    def show_addr_list(self):
        i = 1
        if len(self.addr_list)==0:
            print("there is no client")
        else:
            print("Current clients ip are :")
            for item in self.addr_list:
                print(f"{i}th is {item} ")
                i += 1


class Dataflow():

    # def __init__(self,sock,addr,sock_list,addr_list):
    def __init__(self,sock,addr,addr_list):

        self.path = os.getcwd()
        self.sock = sock
        self.addr = addr
        # self.sock_list = sock_list
        self.addr_list = addr_list
        self.start_trans()

    def show_addr_list(self):
        i = 1
        if(len(self.addr_list)==0):
            print("there is no client!")
            return
        print("Current clients ip are :")
        for item in self.addr_list:
            print(f"{i}th is {item} ")
            i += 1
    def start_trans(self):
        try:
            while True:
                actiondict = {"ls":self.ls,"get":self.get,"put":self.put,"exit":self.exit}
                content = self.sock.recv(1024).decode("gbk")
                print(content)
                if content=="ls" or content=="exit":
                    if content=="exit":
                        actiondict[content]()
                        return
                    actiondict[content]()
                elif len(content.split()) == 2:
                    if content.split()[0] == "get" :
                        action,file = content.split()[0],content.split()[1]
                        actiondict[action](file)
                    elif content.split()[0]=="put":
                        action,file = content.split()[0],content.split()[1]
                        actiondict[action](file)
                    else:
                        print(f"{self.addr} Input Error!")
                        if(input("you can input q to exit other key to continue:") == 'q'):
                            self.exit()
                            break

                else:
                    print(f"{self.addr} Input Error!")
                    if(input("you can input q to exit other key to continue:") == 'q'):
                        self.exit()
                        break
        except Exception as e:
            print(e)
            self.exit()

        

    def ls(self):
        list_tmp = []
        list_tmp = os.listdir(self.path)
        str1 = ','.join(list_tmp)
        self.sock.send(str1.encode())
        print(f"{self.addr} ls success!")


    def exit(self):
        # i = 0
        # for item in self.addr_list:
        #     if(self.addr==item):
        #         break
        #     else:
        #         i+=1
        if(len(self.addr_list)==0):
            return
        print(f"remove {self.addr}")
        self.addr_list.remove(self.addr)
        # self.sock_list.remove(self.sock_list[i])
        self.sock.send("exit".encode())
        print(f"{self.addr} exit success!")
        self.show_addr_list()

    def get(self,file_name):
        print(f"{self.addr} start ...")
        try:
            with open(file_name,"rb") as f:
                content = f.read()
            self.sock.send(content)
            print(f"{self.addr} get {file_name} success!")
        except Exception as e:
            print(e,f"{self.addr}  get {file_name} Error!")
            content = '0'
            self.sock.send(content.encode())
    def put(self,file):

        print(f"{self.addr}  start put {file}")
        content = self.sock.recv(1024)
        try:
            lock = threading.Lock()
            print("waiting to get the lock...")
            # 先要获取锁:
            lock.acquire()
            # 在这操作共享变量 
            print("get the lock")
            with open(file,'wb') as f:
                f.write(content)
            print(f"{self.addr} put {file} success!")
        except Exception as e:
            print(e)
            print(e,f"{self.addr} put {file} Error!")
        lock.release()
        print("release the lock")


def server_start():
    while True:
        try:
            host = input("Please input the Host to listen:")
            port_in = input("Please input the Port to listen:")
            try:
                port = int(port_in.strip())
                server = Server(host.strip(),port)
            except Exception as e1:
                print(e1,"Port Error! Try again!")
        except Exception as e2:
            print(e2,"Host or Port Type Error! Exit!")
        

server_start()