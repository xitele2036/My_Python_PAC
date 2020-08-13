'''
处理 HTTP 协议中的日期字段

#0034003700380032003500331595916760700
问题
现在你需要处理一个历史遗留问题，HTTP 应用中曾经允许过三种格式的日期表示法：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

Sun, 06 Nov 1994 08:49:37 GMT  ; RFC 822, updated by RFC 1123
Sunday, 06-Nov-94 08:49:37 GMT ; RFC 850, obsoleted by RFC 1036
Sun Nov  6 08:49:37 1994       ; ANSI C's asctime() format
编写一个函数来将这样的日期字符串转化为 datetime 对象
'''

import sys
import datetime


def parse_http_datetime(s):
    if '-'in s:
        return datetime.datetime.strptime(s, "%A, %d-%b-%y %H:%M:%S %Z")
    elif s[-1] in ['T']:
        return datetime.datetime.strptime(s, "%a, %d %b %Y %H:%M:%S %Z")
    else:
        return datetime.datetime.strptime(s, "%a %b %d %H:%M:%S %Y")


while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print(parse_http_datetime(line))
