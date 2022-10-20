'''
Author: yhh
Date: 2022-10-19 09:56:45
LastEditTime: 2022-10-19 09:56:51
LastEditors: yhh
Description: 
FilePath: \PythonFile\week7.py
yhh
'''
import pexpect
import json

PROMPT = ['# ', '>>> ', '> ', '\$', 'root']


def send_command(process, cmd):
    process.sendline(cmd)
    process.expect(PROMPT)
    print(process.before)


def connect(server, ip):
    sshCommand = 'ssh %s@%s' % (server['username'], ip)
    process = pexpect.spawn(sshCommand, timeout=30)
    print(f'命令: {sshCommand}')

    expect_list = [
        'yes/no',
        'password:',
        pexpect.EOF,
        pexpect.TIMEOUT,
    ]
    index = process.expect(expect_list)
    print(f'匹配到: {index} => {expect_list[index]}')
    if index == 0:
        process.sendline("yes")
        expect_list = [
            'password:',
            pexpect.EOF,
            pexpect.TIMEOUT,
        ]
        index = process.expect(expect_list)
        print(f'匹配到: {index} => {expect_list[index]}')
        if index == 0:
            process.sendline(server['password'])
        else:
            print('EOF or TIMEOUT')
    elif index == 1:
        process.sendline(server['password'])
    else:
        print('EOF or TIMEOUT')
    process.expect(PROMPT)
    return process

def rsync(process):
    print('开始rsync文件同步')
    rsyncCommand = 'rsync -au --progress /home/sqwang/synchronization/ %s@%s:/home/sqwang/synchronization/ > log.txt' \
                   % (server['username'], server['remoteIP'])
    process.sendline(rsyncCommand)
    expect_list = [
        'yes/no',
        'password:',
        pexpect.EOF,
        pexpect.TIMEOUT,
    ]
    index = process.expect(expect_list)
    print(f'匹配到: {index} => {expect_list[index]}')
    if index == 0:
        process.sendline("yes")
        expect_list = [
            'password:',
            pexpect.EOF,
            pexpect.TIMEOUT,
        ]
        index = process.expect(expect_list)
        print(f'匹配到: {index} => {expect_list[index]}')
        if index == 0:
            process.sendline(server['password'])
        else:
            print('EOF or TIMEOUT')
    elif index == 1:
        process.sendline(server['password'])
    else:
        print('EOF or TIMEOUT')
    process.expect(PROMPT)
    print('已将文件保存至log.txt中')
    return process


if __name__ == '__main__':
    with open('week7.json', 'r') as f:
        server = json.loads(f.read())
    processPC = connect(server, server['localIP'])
    print('已和主机{}建立ssh连接'.format(server['localIP']))
    processPC = rsync(processPC)
    print('完成rsync文件传输')
    send_command(processPC, 'cat log.txt')
