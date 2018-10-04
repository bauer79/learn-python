#!/usr/bin/python3
#-*-coding:UTF-8-*-
greeting='hello'
if greeting=='hello':
	student={'小萌':'1001','小智':'1002','小强':'1005','小张':'1006'}
	print('字典元素个数为： %d个'%len(student))
	student.clear()
	print('字典删除后元素个数为：%d个'%len(student))
