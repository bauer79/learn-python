#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class PrivatePublicMethods(object):
	def __init__(self):
		pass
	
	def __foo(self):    #私有方法
		print('这是私有方法')
	
	def foo(self):    #公共方法
		print('这是公共方法')
		print('公共方法中调用私有方法')
		self.__foo()
		print('公共方法中调用私有方法结束')

		
pri_pub=PrivatePublicMethods()
print('开始调用公共方法：')
pri_pub.foo()
print('开始调用私有方法：')
#pri_pub.__foo()