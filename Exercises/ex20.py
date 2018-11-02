#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Functions and Files
# Usage python3 ex20.py ../Files/file1.txt

from sys import argv

script, input_file = argv

# Print file content
def print_file(f):
  print(f.read())

# Rewind back to starting postion of file
def rewind(f):
  f.seek(0)
  
def print_line(linenum,f):
  print(linenum , ':' , f.readline(), end='')
  
current_file=open(input_file)

print("Lets print whole file:")
print_file(current_file)

print("Lets rewind back to original position of file")
rewind(current_file)

print("Print content line by line")
current_line=1
print_line(current_line,current_file)
print_line(current_line+1,current_file)
print_line(current_line+2,current_file)




# Traceback (most recent call last):
#   File "ex20.py", line 31, in <module>
#     print_line(current_line,current_file)
#   File "ex20.py", line 19, in print_line
#     print(linenum + ':' + f.readline(), end='')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

