#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Basic Object- Oriented
# Override Explicitly

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
