#!/usr/bin/python3
import telnetlib
import random
import bs4
import requests
import json
import os
import time
import openpyxl
from bs4 import BeautifulSoup
import re
wb_data = openpyxl.Workbook()
ws_data = wb_data.active
Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    'User-Agent': "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)"
    }

# https://i1.joucus-tj.com/bookimages/1224/220513/1.jpg
labels = [ ]
f = open('PIC_path.txt','a',encoding='UTF-8')
class Spider():
    # 构造函数，初始化数据使用
    def __init__(self, target_url):
        self.target_url = target_url
        # self.headers = headers

    def GetOneType(self,Headers,num):
        print('正在抓取第' + str(num) + '页')
        rp = requests.get(self.target_url, headers=Headers)
        # print(rp)
        bsObj = BeautifulSoup(rp.text, "lxml")
        # print(bsObj)
        table_list = bsObj.find("table", {"summary": "forum_52"})
        # print(table_list)
        for tbody in table_list.find_all("tbody"):
            # print(tbody)
            Soup = bs4.BeautifulSoup(str(tbody), "lxml")
            l = Soup.find("a",{"class":"s xst"})
            # print(l)
            webl = re.findall("(?<=href=\").*?(?=\")", str(l))
            namel = re.findall("(?<=>).*?(?=</a>)",str(l))
            webs = ''.join(webl)
            names = ''.join(namel)
            namess = re.sub("\[", '', names)
            Mname = re.sub("\]", '', namess)
            print(len(Mname))
            if (len(Mname)) >= 10:
                web = str(webs)
                print(web+":"+str(Mname))
                f.write(web+":"+str(Mname)+'\r')
                deties = requests.get(web, headers=Headers)
                bs = BeautifulSoup(deties.text, "lxml")
                # print(bs)
                ds = bs.find("span",{"style":"white-space: nowrap"})
                down = re.findall("(?<=href=\").*?(?=\")",str(ds))
                try:
                    downs = ''.join(down)
                    d = re.sub('amp;','',downs)
                    if (len(d)) >= 10:
                        web_path = "http://btshoufa.cc/" + d
                        print(web_path)
                        f.write("http://btshoufa.cc/"+d+'\r')
                        # r = requests.get(web_path,headers=Headers)
                        # open('E:\\BaiduNetdiskDownload\\Movie\\'+str(Mname)+'.torrent', 'wb').write(r.content)
                        # print("done")
                except:
                    continue
        f.flush()

def main():
    for num in range(110,200):
        UrlLabel = 'http://www.btshoufa.cc/forum-52-'+ str(num) +'.html'
        sp = Spider(UrlLabel)
        # print(labels[i])
        # wb_data.create_sheet(labels[i])
        # ws_data = wb_data[labels[i]]
        # ws_data['A1'] = '网址'
        # ws_data['B1'] = '标签'
        # ws_data['C1'] = '书名'
        # ws_data['D1'] = '作者'
        # ws_data['E1'] = '评分'
        # ws_data['F1'] = '人数'
        # ws_data['G1'] = '简介'
        sp.GetOneType(Headers,num)
        # ws_data.save('douban.xlsx')
main()

