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

file_path = 'E:\\Python\\JBUS\\Movie\\'
update_path = 'E:\\Python\\JBUS\\Movie\\Movie_update\\'


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



class Spider():
    # 构造函数，初始化数据使用
    def __init__(self, target_url):
        self.target_url = target_url
        # self.headers = headers

    def GetOnePage(self,Headers,num):
        global jpg_path, name, date_name
        print('正在抓取第' + str(num) + '页')
        rp = requests.get(self.target_url, headers=Headers)
        # print(rp)
        bsObj = BeautifulSoup(rp.text, "lxml")
        # print(bsObj)
        table_list = bsObj.find("div", {"id": "waterfall"})
        # print(table_list)
        # for tbody in table_list.find_all("div"):
        #     print(tbody)
        Soup = bs4.BeautifulSoup(str(table_list), "lxml")
        try:
            for all in Soup.find_all("a"):
                j_path = all.get("href")
                # print(j_path)
                for img in all.find_all("img"):
                    jpg_path = img.get("src")
                    name = img.get("title")
                    # print(jpg_path)
                    # print(name)
                for date in all.find_all("span"):
                    date_name = date.date.string
                    # print(type(date_name))
                # text_path = file_path + date_name
                # print("{:*^60}".format('+'))

            # print(text_path)
                if os.path.exists(file_path) == False:
                    os.mkdir(file_path)
                r = requests.get(jpg_path,headers=Headers)
                open(file_path+'\\'+str(date_name)+'_small.jpg', 'wb').write(r.content)
                self.Getinfo(j_path,file_path)
                print("done")
        except:
            print("文件目录不存在")
        print("{:*^60}".format('+'))

    def Getinfo(self,info_url,text_path=None):

        global big_img_path

        full_path = text_path +'\\'+ date_name + '_info.txt'
        file = open(full_path, 'w', encoding='utf-8')
        print('正在抓取' + info_url + '详细页面')
        rp_info = requests.get(info_url, headers=Headers)
        bs_info = BeautifulSoup(rp_info.text, "lxml")
        info_list = bs_info.find("div", {"class": "container"})
        Soup = bs4.BeautifulSoup(str(info_list), "lxml")
        # try:
            # print(Soup.h3.string)
        file.write("电影名: " + Soup.h3.string + '\n')
        for big_img in Soup.find("a"):
            big_img_path = big_img.get("src")
            # print(big_img.get("src"))
            # print(big_img.get("title"))
        for big_img in Soup.find_all("p"):
            str_info = list(big_img.stripped_strings)
            # print(' '.join(str_info))
            msg = ' '.join(str_info)
            file.write(msg + '\n')
        r = requests.get(big_img_path, headers=Headers)
        open(text_path + '\\' + str(date_name) + '_big.jpg', 'wb').write(r.content)
        file.close()
        # except:
        #     print("获取INFO FAIL")

    def updateOnePage(self,Headers,num):
        global jpg_path, name, date_name
        print('正在抓取第' + str(num) + '页')
        rp = requests.get(self.target_url, headers=Headers)
        # print(rp)
        bsObj = BeautifulSoup(rp.text, "lxml")
        # print(bsObj)
        table_list = bsObj.find("div", {"id": "waterfall"})
        # print(table_list)
        # for tbody in table_list.find_all("div"):
            # print(tbody)
        Soup = bs4.BeautifulSoup(str(table_list), "lxml")
        try:
            for all in Soup.find_all("a"):
                j_path = all.get("href")
                # print(j_path)
                for img in all.find_all("img"):
                    jpg_path = img.get("src")
                    name = img.get("title")
                    # print(jpg_path)
                    # print(name)
                for date in all.find_all("span"):
                    date_name = date.date.string
                    # print(date_name)
                text_path = file_path + date_name
                textupdate__path = update_path + date_name
                # print("{:*^60}".format('+'))

            # print(text_path)
                if os.path.exists(text_path) == False:
                    os.mkdir(textupdate__path)
                    r = requests.get(jpg_path,headers=Headers)
                    open(textupdate__path+'\\'+str(date_name)+'_small.jpg', 'wb').write(r.content)
                    self.Getinfo(j_path,textupdate__path)
                    print("done")
                else:
                    print(date_name + "已存在")
                    continue

        except:
            print("FAIL")
        print("{:*^60}".format('+'))

    def Getinfo_test(self,info_url,text_path=None):

        global big_img_path

        # full_path = text_path +'\\'+ date_name + '.txt'
        # file = open(full_path, 'w', encoding='utf-8')
        print('正在抓取' + info_url + '详细页面')
        rp_info = requests.get(info_url, headers=Headers)
        bs_info = BeautifulSoup(rp_info.text, "lxml")
        info_list = bs_info.find("div", {"class": "container"})
        Soup = bs4.BeautifulSoup(str(info_list), "lxml")
        try:
            # print(Soup.h3.string)
            # file.write("电影名: " + Soup.h3.string + '\n')
            for big_img in Soup.find("a"):
                big_img_path = big_img.get("src")
                # print(big_img.get("src"))
                # print(big_img.get("title"))
            for big_img in Soup.find_all("p"):
                str_info = list(big_img.stripped_strings)
                # print(' '.join(str_info))
                # msg = ' '.join(str_info)
            #     file.write(msg + '\n')
            # r = requests.get(big_img_path, headers=Headers, proxies=proxies)
            # open(file_path + date_name + '\\' + str(date_name) + '_big.jpg', 'wb').write(r.content)
            # file.close()
        except:
            print("FAIL")





def main():
    for num in range(117,200):
        UrlLabel = 'https://www.javbus.com/page/'+ str(num)
        sp = Spider(UrlLabel)
        sp.GetOnePage(Headers,num)
        # sp.updateOnePage(Headers,num)
        # sp.Getinfo_test("https://www.javbus.com/KNAM-019")
main()

# https://www.javbus.one/page/1
# https://www.javbus.com/uncensored/page/1
# https://www.javbus.com/page/1