#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/4'




#for 循环
'''
for i in range(10):
    代码块
'''

for i in range(10):
    print(i)
    print('超越')

for i in range(1,100,2):
    print(i)


#终止循环 break

#打印100以内的数，遇到5终止
for i in range(100):
    if(i == 5):
        break
    print(i)


#跳过本次循环 continu
#打印100以内的数，遇到被5整除的跳过
for i in range(100):
    if(i%5 == 0):
        continue
    print(i)

#whline循环
'''
i =0
whilne(判断条件)
    循环体
    i= i+1

'''

i= 1
while(i < 101):
    print(i)
    i+=1