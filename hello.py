#!usr/bin/env python3
# -*- coding: utf-8 -*-

name = input('please enter your name:')
print('hello',name)

height = 1.75
weight = 80.5
bmi = weight / (height*height)
if bmi < 18.5:
	print("过轻")
elif bmi >= 18.5 and bmi < 25:
	print("正常")
elif bmi >= 25 and bmi < 32:
	print("过重")
else:
	print("肥胖")
	
names = ['a','b','c']
names.insert(1,'aa')
for name in names:
	print(name)
	
list(range(100))
sum = 0
for x in range(101):
	sum = sum + x
print(sum)