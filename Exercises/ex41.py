#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Learning to Speak Object Oriented

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
	}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip().decode('utf-8'))


def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
								random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
		
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
	
	for sentence in snippet, phrase:
		result = sentence[:]
 
	results.append(result)
	
	# fake class names
	for word in class_names:
		result = result.replace("%%%", word, 1)
	
	# fake other names
	for word in other_names:
		result = result.replace("***", word, 1)
	
	# fake parameter lists
	for word in param_names:
		result = result.replace("@@@", word, 1)
	
	results.append(result)
#	print(results[0],"\n")	
	return results


# keep going until they hit CTRL- D
try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print(question)
			
			input("> ")
			print("ANSWER: %s\n\n" % answer)
except EOFError:
	print("\nBye")


	
# 	cabox@Learn-Python-the-Hard-Way:~/workspace/Exercises$ python3 ex41.py
#   File "ex41.py", line 75
#     phrase = PHRASES[snippet]
#          ^
# IndentationError: expected an indented block

# cabox@Learn-Python-the-Hard-Way:~/workspace/Exercises$ python3 ex41.py
# Traceback (most recent call last):
#   File "ex41.py", line 6, in <module>
#     from urllib import urlopen
# ImportError: cannot import name 'urlopen'

#Traceback (most recent call last):
#  File "ex41.py", line 72, in <module>
#    random.shuffle(snippets)
#  File "/usr/lib/python3.5/random.py", line 272, in shuffle
#    x[i], x[j] = x[j], x[i]
#TypeError: 'dict_keys' object does not support indexing. -> Use list(d.keys())
# Code Change -> snippets = list(PHRASES.keys())

# cabox@Learn-Python-the-Hard-Way:~/workspace/Exercises$ python3 ex41.py
# Traceback (most recent call last):
#   File "ex41.py", line 76, in <module>
#     question, answer = convert(snippet, phrase)
#   File "ex41.py", line 53, in convert
#     result = result.replace("%%%", word, 1)
# TypeError: Can't convert 'bytes' object to str implicitly
# CodeChange: WORDS.append(word.strip().decode('utf-8'))