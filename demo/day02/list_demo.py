#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/5'


z = [1,2,3,4,5,6,7,8,9]

#在后面新增单个数据
z.append(0)
print(z)

#在某个位置新增数据
z.insert(2,1.5)
print(z)

#在后面新增多个数据
x =[1,2,3,4]
z.extend(x)
print(z)
print(x)

#删除数据
print(z.pop())
print(z)
print(z.pop(2))
print(z)
print(z.pop(-3))
print(z)

#根据内容删除数据
z.remove(2)
print(z)

#修改列表数据
z[2]=12
print(z)

#排序
z.sort(reverse=True)
print(z)


