#!/usr/bin/python
# -*- coding:UTF-8 -*-

import sys
import linecache


import linecache



def check_line(file, line_count, count):
#检查当前行的token1
    line1 = linecache.getline(file, line_count).strip()
    print line1
    e1 = line1.split("\t")
    print e1
    token1 = e1[n]
#从当前行开始，找到与当前行token不一样的行返回
    for i in range(1, count - line_count + 1):
        line2 = linecache.getline(file, line_count + i).strip()
        e2 = line2.split("\t")
        token2 = e2[n]
        if token2 != token1:
            return line_count + i - 1
    return count
def write_part(file, start_line, end_line, outfile):
    fo = open(outfile, "wb")
    for i in range(start_line, end_line + 1):
        line = linecache.getline(file, i).strip()
        fo.write(line + "\n")
    fo.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    if not len(args) == 3:
        print 'Usage:%s <filepath> <part_count> <token_count>' %(sys.argv[0])
        sys.exit()
    filepath = sys.argv[1] #要被切分的文件
    part_count = sys.argv[2] #切分的份数
    token_count = sys.argv[3] #文件的token在第几列
    n = int(token_count)
    part_count = int(part_count)
    with open(filepath, "r") as a:
        start_line = [0]*100
        end_line = [0]*100
#计算出总的行数
        count = len(a.readlines())
#平均每份大概多少行
    ave_lines = count / part_count
    end_line[0] = 0
    for i in range(1, part_count + 1):
        next_end = end_line[i-1] + ave_lines
#如果下一份的最后一行已经大于等于总行出则直接取最后一行为结尾，结束循环
        if next_end >= count:
            end_line[i] = count
            start_line[i] = end_line[i-1] +1#开始行为上一个结束行+1
            outfile = "part" + str(i)
            write_part(filepath, start_line[i], end_line[i], outfile)
            break
#调用check函数检查暂定的最后一行的下一行与它是否为同一个TOKEN
        end_line[i] = check_line(filepath, next_end, count)
#如果本份的结行就是最后一行直接break
        if end_line[i] == count:
            start_line[i] = end_line[i-1] +1
            outfile = "part" + str(i)
            write_part(filepath, start_line[i], end_line[i], outfile)
            break
        start_line[i] = end_line[i-1] +1
        outfile = "part" + str(i)
        write_part(filepath, start_line[i], end_line[i], outfile)
