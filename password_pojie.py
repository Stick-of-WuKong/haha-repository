# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 10:19
# @Author  : yhh
# @File    : password_pojie.py
# @Software: PyCharm
import rarfile
import zipfile
import py7zr
c = 0
a = 0
print("本软件只支持 7z , zip , rar格式的压缩包")
zd = input("请输入字典位置：")
try:
    ozd = open(zd,"r",encoding="utf8").read().split("\n")
except:
    print("字典读取失败")
print(f"检测到字典里有{len(ozd)}个密码")
file = input("请输入要破解的压缩包位置：")
if file.endswith(".zip"):
    print("检测到是zip压缩包")
    print("正在破解.....")
    zip = zipfile.ZipFile(file)
    for pas in ozd:
        c = c + 1
        pasw = bytes(pas.encode("utf8"))
        try:
            zip.extractall(pwd=pasw)
            print("破解成功，密码是：" + pas)
            a = a + 1
            break
        except:
            pass
    if a == 0:
            print("破解失败")
elif file.endswith(".rar"):
    print("检测到是rar压缩包")
    print("正在破解.....")
    rar = rarfile.RarFile(file)
    for pas in ozd:
        c = c + 1
        pasw = bytes(pas.encode("utf8"))
        try:
            rar.extractall(pwd=pasw)
            print("破解成功，密码是：" + pas)
            a = a + 1
            break
        except:
            pass
    if a == 0:
        print("破解失败")
elif file.endswith(".7z"):
    print("检测到是7z压缩包")
    print("正在破解.....")
    for pas in ozd:
        c = c + 1
        pasw = bytes(pas.encode("utf8"))
        try:
            qz = py7zr.SevenZipFile(file,password = pasw)
            qz.extractall()
            print("破解成功，密码是" + pas)
            a = a + 1
            break
        except:
                pass
    if a == 0:
        print("破解失败")
else:
    print("此文件不是压缩包文件")
print(f"已经尝试了{c}个密码")
input("破解完成，请按任意键继续.....")