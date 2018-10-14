#!/usr/bin/python3
#-*-coding:UTF-8-*-

import time

#print('当前的时间：',time.localtime()[0:5])

s=568745203
t=time.localtime(s)
print('time.asctime(t): %s'%time.asctime(t))
