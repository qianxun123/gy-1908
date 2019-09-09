#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/5'


#截取
a ='披荆斩棘天使翼'

print(a[0:4])
print(a[4:])
print(a[:6])
print(a[:-3])

#字符串倒叙
print(a[::-1])

#dergakio   要求生成两个新的字符串  drai  和egko
b ='dergakio'
print(b[::2])
print(b[1::2])

#通过下标取出字符
print(a[4])

#重复字符串
print(a * 2)


#字符串切片

d = '超越,小七,选一'
print(d.split(','))

#去空格
e = '    超 越 小 七 选 一    '
print(e.strip())
print(e.lstrip())
print(e.rstrip())
print(e.replace(' ',''))

#替换
f = '超越"小七"选一'
print(f.replace('"',"'"))

#查找
g = '超越小七选一'
print(g.find('小七'))

#长度
print(len(g))

#GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
l = 'GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1'
l = l.split(" ")
method = l[0]
print("请求方法为："+method)
xieyibanben = l[2]
print("协议版本为：" + xieyibanben)
url = l[1]
print(url)
if('?' in url):
    print("请求数据为：" + url.split("?")[1])
    url = url.split("?")[0]
print(url)
print("协议名为：" + url[:url.find("://")])

url = url[url.find("://") + 3:]
print(url)
if(":" in url):
    print("域名或者ip为："+url.split(":")[0])
    url  = url.split(":")[1]
    print(url)
    print("端口号为：" + url[:url.find('/')])
    print("请求地址为：" + url[url.find('/'):])
else:
    print("域名或者ip为：" + url[:url.find('/')])
    print("请求地址为：" + url[url.find('/'):])


