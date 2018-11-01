#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Parameters, Unpacking, Variables

from sys import argv

# argv is tuple here. Check below statement for tuple assignments
if len(argv) == 4 :
	script,first,second,third=argv
else: 
	print("Incorrect number of parameters passed to the script:")
	print("Correct usage is : python3 ex13.py [arg1] [arg2] [arg3] ")
	exit()

print("The script is called:", script)
print("First argument:", first)
print("Second argument:", second)
print("Third argument:", third)

# Overwriting global parameters with local parameters.
argv="first","second","third"
argv= argv + ('fourth',)      # Nested tuples with "," , Addition to the tuple with "+"
print(argv)
script,first,second,third=argv

print("The script is called:", script)
print("First argument:", first)
print("Second argument:", second)
print("Third argument:", third)



# Traceback (most recent call last):
#   File "ex13.py", line 7, in <module>
#     script,first,second,third=argv
# ValueError: not enough values to unpack (expected 4, got 1)


# Traceback (most recent call last):
#   File "ex13.py", line 7, in <module>
#     script,first,second,third=argv
# ValueError: too many values to unpack (expected 4)


# Traceback (most recent call last):
#   File "ex13.py", line 26, in <module>
#     argv[4]="fourth"
# TypeError: 'tuple' object does not support item assignment
	
# Traceback (most recent call last):
#   File "ex13.py", line 26, in <module>
#     argv= argv + "fourth"
# TypeError: can only concatenate tuple (not "str") to tuple
	