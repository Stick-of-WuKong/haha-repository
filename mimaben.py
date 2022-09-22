# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 10:21
# @Author  : yhh
# @File    : mimaben.py
# @Software: PyCharm
charsw='qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+|~}{><?,.;[]'#先创建密码本，把所有的按键敲了一遍
import itertools
l=1#密码的初始长度为1
path = input('请输入文件全名')
while l <= 6: #被破解的密码最终长度，先使用迭代创建一个密码本
  for passwords in itertools.product(charsw, repeat=l):
    passwords= ''.join(passwords)
    print(passwords) #可以使用pass直接跳过
    f = open(path, 'a+')
    password = str(passwords)+ '\n'
    f.write(password)
    f.close()
  l += 1