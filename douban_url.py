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
proxies = {
  "http": "http://120.83.108.89:9999",
  "https": "https://218.249.45.162:35586",
}
# https://i1.joucus-tj.com/bookimages/1224/220513/1.jpg
labels = [ ]
page = 51
class Spider():
    # 构造函数，初始化数据使用
    def __init__(self, target_url):
        self.target_url = target_url
        # self.headers = headers

    def GetOneType(self, Headers, Num, ws_data):
        STR = r'class="nbg" href="(.*?)".*?src="(.*?)".*?title="(.*?)".*?<div class="pub">\s*(.*?)\/.*?nums">(.*?)</span>.*?pl">(0-9*)</span>.*?<p>(.*?)</p>'
        for i in range(page):
            print('正在抓取' + labels[Num] + '类的第' + str(i) + '页')
            url = self.target_url + '?start=' + str(i * 20) + '&type=S'
            rp = requests.get(url, headers=Headers)
            bsObj = BeautifulSoup(rp.text, "lxml")
            bookList=[]
            bookCategroy = bsObj.h1.string
            for book in bsObj.find_all("li", {"class": "subject-item"}):
                bookSoup = bs4.BeautifulSoup(str(book), "lxml")
                bookweb = bookSoup.h2.a["href"]
                bookTitle = bookSoup.h2.a["title"]
                # print(bookTitle)
                bookAuthor = bookSoup.find("div", {"class": "pub"})
                # print(bookAuthor)
                bookrating = bookSoup.find("span", {"class": "rating_nums"})
                bookComment = bookSoup.find("span", {"class": "pl"})
                # print(bookComment)
                bookContent = bookSoup.li.p
                # print(bookContent)
                try:
                    if bookweb and bookTitle and bookAuthor and bookComment and bookContent:
                        bookList.append([bookweb.strip(),bookCategroy.strip(),bookTitle.strip(),bookAuthor.string.strip(),bookrating.string.strip(),
                                     bookComment.string.strip(), bookContent.string.strip()])
                except:
                    continue
            # content = rp.text
            # data = json.loads(rp.text)
            # print(type(data))
            time.sleep(5 + random.uniform(1, 10))


        #     result = re.findall(STR, content, re.S | re.M)
            for strs in bookList:
                print(strs)
                ws_data.append(strs)
        wb_data.save('豆瓣读书.xlsx')


def main():

    f = open("标签.txt", 'r', encoding='UTF-8')
    line = f.readlines()
    for l in line:
        n = l.replace('\n', '')
        labels.append(n)
    print(labels)
    for i in range(len(labels)):
        UrlLabel = 'https://book.douban.com/tag/' + labels[i]
        sp = Spider(UrlLabel)
        print(labels[i])
        wb_data.create_sheet(labels[i])
        ws_data = wb_data[labels[i]]
        ws_data['A1'] = '网址'
        ws_data['B1'] = '标签'
        ws_data['C1'] = '书名'
        ws_data['D1'] = '作者'
        ws_data['E1'] = '评分'
        ws_data['F1'] = '人数'
        ws_data['G1'] = '简介'
        sp.GetOneType(Headers,i,ws_data)
        # ws_data.save('douban.xlsx')
main()

