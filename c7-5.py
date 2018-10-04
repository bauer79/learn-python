#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def func(x):
    return x>3

a=func(10)
f_list=filter(func,[1,2,3,4,5])

print('列表中大于3的元素有：',[item for item in f_list])