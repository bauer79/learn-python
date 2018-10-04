#!/usr/bin/python3
#-*-coding:UTF-8-*-

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1=count()
f2=count()
f3=count()

    
print('f1的结果是：',f1[2]())
print('f2的结果是：',f2())
print('f3的结果是：',f3())
