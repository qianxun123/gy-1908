#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/5'


#1到100的和
def he():
    a = 0
    for  i in range(1,101):
        a += i;
    print(a)

#1到100！
def chengji():
    s = 1
    for i in range(1,101):
        s *= i
    print(s)

#100以内的质数
def zhishu():
    for i in range(2,100):
        f = False # 标记i是否被整除
        for j in range(2,i):
            if(i%j==0):
                f = True #如果i被整除，把f值改成True
                break
        if (not f):
            print(i)
#99乘法表
def cfb():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, "X", i, '=', i * j,"\t",end='',)
        print()
#冒泡循环
def maopao():
    a = [90, 43, 2, 63, 6, 3, 4]
    # 外层循环确定待排序的位置
    for i in range(len(a) - 1, 0, -1):
        # 内层循环依次取相邻的两个数据
        for j in range(i):
            # if判断比较相邻两个数据的大小，如果前边大于后边的，则交换位置
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]

print(zhishu())


if __name__ == '__main__':
    pass
