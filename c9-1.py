#!/usr/bin/python3
#-*-coding:UTF-8-*-

def exp_exception(x,y):
	try:
		a=x/y
		print('a=',a)
		return a
	except ZeroDivisionError:
		print('程序出现异常，异常信息：被除数为0')
	except TypeError:
		print('缺少变量')

exp_exception(2,0)