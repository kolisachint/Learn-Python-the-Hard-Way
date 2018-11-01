#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Reading and Writing Files
# Usage: python3 ex16.py ../Files/file1.txt

from sys import argv

script,filename= argv

print("We are going to erase %r" % filename )
print("If you don't want that, hit CTRL- C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening file.....")
target= open(filename,'r')

print("Reading file.....")
print(target.read())

target.seek(15,0)             # seek only works with r, w, r+, w+ And not in a, a+ mode
print(target.read())

print("Truncating file.....")
target.truncate()             # Truncate is never required for any mode

print("Now I am going to ask you for three lines->")
line1= input("Line1:")
line2= input("Line2:")
line3= input("Line3:")

print("I am going to write to the file........")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And I am finally going to close the file......")
target.close()


# r mode won't allow you write or append a file
# w mode won't allow you to read [ For appending use seek ]
# a mode won't allow you to read or write a file from start [ Except append ]


# Traceback (most recent call last):
#   File "ex16.py", line 30, in <module>
#     target.writeline(line2)
# AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'


# Traceback (most recent call last):
#   File "ex16.py", line 20, in <module>
#     target.truncate()
# io.UnsupportedOperation: File not open for writing

# Traceback (most recent call last):
#   File "ex16.py", line 20, in <module>
#     print(target.read())
# io.UnsupportedOperation: not readable






