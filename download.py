#!/usr/bin/python
#encoding:utf-8

import requests
import time
import os
import re
import threading

all_urls = []  # 我们拼接好的图片集和列表路径
g_lock = threading.Lock()

class Spider():
    # 构造函数，初始化数据使用
    def __init__(self, target_url, headers):
        self.target_url = target_url
        self.headers = headers

    # 获取所有的想要抓取的URL
    def getUrls(self, start_page, page_num):
        global all_urls
        # 循环得到URL
        for i in range(start_page, page_num + 1):
            url = self.target_url % i
            all_urls.append(url)


class Producer(threading.Thread):

    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST': 'www.meizitu.com'
        }
        global all_urls
        while len(all_urls) > 0:
            g_lock.acquire()  # 在访问all_urls的时候，需要使用锁机制
            page_url = all_urls.pop()  # 通过pop方法移除最后一个元素，并且返回该值

            g_lock.release()  # 使用完成之后及时把锁给释放，方便其他线程使用
            try:
                print("分析" + page_url)
                response = requests.get(page_url, headers=headers, timeout=3)
                all_pic_link = re.findall('<a target=\'_blank\' href="(.*?)">', response.text, re.S)
                global all_img_urls
                g_lock.acquire()  # 这里还有一个锁
                all_img_urls += all_pic_link  # 这个地方注意数组的拼接，没有用append直接用的+=也算是python的一个新语法吧
                print(all_img_urls)
                g_lock.release()  # 释放锁
                time.sleep(0.5)
            except:
                pass


if __name__=="__main__":
    # 头文件，header是字典类型
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'HOST': 'www.meizitu.com'
    }
    target_url = 'http://www.meizitu.com/a/pure_%d.html'  # 图片集和列表规则

    spider = Spider(target_url, headers)
    spider.getUrls(1, 16)
    print(all_urls)
    page_url = all_urls.pop()
    print(page_url)
    for x in range(2):
        t = Producer()
        t.start()
        t.run()