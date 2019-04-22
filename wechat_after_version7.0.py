
# coding: utf-8

# In[1]:


import re
import time
import pdfkit
import os 
from queue import Queue
from threading import Thread
import re
source_path = r'D:/1.txt'    #这里是邮件txt位置
save_path = r'D:/wxwz/'  #这里设置pdf保存位置
wkhtmltopdf_path = r'D:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'   #这里设置wkhtmltox程序的路径

maxsize = 1000 #最多一次下载的个数
#pdfkit配置
confg = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)


# In[2]:


#将一些文件名冲突字符替换成空格
def get_filename(title):
    pat = re.compile(r'[\/:*?"<>|]')
    return  (save_path + re.sub(pat,' ',title) +  '.pdf')


# In[3]:


#从邮件发送形成的txt中提取每个链接的标题和地址
def get_info(): 

    with open('D:/1.txt') as f:
        title_list = []
        url_list = []
        l = f.readline()
        mode = re.compile(r'\[(.*?):(http://.*?)\]')
        a = re.finditer(mode,l)
        for each in a:
            try:
                title_list.append(each.group(1))
                url_list.append(each.group(2))
            except:
                pass
        title_list = list(map(get_filename, title_list))
        for each in zip(title_list, url_list):
            file_list.put(each) 


# In[4]:


#多线程类
class consumer(Thread):
    def __init__(self, file_list, *args, **kwargs):
        super(consumer,self).__init__(*args, **kwargs)
        self.file_list = file_list
        
    def run(self):
        while True:
            if self.file_list.empty():
                break
            self.download()
            
    def download(self):
        dirlist = os.listdir(save_path)#目标路径所有文件名
        filename, url = self.file_list.get()
        if (filename[8:] not in dirlist): #如果文件已存在则跳过
            print(filename)
            print(url)

            try:
                pdfkit.from_url(url, filename, configuration=confg,)
                dirlist.append(filename[8:])#将刚下载的此文件名加入列表
                #time.sleep(3)
            except:
                print('【出现错误,请检查文件是否已下载！】')

        else:
            print(filename,'【文件已存在！】')     


# In[ ]:


def main():
    file_list = Queue(maxsize)
    get_info(file_list)
    print('共%d篇:\n' % (file_list.qsize()))

    for x in range(5):
        t = consumer(file_list)
        t.start()


# In[ ]:


if __name__ = '__main__':
    main()

