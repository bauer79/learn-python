#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class Fib(object):
    # def __init__(self):
        # self.a, self.b = 0, 1 # 初始化两个计数器a、b

    # def __iter__(self):
        # return self # 实例本身就是迭代对象，故返回自己

    # def __next__(self):
        # self.a, self.b = self.b, self.a + self.b # 计算下一个值
        # if self.a > 1000000: # 退出循环的条件
            # raise StopIteration();
        # return self.a # 返回下一个值
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
	def __getattr__(self,attr):
		return None
		

fib=Fib()
print(fib[120])
print(fib.score)
		
#for n in Fib():
#	print(n)