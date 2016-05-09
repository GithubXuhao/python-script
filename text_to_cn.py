# coding=utf-8
from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
fo = open("huajiao_text_cn", "wb")
urlfile = open("huajiao_text.txt", "r")
line = urlfile.readline()
while line:
#    print line,
    e = line.decode("unicode_escape")
#    print "\n"
#    print e
    m = e.replace("\\n", "").replace("\\r", "")
#    print "\n"
#    print m
    e = m.decode("unicode_escape")
#    print e
    fo.write(e)
#    fo.write("\r\n")
    line = urlfile.readline()


#    print a
#    time.sleep(1)
fo.close()
