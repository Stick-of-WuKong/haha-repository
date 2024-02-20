'''
Author: your name
Date: 2024-01-04 09:56:12
LastEditTime: 2024-02-04 21:16:17
LastEditors: haihangyu-sz
Description: In User Settings Edit
FilePath: \VSCodeProjects\PythonFile\read_link_download.py
'''
import os
from time import sleep
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from urllib.parse import urljoin
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def download_links(url, download_folder, parent_file=None):
    print(f"url : {url}")
    print(f"download_folder : {download_folder}")
    proxies = {
        "https":"socks5://127.0.0.1:7890"
    }
    # 禁用不安全的请求警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # 添加请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    # 创建一个会话
    session = requests.Session()

    # 网站需要添加身份验证信息则加入此项
    session.auth = ("name", "passwd")
    # 发送请求获取页面内容
    response = session.get(url,proxies=proxies, headers=headers)
    if response.status_code != 200:
        print(f"Notion !!!!  Failed to retrieve the page. Status code: {response.status_code}")
        return

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取页面中的链接
    links = soup.find_all('a', href=True)

    # 创建下载目录
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Success makedirs {download_folder}")
        print(f"file will download to : {download_folder}")

    # 如果需要父级文件，则创建
    if parent_file:
        with open(os.path.join(download_folder, parent_file), 'w') as f:
            pass
        print(f"Success makedirs {os.path.join(download_folder, parent_file)}")
        print(f"file will download to : {os.path.join(download_folder, parent_file)}")

    # 下载链接
    for link in links:
        href = link['href']
        print(f"href : {href}")
        absolute_url = urljoin(url, href)
        print(f"absolute_url: {absolute_url}")
        
        # 检查链接文本是否为 "Parent Directory"，如果是则跳过
        if "Parent Directory" in link.get_text():
            print(f"JUMP :{link.get_text()}")
            continue

        # 区分目录和文件
        if absolute_url.endswith('/') :
            # 如果链接以 / 结尾，认为是目录，递归下载目录内容 #os.path.basename返回给定URL的最后一部分
            subdir = href[:-1]
            #subdir = os.path.basename(absolute_url)
            print(f"subdir: {subdir}")
            print(f"dir to download: {os.path.join(download_folder, subdir)}")  
            download_links(absolute_url, os.path.join(download_folder, subdir))

        elif '.' in os.path.basename(absolute_url):
            # 如果链接包含 .认为是文件，下载文件内容
            try:
                #因为requests的网络流是没有关联的  没发一次请求都需要重新设置参数  可以用session来保持会话
                response = session.get(absolute_url,proxies=proxies, headers=headers)
                if response.status_code == 200:
                    # 提取文件名
                    filename = os.path.join(download_folder, unquote(os.path.basename(absolute_url)))
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"Success Downloaded: {unquote(os.path.basename(absolute_url))} to {download_folder}")
                else:
                    print(f"Failed to download: {absolute_url}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error downloading {absolute_url}: {str(e)}")

if __name__ == "__main__":
    page_url = "https://xxx"  # 替换为你要下载链接的页面 URL
    output_folder = "D:\\"  # 替换为你的下载目录
    download_links(page_url, output_folder)