#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Asking Questions


print("How old are you?")
age=input()

# Indentation is used for block ending for conditional and loop operations
if age.isdigit():
	agenum=int(age)
else:
	agenum=0
	print("Please provide valid number for age field:")
	quit()
	
print("How tall are you?")
height=input()
print("How much do you weigh?")
weight=input()


print("So you are %d years old, %r in height and %r in weight" % (agenum,height,weight))


# Traceback (most recent call last):
#   File "ex11.py", line 11, in <module>
#     weight=int(input())
# ValueError: invalid literal for int() with base 10: 's'


#   File "ex11.py", line 17
#     print("How tall are you?")
#                              ^
# IndentationError: unindent does not match any outer indentation level