#!/usr/bin/python3


import pymysql
import random



db = pymysql.connect("localhost","root","creatcomm@123")

def create_table():
    #连接本地数据库
    # db = pymysql.connect("localhost","root","liuke6152389")

    #创建游标
    cursor = db.cursor()
    try:
        cursor.execute("create database JAVBUS_datebase character set utf8;")  # awesome表示库的名字 如果原来有就会出错 这是一个空的还没有表
    except:
        print('此数据库已存在')

    cursor.execute("use JAVBUS_datebase;")  # 在这个库下面建表就要打开这个库

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
        number char (10),
        name char(50),
        small_img char(100),
        big_img char(100),
        create_time char(10),
        time char(5),
        producer char(10),
        publisher char(10),
        series char(50),
        classes char(50),
        actor char(10)
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

def input_value():
    cursor = db.cursor()
    cursor.execute("use JAVBUS_datebase;")
    sql = "insert into J_MOVIE(number,name,small_img,big_img,create_time,time,producer,publisher,series,classes,actor)values(n,'W','E:\\BaiduNetdiskDownload\\Movie\\OTIM-020\\OTIM-020.jpg','E:\\\BaiduNetdiskDownload\\\Movie\\\OTIM-020\\\OTIM-020_big.jpg','2020-04-11','170分鐘','Fitch','Fitch','W','sdsd','三')"

    cursor.execute(sql)
    db.commit()


def main():
    # create_table()
    input_value()

if __name__ == "__main__":
    main()