#!/usr/bin/python3
#-*-coding:UTF-8-*-

path='./test.txt'

f_name=open(path,'w')
# print(f_name.name)
# print(f_name)
# print('read result:',f_name.read())
print('write length:',f_name.write('Hello world!'))
f_name=open(path,'r')
print('read result:',f_name.read())

f_name=open(path,'a')
print('add length:',f_name.write('\nwelcome!'))

f_name=open(path,'r')

print('read result:\n'+f_name.read())