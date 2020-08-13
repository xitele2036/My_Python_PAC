'''
各种时间格式转化为标准时间格式
20:15:33 2020-01-01
2020-01-01 20:15:33
'''



import sys
import datetime

def standard_times(line):
    s = datetime.datetime.strptime(line,'%H:%M:%S %Y-%m-%d')
    return s
while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print(standard_times(line))