#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Names, Variables, Code, Functions
# Usage: python3 ex17.py ../Files/file2.txt ../Files/file3.txt

# this one is like scripts with argv
def print_tuple(*argv):
  arg1,arg2=argv
  print("print_tuple arguments %s, %s " % (arg1, arg2))
  
# this one is like scripts with arg1,arg2
def print_multiargs(arg1,arg2):
  print("print with multiple arguments %s, %s " % (arg1,arg2))
  
# this one is with only one parameter
def print_onearg(arg1):
  print("print with one argument %s " % arg1)

# this one is with no parameter
def print_none():
  print("print with no arguments")

# Calling functions now
print_tuple("sachin","koli")
print_multiargs("sachin","koli")
print_onearg("sachin")
print_none()




# cabox@Learn-Python-the-Hard-Way:~/workspace/Exercises$ python3 ex18.py
#   File "ex18.py", line 13
#     print("print with multiple arguments %s, %s ", % (arg1,arg2))
#                                                    ^
# SyntaxError: invalid syntax

# cabox@Learn-Python-the-Hard-Way:~/workspace/Exercises$ python3 ex18.py
# Traceback (most recent call last):
#   File "ex18.py", line 24, in <module>
#     print_tuple("sachin","koli")
#   File "ex18.py", line 9, in print_tuple
#     print("print_tuple arguments %s, %s, %s " % (arg1, arg2))
# TypeError: not enough arguments for format string

# cabox@Learn-Python-the-Hard-Way:~/workspace/Exercises$ python3 ex18.py
# Traceback (most recent call last):
#   File "ex18.py", line 24, in <module>
#     print_tuple("sachin","koli")
#   File "ex18.py", line 9, in print_tuple
#     print("print_tuple arguments %s, %s, %s " % (arg1, arg2))
# TypeError: not enough arguments for format string
