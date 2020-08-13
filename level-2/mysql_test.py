#!/usr/bin/python3


import pymysql
import os
import re


path = 'E:\BaiduNetdiskDownload\Movie'

dirs = os.listdir(path)
dir_list = []
bigs = []
smalls = []
infos = []
result_list = []


db = pymysql.connect("localhost","root","creatcomm@123")

def create_table():
    #连接本地数据库
    # db = pymysql.connect("localhost","root","liuke6152389")

    #创建游标
    cursor = db.cursor()
    try:
        cursor.execute("create database JAVBUS_database character set utf8;")  # awesome表示库的名字 如果原来有就会出错 这是一个空的还没有表
    except:
        print('此数据库已存在')

    cursor.execute("use JAVBUS_database;")  # 在这个库下面建表就要打开这个库

    #如果存在student表，则删除
    # cursor.execute("create table if not exists J_MOVIE")

    try:
        cursor.execute("create table if not exists J_MOVIE")  # 新建表名为 doudou
        #
    except:
        print('此表名已存在')

    #创建student表
    sql = """
        create table J_MOVIE(
        number char (20),
        name char(50),
        small_img char(100),
        big_img char(100),
        create_time char(10),
        time char(5),
        producer char(10),
        publisher char(10),
        series char(50),
        classes char(50),
        actor char(10),
        info char(100)
        )
    """

    try:
        # 执行SQL语句
        cursor.execute(sql)
        print("创建数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s"%e)
    finally:
        #关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def input_value(file,small,big,info):
    cursor = db.cursor()
    cursor.execute("use JAVBUS_database;")
    sql = "insert into J_MOVIE(number,small_img,big_img,info)values('%s','%s','%s','%s')" %(file,small,big,info)

    cursor.execute(sql)
    db.commit()

def split_list():
    for root, dirs, files in os.walk(path):
        for name in files:
            big = r'(_big.jpg)'
            small = r'(_small.jpg)'
            info = r'(_info.txt)'
            if re.findall(big, name):
                bigs.append(os.path.join(root, name))
                # print(bigs)
            if re.findall(small, name):
                smalls.append(os.path.join(root, name))
                # print(smalls)
            if re.findall(info, name):
                infos.append(os.path.join(root, name))
                # print(infos)
    return bigs, smalls, infos

def main():
    # create_table()
    if __name__ == '__main__':
        big_list, small_list, info_list = split_list()
        for file in dirs:
            # print("{}\{}".format(path,file))
            file_name = os.path.join(file)
            print(file + "写入MYSQL")
            for big, small, info in zip(big_list, small_list, info_list):
                if re.search(file_name, big):
                    # result_list.append(big)
                    # print('{}'.format(big))
                    pass
                if re.search(file_name, small):
                    # result_list.append(small)
                    # print('{}'.format(small))
                    pass
                if re.search(file_name, info):
                    # result_list.append(info)
                    # print('{}'.format(info))
                    # with open(info, "r", encoding="utf-8") as f:
                    #     lines = f.readlines()
                    # print(lines)
                    # print(file,lines[0],small,big,lines[2],lines[3],lines[4],lines[5],lines[6])
                    print(file,small.replace('\\','\\\\'),big.replace('\\','\\\\'),info.replace('\\','\\\\'))
                    input_value(file,small.replace('\\','\\\\'),big.replace('\\','\\\\'),info.replace('\\','\\\\'))
                    print("完成")
    # input_value("ABBA-471","E:\BaiduNetdiskDownload\Movie\ABBA-471\ABBA-471_small.jpg,big","E:\BaiduNetdiskDownload\Movie\ABBA-471\ABBA-471_big.jpg","E:\BaiduNetdiskDownload\Movie\ABBA-471\ABBA-471_info.txt")
    # print("完成")
    # create_table()
    # input_value()

if __name__ == "__main__":
    main()