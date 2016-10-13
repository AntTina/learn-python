#!/usr/bin/python
# coding:utf-8
# 1.提醒用户输入目录的绝对路径
# 2.输出所有的.py文件
# 3.统计出.py文件的总数

import os
import fnmatch

# first method
way = raw_input("please input the path:")
num = 0
for path, d_name, f_name in os.walk(way):
    for i in fnmatch.filter(f_name, "*.py"):
        num += 1
        print os.path.join(path)

print "\033[31m%s flie(s)\033[0m" % num

# second method
py_list = []
for path, d_name, f_name in os.walk(way):
    for i in f_name:
        if i.endswith('.py'):
            print os.path.join(path, i)
            py_list.append(os.path.join(path, i))
print "\033[31m%s flie(s)\033[0m" % len(py_list)
