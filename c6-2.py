#!/usr/bin/python3
#-*-coding:UTF-8-*-

ams_num=[1,2,3,4,5,6,7,8,9,153,370,371,407]
num=input("请输入一个数字:")
num_input=int(num)
guess=0
j=0
for i in ams_num:
    guess+=1
    if num_input==i:
        print('%d 是一个阿姆斯特朗数,%d'%(num_input,guess))
        j=1
        break
    else:
        pass
if j==0:
    print('%d 不是一个阿姆斯特朗数'%num_input)

