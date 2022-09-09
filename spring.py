'''
Author: yhh
Date: 2022-09-06 21:03:05
LastEditTime: 2022-09-09 10:55:41
LastEditors: yhh
Description: 
FilePath: \PythonFile\spring.py
yhh
'''
import json
import requests
import os

def post_spring( url, data, file_path):
    try:
        with open('output.txt','r') as f:
            s ='{'
            for i in f.readlines():
                s +=i
            s += '}'
            headers = json.loads(s)
            #print(headers)
    except Exception as e:
        print(e)      
    file_path = os.path.join(os.path.dirname(__file__), file_path)

    try:
        r = requests.post(url,headers=headers,data=data)
        # 将返回的数据写入文件(覆盖)

        with open(file_path, "w") as f:
           f.write(r.text)
        print(r.txt)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    url = input('Type the url:')
    body = input("Type the body:")
    post_spring(url, body, 'response.json')
   