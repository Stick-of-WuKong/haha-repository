import requests

reqUrl = "http://192.168.1.221/dvwa_test/vulnerabilities/sqli/?id=&Submit=Submit"

headersList = {
 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
 "accept-encoding": "gzip, deflate",
 "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
 "connection": "close",
 "cookie": "experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltRmpOMlZpWVdFNExUTTVNRFl0TkRnd05DMDRNRFl6TFRnMFlXSTRaRGhoTURFMVlpST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--fa61bc8250f428fab74992fe3b6e868f5908d932; sidebar_collapsed=false; PHPSESSID=jvrhoa1qgsfqf7eftcf0864d63; security=low",
 "host": "192.168.1.221",
 "referer": "http://192.168.1.221/dvwa_test/vulnerabilities/sqli/",
 "upgrade-insecure-requests": "1",
 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)