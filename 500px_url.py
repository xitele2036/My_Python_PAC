#!/usr/bin/python3

import re


def collect_txt():
    f = open("liujason.html",'r',encoding='UTF-8')
    w = open("web-tmp.txt",'w',encoding='UTF-8')
    line = f.readlines()
    news = []
    for l in line:
        ret = re.findall("(https://500px.com/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])", l)
        a = '\r'.join(ret)
        # print(a)
        w.write(a+'\n')
    w.close()
    f.close()

def dislodge_web():
    f = open("web-tmp.txt", 'r')
    w = open("500px.txt", 'a+', encoding='UTF-8')
    line = f.readlines()
    news = []
    for l in line:
        if not l in news:
            news.append(l)
    for i in news:
        print(i)
        w.write(i)


def main():
    collect_txt()
    dislodge_web()


main()
