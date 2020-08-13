#!/usr/bin/python3

import re
import requests
import json
import os
import time

# https://i1.joucus-tj.com/bookimages/1224/220513/1.jpg

class Spider():
    # 构造函数，初始化数据使用
    def __init__(self, target_url):
        self.target_url = target_url
        # self.headers = headers

    # 获取所有的想要抓取的URL
    def getUrls(self):
        jsonData = requests.get(self.target_url)
        data = json.loads(jsonData.text)
        datas = data['result']['list']
        http = "https://i1.joucus-tj.com"
        url = []
        for i in datas:
            title = i['title']
            print(title)
            path = 'E:\\Backup_tmp\\ZZMH\\Loser\\' + title[0:5]
            os.makedirs(path)
            # time.sleep(2)
            # print(i['imagelist'])
            url = i['imagelist']
            urls = url.split(",")
            for x in urls:
                bookimages = x.lstrip('.')
                full = http + bookimages
                print(full)
                fulls = full.lstrip('/')
                fu = fulls.split('/')[-1]
                file = path + '/' + fu
                # print(file)
                respon = requests.get(full)
                print(file)
                with open(file,"wb") as f:
                    f.write(respon.content)
                    f.close



def collect_txt():
    f = open("meimei2.html",'r',encoding='UTF-8')
    w = open("web-tmp.txt",'w',encoding='UTF-8')
    line = f.readlines()
    news = []
    for l in line:
        # print(type(l))
        ret = re.findall('(https:[a-zA-z0-9/*._]+)',l,re.S)
        # print(type(ret))
        a = ''.join(ret)
        text = re.compile(r".*[0-9]$")
        if text.match(a):
            # print(a)
            w.write(a+'\n')
        else:
            continue
    w.close()
    f.close()

def dislodge_web():
    f = open("web-tmp.txt", 'r')
    w = open("manhua.txt", 'a+', encoding='UTF-8')
    line = f.readlines()
    news = []
    for l in line:
        if not l in news:
            news.append(l)
    for i in news:
        print(i)
        w.write(i)



def main():
    # collect_txt()
    # dislodge_web()
    # 头文件，header是字典类型
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    #     'HOST': 'https://m.zuozuos.com/home/book/chapter_list/id/8131'
    # }
    for x in range(1,20):
        target_url = 'https://m.zuozuos.com/home/api/chapter_list/tp/8196-1-'+str(x)+'-10'  # 图片集和列表规则
        S = Spider(target_url)
        S.getUrls()
main()

