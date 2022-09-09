# 将从网页复制的请求头转换为 json 样式的文本

import os


def generate_header(source_file_path:str, target_file_path: str) -> None:
    """
    将从网页复制的请求头转换为 json 样式的文本  
    :param source_file_path: 源文件路径  
    :param target_file_path: 目标文件路径  
    :return: None  
    """
    # 如果 target_file_path 已存在则删除该文件
    if os.path.exists(target_file_path):
        os.remove(target_file_path)
    with open(source_file_path, "r") as f:
        lines = f.readlines()
        length = len(lines)
        for i in range(length):
            line = lines[i].strip()
            split_line = line.split(":")
            new_line = f'"{split_line[0]}": "{":".join(split_line[1:]).strip()}",\n'
            # 去掉最后一行的逗号
            if i == length - 1:
                new_line = new_line[:-2]
            print(new_line)
            with open(target_file_path, "a") as f2:
                f2.write(new_line)


if __name__ == '__main__':
    source_file = os.path.join(os.path.dirname(__file__), "source.txt")
    target_file = os.path.join(os.path.dirname(__file__), "target.txt")
    generate_header(source_file, target_file)