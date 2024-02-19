'''
Author: your name
Date: 2024-02-04 21:58:33
LastEditTime: 2024-02-04 22:06:08
LastEditors: haihangyu-sz
Description: In User Settings Edit
FilePath: \Crawler\he.py
'''
import os
import re

# 获取当前脚本所在目录
script_directory = os.path.dirname(os.path.realpath(__file__))
chapter_files_directory = os.path.join(script_directory, "chapter_files")
output_file_path = os.path.join(script_directory, "A股教父.txt")

# 定义提取数字的正则表达式
number_pattern = re.compile(r'第(\d+)章')

# 遍历 chapter_files 文件夹下的所有 .txt 文件，并提取数字
file_list = []
for filename in os.listdir(chapter_files_directory):
    if filename.endswith(".txt"):
        match = number_pattern.search(filename)
        if match:
            # 将匹配到的数字转换为整数，同时保存文件名和路径
            file_list.append((int(match.group(1)), os.path.join(chapter_files_directory, filename)))
# 按照提取到的数字排序文件列表
file_list.sort(key=lambda x: x[0])

# 将排序后的文件内容写入新的文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for _, file_path in file_list:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            content = input_file.read()
            output_file.write(f"File: {os.path.basename(file_path)}\n\n{content}\n\n{'='*30}\n")
    print("合并完成")