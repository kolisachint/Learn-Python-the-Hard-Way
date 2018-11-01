#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# More Files
# Usage: python3 ex17.py ../Files/file2.txt ../Files/file3.txt

from sys import argv
from os.path import exists

script, from_file, to_file= argv

print("Copying content of the file from %s to %s" % (from_file,to_file))

print("Input file exists: %s" % exists(from_file))
print("Output file exists: %s" % exists(to_file))
print("Do you want to still continue: ")
print("Ready, hit RETURN to continue, CTRL- C to abort:")
input()

in_file=open(from_file,'r')
indata= in_file.read()

out_file=open(to_file,'w')
out_file.write(indata)

in_file.close()
out_file.close()

