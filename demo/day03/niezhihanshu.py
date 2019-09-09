#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/6'

# aaa = open("test.txt","r",encoding='utf-8')
# #按行读取文件内容，返回一个列表
# # print(aaa.readlines())
# #返回一个字符串
# print(aaa.read())
# aaa.close()

aaa = open("test.txt","a",encoding='utf-8')
# aaa.write('woshichaoyue')
aaa.writelines(['fdddsadsdsd\n','qqqqqqqq\n','wwwwwwww\n'])
#关闭文件
aaa.close()
