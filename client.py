'''
Author: yhh
Date: 2022-09-26 18:33:16
LastEditTime: 2022-09-27 17:28:27
LastEditors: yhh
Description: 
FilePath: \PythonFile\week6\client.py
yhh
'''
from http import client
import threading
import socket
import os
import time
class Client():
    def __init__(self,address,port):
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.sock.connect((address,port))
            self.start()
        except Exception as e:
            print(e,f"{address}:{port} Error!")
            self.sock.close()
        

    def start(self):
        while True:
            actiondict = {"ls":self.ls,"get":self.get,"put":self.put,"exit":self.exit}
            print("The default data size server can receive is 1024bits!")
            print("The supported actions are: ls, get {file},put {file},exit --Don't ignore case")
            content=input()
            if content=="ls" or content=="exit":
                if content=="exit":
                    actiondict[content]()
                    return
                actiondict[content]()
            elif len(content.strip().split()) == 2:
                if content.split()[0] == "get" :
                    action,file = content.split()[0],content.split()[1]
                    actiondict[action](file)
                elif content.strip().split()[0]=="put":
                    action,file = content.split()[0],content.split()[1]
                    actiondict[action](file)
                else:
                    print(f"{self.address} Input Error!")
            else:
                    print(f"{self.address} Input Error!")
            
    def ls(self):
        self.sock.send("ls".encode("gbk"))
        content = self.sock.recv(1024)
        dir_list = content.decode().split(',')
        for item in dir_list:
            print(item)


    def exit(self):
        self.sock.send("exit".encode("gbk"))
        content = self.sock.recv(1024)
        if (content.decode()=="exit"):
            self.sock.close()
            print(f"server has closed the socket ")
            

    def get(self,file_name):
        self.sock.send(f"get {file_name}".encode("gbk"))
        print(f"start downloading {file_name}...")
        file_name = "client_"+file_name
        try:
            time_start = time.time()
            content = self.sock.recv(1024)
            time_end = time.time()
            sum = time_end - time_start
            if(content.decode() == '0'):
                # print(content)
                print("transfer error or file!")
                return
            else:
                with open(file_name,"wb") as f:
                    content = f.write(content)
                print(f"download {file_name} success!")
            file_len = float((content/1024)/8)
            if(sum == 0):
                print(f"{file_name} is too small,Unable to calculate speed")
                print(f"File's length is :{file_len} KB")
            else:
                speed = float(((content/1024)/8)/sum)
                print(f"File's length is :{file_len} KB,speed is :{speed} KB/s")
        except Exception as e:
            print(f"download {file_name} Error!")
            

    def put(self,file):
        self.sock.send(f"put {file}".encode("gbk"))
        print(f'start upload {file}')
        try:
            with open(file,'rb') as f:
                content = f.read()
            self.sock.send(content)
            print(f"upload client_{file} success!")
        except Exception as e:
            print(e,f"upload {file} error!")
def client_start():
    try:
        host = input("Please input the Host to connect:")
        port_in = input("Please input the Port to connect:")
        try:
            port = int(port_in.strip())
            client = Client(host.strip(),port)
        except Exception as e1:
            print(e1,"Port Error! Try again!")
    except Exception as e2:
        print(e2,"Host or Port Type Error! Exit!")
        return
    
client_start()
