#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class MyClass(object):
	i=123
	def __init__(self,name):
		self.name=name

	def f(self):
		return 'hello world'+self.name

use_class=MyClass('xiaomeng')
#use_class.i=100
print('调用类的属性:',use_class.i)
print('调用类的方法:',use_class.f())