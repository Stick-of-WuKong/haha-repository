'''
Author: yhh
Date: 2022-09-05 22:44:23
LastEditTime: 2022-09-05 22:44:26
LastEditors: yhh
Description: 
FilePath: \PythonFile\ping.py
yhh
'''
# 读取 source.txt 每一行的地址, 每个 ping 4次, 按照响应时间递增排序, 输出到 result.txt
import os
import re
import time


def ping_windows(host: str, count: int = 4) -> float:
    output = os.popen(f'ping {host} -n {count}').read()
    time_list = re.findall(r'平均 = (\d+)ms', output)
    if time_list:
        return sum(map(int, time_list)) / len(time_list)
    else:
        return 999999      

def ping_linux(host: str, count: int = 4) -> float:
    output = os.popen(f'ping {host} -c {count}').read()
    # print(output)
    #rtt min/avg/max/mdev = 44.661/44.987/45.242/0.242 ms
    try:
        min, avg, max, mdev = re.findall(r'rtt min/avg/max/mdev = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+) ms', output)[0]
    # 全丢包的情况下就找不到了, 此时返回一个很大的数
    except IndexError:
        return 999999
    # print(avg)
    # print("=======================================")
    return float(avg)


https_lst = []
http_lst = []



def get_hosts(file_path: str) -> list:
    global https_lst
    global http_lst
    with open(file_path, 'r') as f:
        hosts = f.read().splitlines()
        if os.name == 'posix':
            print("检测到系统为Linux, 开始执行协议头去除操作")
            for i in range (len(hosts)):
                if hosts[i].startswith('https://'):
                    hosts[i] = hosts[i][8:]
                    https_lst.append(hosts[i])
                elif hosts[i].startswith('http://'):
                    hosts[i] = hosts[i][7:]
                    http_lst.append(hosts[i])
                else:
                    print("Error: Unknown host type")
                    continue
            print("协议头去除操作完成")
        return hosts


def sort_write_hosts(hosts: list) -> list:
    # 递增排序
    if os.name == 'nt':
        result = sorted(hosts, key=lambda x: ping_windows(x))
    if os.name == 'posix':
        result = sorted(hosts, key=lambda x: ping_linux(x))
        print("检测到系统为Linux, 开始执行协议头添加操作")
        # 根据 http_lst 和 https_lst 将去除协议头的 host 重新加上协议头
        for i in range(len(result)):
            if result[i] in https_lst:
                result[i] = 'https://' + result[i]
            elif result[i] in http_lst:
                result[i] = 'http://' + result[i]
            else:
                print("Error: Unknown host type")
                continue

    with open('result.txt', 'w') as f:
        f.write('\n'.join(result))

def ping(source_path: str) -> None:
    hosts = get_hosts(source_path)
    sort_write_hosts(hosts)

if __name__ == '__main__':
    source_path = os.path.join(os.path.dirname(__file__), 'source.txt')
    ping(source_path)