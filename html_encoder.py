"""
作者：马朴涵
时间：2022.10.20
简介：输入字符串，显示其所有可用的html实体编码，每一行表示一种对应编码
"""

# 通过给定char获得一个所有html编码的列表
def getHtmlCharList(theChar):
    chrInteger = ord(theChar)
    flag = "&#"
    res = []
    zero = ""
    for i in range(0, 6):
        string = zero + str(chrInteger)
        res.append(flag + string)
        res.append(flag + string + ";")
        if len(string) < 7:
            zero += "0"
    zero = ""
    for i in range(0, 6):
        hexStr = zero + "%x" % chrInteger
        res.append(flag + "x" + hexStr)
        res.append(flag + "X" + hexStr)
        res.append(flag + "x" + hexStr.upper())
        res.append(flag + "X" + hexStr.upper())
        res.append(flag + "x" + hexStr + ";")
        res.append(flag + "X" + hexStr + ";")
        res.append(flag + "x" + hexStr.upper() + ";")
        res.append(flag + "X" + hexStr.upper() + ";")
        if len(hexStr) < 7:
            zero += "0"
    return res

# 通过给定字符串获得所有html编码的列表
def strToHtmlCode(string):
    table = []
    res = []
    for s in string:
        table.append(getHtmlCharList(s))
    for j in range(0, len(table[0])):
        t = ""
        for i in range(0, len(string)):
            t += table[i][j]
        res.append(t)
        print(t)
    return res


if __name__ == '__main__':
    while True:
        print(strToHtmlCode(input()))



# <
# %3c
# &lt
# &lt;
# &LT
# &LT;
# &#60
# &#060
# &#0060
# &#00060
# &#000060
# &#0000060
# &#60;
# &#060;
# &#0060;
# &#00060;
# &#000060;
# &#0000060;
# &#x3c
# &#x03c
# &#x003c
# &#x0003c
# &#x00003c
# &#x000003c
# &#x3c;
# &#x03c;
# &#x003c;
# &#x0003c;
# &#x00003c;
# &#x000003c;
# &#X3c
# &#X03c
# &#X003c
# &#X0003c
# &#X00003c
# &#X000003c
# &#X3c;
# &#X03c;
# &#X003c;
# &#X0003c;
# &#X00003c;
# &#X000003c;
# &#x3C
# &#x03C
# &#x003C
# &#x0003C
# &#x00003C
# &#x000003C
# &#x3C;
# &#x03C;
# &#x003C;
# &#x0003C;
# &#x00003C;
# &#x000003C;
# &#X3C
# &#X03C
# &#X003C
# &#X0003C
# &#X00003C
# &#X000003C
# &#X3C;
# &#X03C;
# &#X003C;
# &#X0003C;
# &#X00003C;
# &#X000003C;
# \x3c
# \x3C
# \u003c
# \u003C
