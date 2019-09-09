#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/4'



'''
if(条件):
    代码块
else:
    代码块

'''

# 举例
a = 1 #1有东西，0没东西
if(a == 0):
    print("买东西")
else:
    print("回家吧")



'''
if(条件)：
    代码块
elif(条件)：
    代码块
else:
    代码块

'''

#80优秀 70-80良好 60-70中等 60分不及格
s = 69

if(s >= 80):
    print("优秀")
if(s >= 60 and s <80):
    print("良好")
if(s <60 ):
    print("不及格")



if(s >= 80):
    print("优秀")
elif(s >= 70):
    print("良好")
elif (s >= 60):
    print("中等")
else:
    print("不及格")




