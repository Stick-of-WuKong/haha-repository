'''
Author: yhh
Date: 2022-09-09 09:07:46
LastEditTime: 2022-09-09 10:31:15
LastEditors: yhh
Description: 
FilePath: \PythonFile\auto_post.py
yhh
'''
#输入文件为source.txt  输入后进行分割：并且加:处理   输出为output.txt
import os
import requests

def input(file_path:str)->list:
    try:
        with open(file_path,"r") as f:
            newlist = []
            for line in f.readlines():#读取成列表
                strlist = line.split(":",1)#对列表的每一个元素处理即输入的每一行处理
                if(len(strlist)==2):
                    newstr = "\""+strlist[0]+"\":\""+strlist[1].strip("\n")+'\",\n'
                newlist.append(newstr)
        l = len(newlist)
        newlist[l-1] = newlist[l-1][0:-2]
        print(newlist[-1])
        
        return newlist
    except Exception as e:
        print(e)
#输出文件为output.txt
def output(file_path:str,newlist):
    try:
        with open(file_path,"w") as f:
            f.write("".join(newlist))
    except Exception as e:
        print(e)



if __name__ == '__main__':
    source_file = os.path.join(os.path.dirname(__file__), "source.txt")
    target_file = os.path.join(os.path.dirname(__file__), "output.txt")
    newlist = []
    newlist = input(source_file)
    output(target_file,newlist)