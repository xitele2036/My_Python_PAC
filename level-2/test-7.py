'''
计算两个日期相隔的秒数

#0034003700380032003500331595915738398
问题
输入任意两个日期，计算它们间相隔的秒数。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

日期格式为：2018-03-12 13:24:32‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

讨论
该函数可以用来编写一个倒计时器。比如距 XX 活动开始还有 XX 秒。
'''
import datetime


def date_delta(start, end):
    s = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
    e = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
    print(e-s)
    return((e-s).days*24*3600+float((e-s).seconds))

start = input()  # sys.stdin.readline()
end = input()  # sys.stdin.readline()

print(date_delta(start, end))