#!/usr/bin/python3

import re


def collect_txt():
    f = open("LiuJason_Instagram.html",'r',encoding='UTF-8')
    w = open("web.txt",'w',encoding='UTF-8')
    line = f.readlines()
    news = []
    for l in line:
        ret = re.findall("(https://www.instagram.com/+[0-9A-Za-z/_\s.]*)", l)
        a = '\n'.join(ret)
        # print(a)
        w.write(a)
    w.close()
    f.close()

def dislodge_web():
    f = open("web.txt", 'r')
    w = open("ins.txt", 'w', encoding='UTF-8')
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
