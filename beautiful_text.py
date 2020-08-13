#!/usr/bin/python3
import random
import bs4
import requests
import os
import pymysql

Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
url = 'https://www.baidu.com/'



db = pymysql.connect(host='localhost',user='root',password='liuke6152389',db = "douban_book",charset='utf8')

db_book = db.cursor()

sql = """create table wenxue(
        BOOK_ID INT UNSIGNED AUTO_INCREMENT,
        WEB varchar(100) not null,
        BIAOQIAN varchar(40) not null,
        NAME varchar(40) not null,
        ZUOZHE varchar(100),
        PINGFEN CHAR(20),
        NUMBER CHAR(20),
        JIANJIE varchar(100),
        PRIMARY KEY (BOOK_ID))"""

db_book.execute(sql)
db.close()


# r = requests.get('http://127.0.0.1:8000')
    # ip_ports = json.loads(r.text)
    # ip = ip_ports[0][0]
    # port = ip_ports[0][1]
    # print(str(ip) + ':' + str(port))
    # proxies = {
    #     'http': '%s:%s' % (ip, port),
    #     'https': '%s:%s' % (ip, port)
    # }
    # r = requests.get('https://book.douban.com/tag/', proxies=proxies)
    # r.encoding = 'utf-8'
    # print(r.text)
    # try:
    #     telnetlib.Telnet(str(ip), port=str(port), timeout=3)
    # except:
    #     print('ip无效！')
    # else:
    #     print('ip有效！')


# baidu = requests.get(url,headers=Headers)
# baidu_lxml = bs4.BeautifulSoup(baidu.text, "lxml")
# print(baidu_lxml.title.string)
#
# for i in range(1,100):
#     print(random.uniform(1, 10))

# print(os.path.splitext('E:/Python-project/My_Python/beautiful_text.py'))