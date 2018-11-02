#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Even more practice
# Usage: from ex25 import *

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')          # Split creates list [a,b,c]
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)               # push/pop can be used with lists
	print(word)

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(- 1)
	print(word)

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
  
  
# >>> ex25.print_last_word(words)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/cabox/workspace/Exercises/ex25.py", line 22, in print_last_word
#     word = words.pop(- 1)
# IndexError: pop from empty list