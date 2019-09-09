#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/5'



#无参数，无返回值的方法
def jiafa():
    a = 1
    b = 2
    print(a+b)

#方法调用
jiafa()

#有参数，无返回值的方法
def jiafa(a,b):
    print(a+b)

#方法调用
jiafa(12,54)
jiafa(6,4)

#无参数，有返回值的方法
def jiafa():
    a = 1
    b = 2
    return a + b

#方法调用
c = jiafa()
print(c)

#有参数，有返回值的方法
def jiafa(a,b):
    return a + b

#方法调用
c = jiafa(1,3)
print(c)


def aaa(a,b = 10):
    return  a+b

print(aaa(11))
print(aaa(11,11))
print(aaa(11,b = 11))


def bbb(*args,**kwargs):
    print(args)
    print(kwargs)

bbb({'name':'6'},{'mmm':'44'})
bbb(1,2,3,4,[1,5,4],a=11,b=12)








