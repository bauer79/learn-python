#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import math

def quadratic(a,b,c):
	x[0]=(b+math.sqrt(b*b-4*a*c))/a/2
	x[1]=(b-math.sqrt(b*b-4*a*c))/a/2
	return x

a=1
b=4
c=1
x=[]
x.append((b+math.sqrt(b*b-4*a*c))/a/2)
x.append((b-math.sqrt(b*b-4*a*c))/a/2)
print(x)
y=quadratic(a,b,c)
print(y)