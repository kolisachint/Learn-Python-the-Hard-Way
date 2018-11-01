#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Reading Files
# Usage: python3 ex15.py ex14.py

from sys import argv

script,filename= argv

txt=open(filename)

print("Here is your file: %s" % filename)
print(txt.read())


print("Type the filename again:")
filename1 = input()

txt1=open(filename1)

print("Here is your file: %s" % filename1)
print(txt1.read())

#####################################
#  USE PYTHON3 INSTEAD OF PYTHON
#####################################

# Traceback (most recent call last):
#   File "ex15.py", line 16, in <module>
#     filename1=input()
#   File "<string>", line 1, in <module>
# NameError: name 'ex14' is not defined



