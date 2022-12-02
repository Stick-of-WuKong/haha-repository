import random
"""
作者：马朴涵
时间：2022.10.17
简介：可以用来混淆字符串，选择不同的编程语言后，输入要混淆的字符串，返回混淆后的字符串，通过异或混淆。
"""
def javaXorEncoder():
    xorList = "!@_+-123abc"
    inputStr = input("input String")
    inputStrLen = len(inputStr)
    for i in range(0, inputStrLen):
        t = random.sample(xorList, 1)[0]
        if i == 0:
            print("\"\"", end="")
        print("+(char)('%s'^%d)" % (t, ord(inputStr[i]) ^ ord(t)), end="")
    return

def phpXorEncoder():
    xorList = "!@_+-123abc"
    inputStr = input("input String")
    inputStrLen = len(inputStr)
    for i in range(0, inputStrLen):
        t = random.sample(xorList, 1)[0]
        print("(chr("+str(ord(inputStr[i]) ^ ord(t)),end="")
        print(")^'"+t+"')",end="")
        if i!=inputStrLen-1:
            print(".",end="")
    return

if __name__ == '__main__':
    while True:
        description = """
Select a language
1.java
2.php
"""
        flag = input(description)
        if flag=="1":
            javaXorEncoder()
        elif flag == "2":
            phpXorEncoder()
        else:
            continue