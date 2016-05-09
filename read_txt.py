# coding=utf-8
from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
fo = open("2.txt", "wb")
urlfile = open("1.txt", "r")
line = urlfile.readline()
while line:
#    print line,
    e = line.split("\t")
    print e[0]
    print e[1]
    print e[2]
#
    fo.write(e[0])
    fo.write("\r")
    fo.write(e[1])
    line = urlfile.readline()


#    print a
#    time.sleep(1)
fo.close()
