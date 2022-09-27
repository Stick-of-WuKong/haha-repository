'''
Author: yhh
Date: 2022-09-26 17:51:11
LastEditTime: 2022-09-26 17:52:37
LastEditors: yhh
Description: 
FilePath: \PythonFile\week6\checkport.py
yhh
'''
 
import sys, socket
from argparse import ArgumentParser
from optparse import OptionParser
 
class backupTools:
    def check_port(self, ip, port=80):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            s.shutdown(2)
            print('%s:%d is used' % (ip, port))
            return True
        except socket.error as e:
            print('%s:%d is unused' % (ip, port))
            return False
 
 
if __name__ == '__main__':
    args = sys.argv
    port = sys.argv[1]
    backup = backupTools()
     
    # parser=OptionParser()
    # parser.add_option('-a', '--addr', dest='addr', help='')
    # parser.add_option('-p', '--port', dest='port', default=80, type="int", help='')
    # (options, args) = parser.parse_args()
    # print "options===>", options.addr, args 
 
    parser = ArgumentParser(description="TCP端口检测")
    parser.add_argument('a1')                            #  输入参数时候不用字典传参。
    parser.add_argument('-o', '--other', dest='other')   #  输入参数时候需要字典传参，python test.py 33 -o56 127.0.0.1 3306
    parser.add_argument('-a', '--addr', dest='addr', default='localhost', help='address for the server')
    parser.add_argument('-p', '--port', dest="port", default=80, type=int, choices=[80,443,3306], help='port for the server')
    # args = parser.parse_args()
    args = parser.parse_known_args()[0]
    print ("args===>", args, args.port)
     
    result= backup.check_port(args.addr, int(args.port))
    sys.exit(0)