#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# While-Loops


i = 0
numbers = []

while i < 6:
	print("At the top i is %d" % i)
	numbers.append(i)
	i = i + 1
	print("Numbers now: ", numbers)
	print("At the bottom i is %d" % i)

for x in range(0,6):
  print("Numbers in For loop -> %d " % x)

  
print("The numbers: ")

for num in numbers:
	print(num)