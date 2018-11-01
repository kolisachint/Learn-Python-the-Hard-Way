#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# What Was That?


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# In Multiline statements one can use newline, or \n character
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print("""
A multiline
string literal
""")

print(
"Multiline code, not multiline string literal"
)

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#  File "ex10.py", line 17
#    print tabby_cat
#                  ^
#SyntaxError: Missing parentheses in call to 'print'