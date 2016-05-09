# coding=utf-8
from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
fo = open("bjtime_huajiao.txt", "wb")
urlfile = open("huajiao_time.txt", "r")
line = urlfile.readline()
while line:
#    print line,
    c = int(line)
    b = c / 1000
    timeArray = time.localtime(b)
    a = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    fo.write(a)
    fo.write("\r\n")
    line = urlfile.readline()


#    print a
#    time.sleep(1)
fo.close()
