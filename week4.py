'''
Author: yhh
Date: 2022-09-16 15:38:55
LastEditTime: 2022-09-16 20:43:06
LastEditors: yhh
Description:   ebook
FilePath: \PythonFile\ebook\week4.py
yhh
'''
from asyncio.windows_events import NULL
import os
import sys
from time import sleep
import toml
import chardet
class Ebook():
    """电子书类"""
    def __init__(self,name,path,encoding='utf-8',progress=0):
        """
        name: 电子书名称
        path: 电子书绝对路径
        encoding: 电子书编码格式  默认为utf-8
        progress: 电子书阅读进度----文件指针位置  默认为文件首0
        """
        self.name = name
        self.path = path
        self.encoding = encoding
        self.progress = progress
        self.line_num = 10

    def display(self,progress,line_num):     
        with open(self.path,'r',encoding=self.encoding) as f:
            f.seek(progress)
            for i in range(line_num):
                line = f.readline()
                if line==NULL:
                    print('End of Book! Thanks for your Reading, You can chose another book to read!')
                    break
                else:
                    print(line)   
            self.progress =  f.tell()

    def __str__(self):
        """返回电子书信息"""
        return f'The name of ebook:{self.name},The reading progress: {self.progress}'
    
class BookShelf():
    """书架类"""
    def __init__(self,ebooks_dir='ebooks',config_dir='ebook.toml'):
        """初始化书架
        ebooks_dir: 电子书目录(默认为当前脚本目录下的 books 目录)  
        config_dir: 配置文件目录(默认为当前脚本目录下的 ebook.toml 文件)
        """
        self.ebook_dict = dict()#内存中存放电子书info的字典
        self.ebooks_dir = os.path.join(os.path.dirname(__file__),ebooks_dir)
        self.config_dir = os.path.join(os.path.dirname(__file__),config_dir)
    
    def add_ebook(self,ebook:Ebook):
        self.ebook_dict[ebook.name] = ebook

    def load_bookshelf(self):
        """
        toml 一级键为图书名称, 二级键为图书信息(reading, encoding, path)
        从配置文件读取到book_dict中
        """
        
        config = toml.load(self.config_dir)
        for ebook_name,ebook_info in config.items():
            ebook = Ebook(ebook_name,ebook_info['Path'],ebook_info['Encoding'],ebook_info['Progress'])
            self.add_ebook(ebook)

    def update_bookshelf(self):
        """
        # 遍历 ebooks_dir 目录下的文件和文件夹  如果不在ebook_dict中则加入
        # 函数执行应该先update  后load
        """
        ebook_list = os.listdir(self.ebooks_dir)
        
        for file in ebook_list:
            if file.endswith('.txt'):
                if file[:-4] not in self.ebook_dict:
                    ebook_path = os.path.join(self.ebooks_dir,file)
                    encoding = chardet.detect(open(ebook_path, 'rb').read(4096))['encoding']
                    ebook = Ebook(file[:-4],ebook_path,encoding)
                    self.add_ebook(ebook)       

    def save_bookshelf(self):
        """
        #把ebook_dict信息保存到配置文件中
        """
        with open(self.config_dir,'w',encoding='utf-8') as f:
            for ebook_name,ebook in self.ebook_dict.items():
                toml.dump({ebook_name:{'Path':ebook.path,'Encoding':ebook.encoding,'Progress':ebook.progress}},f)

    def __str__(self):
        """
        #书架信息
        """
        return f'There is {len(self.ebook_dict)} ebooks'

    def display_ebook(self,ebook_name):
        ebook = self.ebook_dict[ebook_name]
        ebook.display(ebook.progress,ebook.line_num)
        while True:
            inchar = input("Input enter to continue,q to exit:")
            if inchar == '':
                ebook.display(ebook.progress,ebook.line_num)
            elif inchar == 'q':
                return


    def loop(self):
        """
        #主函数
        """
        #self.update_bookshelf()
        self.load_bookshelf()
        while True:
            print('Read Ebooks:1')
            print('Add Ebook:2')
            print('Input q to Exit')
            num_input = input('Please input the num:')
            if num_input == '1':
                while len(self.ebook_dict)==0:
                    self.update_bookshelf()
                    print("There is no ebooks in %s" % self.ebooks_dir)
                    print('Please add ebooks to %s' % self.ebooks_dir)
                    sleep(10)
                print('There are some ebooks :')
                for ebook,ebookinfo in self.ebook_dict.items():
                    print(ebook)
                    #print(ebookinfo)
                # for ebook in self.ebook_dict:
                #     print(ebook)  错误---dont understand
                ebook_name = input("Input the name of the ebook--no suffix:")
                if ebook_name not in self.ebook_dict:
                    print("Not Exist!")
                else:
                    self.display_ebook(ebook_name)
            elif num_input == '2':
                try:
                    ebook_path = input("Input the ebook's abspath:")
                    ebook_name = ebook_path.split('/')[-1][:-4]
                    ebook_encoding = chardet.detect(open(ebook_path, 'rb').read(4096))['encoding']
                    ebook = Ebook(ebook_name, ebook_path, ebook_encoding)
                    self.add_ebook(ebook)
                    self.update_bookshelf()
                except Exception as e:
                    print(e)
            elif num_input == 'q':
                self.save_bookshelf()
                break
            else:
                print('Please input the  right num!')
            
if __name__=='__main__':
    config_bookshelf_path = os.path.join(os.path.dirname(__file__), 'config.toml')
    config_bookshelf = toml.load(config_bookshelf_path)
    bookshelf = BookShelf(config_bookshelf['ebook_dir'], config_bookshelf['ebook_config_dir'])
    bookshelf.loop()
