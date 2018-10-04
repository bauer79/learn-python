#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1= count()
f2= count()
f3= count()
print('f1的结果是：',f1())
print('f2的结果是：',f2())
print('f3的结果是：',f3())