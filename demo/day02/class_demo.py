#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'cuicl'
#__mtime__ = '2019/9/5'



class ClassDemo():
    def aa(self):
        print('我是超越')
    def bb(self):
        print('我是小七')
    def cc(self):
        print('你是谁')
        self.aa()
if __name__ == '__main__':
    c = ClassDemo()
    c.bb()
    c.cc()