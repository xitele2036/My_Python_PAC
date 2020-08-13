'''
获得昨天和明天的日期

#0034003700380032003500331595914234864
问题
编写一个函数，接收一个日期输入，并输出该日期前一天和后一天的日期‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

日期格式为：2018-03-21‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

讨论
可以使用标准数学运算来操纵 datetime 示例。如果想表示一个时间间隔，可以使用 datetime.timedelta 方法。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬


'''

import datetime
import sys


def next_day(date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    nextday = date + datetime.timedelta(days=1)
    result = nextday.strftime('%Y-%m-%d')
    return result

def prev_day(date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    prevday = date - datetime.timedelta(days=1)
    result = prevday.strftime('%Y-%m-%d')
    return result

while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print('前一天:', prev_day(line))
    print('后一天:', next_day(line))
