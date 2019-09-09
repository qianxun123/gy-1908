#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/6'


'''21
key:value
key唯一
'''
# 增
# 初次创建
a = {}
a1 = {'name':'小七','sex':'女'}
# 新增一对数据
a1['age']= 21
a1['high'] = 170
print(a1)

# 删
# 删除key
print(a1.pop('high'))
print(a1)

del a1['sex']
print(a1)
print('---------')

# 删除整个字典

# del a1
# print(a1)

# 清空

# a1.clear()
# a1  = {}

# 改
a1['name'] = '超越'
print(a1)

# 查
print(a1['name'])

# 获取长度
print(len(a1))

# 成员判断，只能用key
print('name' in a1)

# 字典的拼接
a2 = {'1':'123','2':'789'}
a3 = {'3':'123','4':'456'}
# 在某个字典末尾加上另一个字典
# 拿着a3改a2,有key则改value,无则新增
# a2.update(a3)
# print(a2)

# 生成一个新的字典，key不能为int
print(dict(a2,**a3))