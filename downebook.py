'''
Author: your name
Date: 2024-02-04 21:16:29
LastEditTime: 2024-02-04 21:58:08
LastEditors: haihangyu-sz
Description: In User Settings Edit
FilePath: \Crawler\downebook.py
'''
import requests
from bs4 import BeautifulSoup
import os
import string
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 设置起始和结束页码
start_page = 254586905
end_page = 254586953

# 设置保存文件夹和合并后的文件名
output_folder = "chapter_files"
merged_file = "A股教父.txt"

# 创建保存文件夹
os.makedirs(output_folder, exist_ok=True)

# 禁用不安全的请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    "Connection": "close"}



def sanitize_filename(filename):
    # 去除非法字符，只保留字母、数字、中文、空格和括号
    valid_chars = '-_.() %s%s' % (string.ascii_letters, string.digits)  # 添加需要保留的字符
    sanitized_filename = ''.join(c for c in filename if c in valid_chars)
    return sanitized_filename

# 循环爬取页面内容并保存到文件
for page_number in range(start_page, end_page + 1):
    url = f"https://www.84kanshu.com/book/94936579/{page_number}.html"
    #response = requests.get(url,headers=headers,verify=False)
    response = requests.get(url, headers=headers, timeout=5, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到 <h1> 标签并提取内容
        title_tag = soup.find('h1', class_='title')
        if title_tag:
            title_content = title_tag.get_text(strip=True)
            # 以标题内容作为文件名
            file_name = f"{title_content}.txt"
            print(file_name.rsplit('（', 1)[0]+'.txt')
            file_path = os.path.join(output_folder, file_name.rsplit('（', 1)[0]+'.txt')
            
            # 找到所有 <p> 标签并提取内容
            paragraphs = soup.find_all('p')
            with open(file_path, 'w',encoding='utf-8') as file:
                for paragraph in paragraphs:
                    content = paragraph.get_text(strip=True)
                    # 将每个段落的内容写入文件
                    file.write(content + '\n\n')
                
                print(f"Page {page_number} saved as {file_name.rsplit('（', 1)[0]+'.txt'}.")
        else:
            print(f"Failed to find title for page {page_number}.")
    else:
        print(f"Failed to retrieve page {page_number}.")

# 获取当前脚本所在目录
script_directory = os.path.dirname(os.path.realpath(__file__))
chapter_files_directory = os.path.join(script_directory, "chapter_files")
output_file_path = os.path.join(script_directory, "A股教父.txt")

# 遍历 chapter_files 文件夹下的所有 .txt 文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for filename in os.listdir(chapter_files_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(chapter_files_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as input_file:
                content = input_file.read()
                # 将文件名和文件内容写入新的文件 "A股教父.txt"
                output_file.write(f"File: {filename}\n\n{content}\n\n{'='*30}\n")
    print("合并完成")

print("Script completed.")