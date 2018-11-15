#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Modules, Classes, and Objects


class Song(object):
	dummyvar="Variable is created with default value"
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		self.dummyvar="Value is assigned dynamically when class instant is initialised"

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you",
			"I don't want to get sued",
			"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
					"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

dummyclass=Song(["Testing class instant and variables."])
print(dummyclass.dummyvar)
dummyclass.sing_me_a_song()



# Traceback (most recent call last):
#   File "ex40.py", line 26, in <module>
#     dummyclass=Song()
# TypeError: __init__() missing 1 required positional argument: 'lyrics'


# Traceback (most recent call last):
#   File "ex40.py", line 22, in <module>
#     happy_bday.sing_me_a_song()
#   File "ex40.py", line 12, in sing_me_a_song
#     for line in self.lyrics:
# AttributeError: 'Song' object has no attribute 'lyrics'