#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Basic Object- Oriented
# Implicit Inheritance


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()