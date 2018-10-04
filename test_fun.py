#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def fun1(a):
	for i in range(len(a)):
		a[i]*=a[i]
	print(a)
	
a=[1,2,3]
fun1(a)
print(a)
