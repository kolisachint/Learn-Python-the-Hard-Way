#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# More Variables and Printing


my_name = 'Zed A. Shaw'
my_age = +35 # not a lie
my_height = +74 # inches
my_weight = +180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name                              )              
print("He's %d inches tall." % my_height                            )    
print("He's %d pounds heavy." % my_weight                           )              
print("Actually that's not too heavy."                              )        
print("He's got %s eyes and %s hair." % (my_eyes, my_hair)          )            
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight))

# Print 99 in different formats
print("99 can be printed like this : %s  " % 99 ) 
print("99 can be printed like this : %(num)+10r  " %{"num":99} ) 
print("99 can be printed like this : %(num)+10s  " %{"num":99} ) 

print("99 can be printed like this : %(num)010d  " %{"num":99} ) 
print("99 can be printed like this : %(num)10d  " %{"num":99} ) 
print("99 can be printed like this : %(num)-10d  " %{"num":99} ) 
print("99 can be printed like this : %(num)+10d  " %{"num":99} ) 

print("99 can be printed like this : %(num)+10e  " %{"num":99} ) 

print("99 can be printed like this : %(num)021f  " %{"num":99} ) 
print("99 can be printed like this : %(num)-21f  " %{"num":99} ) 
print("99 can be printed like this : %(num)+21f  " %{"num":99} ) 

print("99 can be printed like this : %(num)10g  " %{"num":99.01} ) 
print("99 can be printed like this : %(num)+21g  " %{"num":999999999999999999999.01} ) 
print("99 can be printed like this : %(num)+21g  " %{"num":999999} ) 

s="       sachin        "
print("Characters can be formatted as 'sachin' ", s)
print("Characters can be formatted as 'sachin' ", s.ljust(30))
print("Characters can be formatted as 'sachin' ", s.rjust(30))
print("Characters can be formatted as 'sachin' ", s.ljust(30,'X'))
print("Characters can be formatted as 'sachin' ", s.rjust(30,'X'))
print("Characters can be formatted as 'sachin' ", s.strip())
print("Characters can be formatted as 'sachin' ", s.lstrip())
print("Characters can be formatted as 'sachin' ", s.rstrip())

#print(num)
#
#Traceback (most recent call last):
#  File "ex5.py", line 42, in <module>
#    print(num)
#NameError: name 'num' is not defined