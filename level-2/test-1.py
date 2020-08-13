'''
将形如 5D, 30s 的字符串转为秒

#0034003700380032003500331595913671373
问题
编写一个函数，将形如 5D, 30s, 的字符串转为秒‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

=========   ======= ===================
Character   Meaning Example
=========   ======= ===================
s           Seconds '60s' -> 60 Seconds
m           Minutes '5m'  -> 5 Minutes
h           Hours   '24h' -> 24 Hours
d           Days    '7d'  -> 7 Days
=========   ======= ===================
讨论
这个函数能够提高时间间隔作为参数时的可读性， 比如设置一个计时器 set_timer('20m')。 因此在一些开源项目内得到应用。
'''

import sys


def convert_to_seconds(time_str):
    if time_str[-1] in ['s', 'S']:
        return float(time_str[0:-1])*1.0
    elif time_str[-1] in ['m', 'M']:
        return float(time_str[0:-1])*60.0
    elif time_str[-1] in ['h', 'h']:
        return float(time_str[0:-1])*3600.0
    elif time_str[-1] in ['d', 'D']:
        return float(time_str[0:-1])*24*3600.0


while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print(convert_to_seconds(line))

