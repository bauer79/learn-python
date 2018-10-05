#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def eat(self):
		print('dog is eating')
	pass

class Cat(Animal):
	pass

def run_two_times(animal):
	animal.run()
	animal.run()

run_two_times(Animal())

run_two_times(Dog())

dog=Dog()
print(type(dog))
print('b是否为Dog类型：',isinstance(dog,Dog))
print('b是否为Animal类型：',isinstance(dog,Animal))

dog.run()
dog.eat()

cat=Cat()
cat.run()