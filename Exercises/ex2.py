#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# Comments , Pound Characters and Docstrings

# A comment, this is so you can read it later
# Anything after # this is ignored by python

print("I could have code like this.")		# and comment after this is ignored

# You can also use comment to 'disable' or comment out piece of code.
# print("This won't run.")

print("This will run.")

print("""
This will still run with #.
# is considered character when used in code.
This is A multiline string literal used with \"\"\" or ''' inside print function
""")

"""
This is docstring and will be parsed by interpreter and uses memory as well.
"""
'''
This is docstring and will be parsed by interpreter and uses memory as well.
'''

# Multiline comments works like this
# Do not confuse it with docstring use with -> """ or ''' 
# Docstrings are parsed by interpreter and uses memory. They are no way ignored by python.
# Multiline block ends here.
