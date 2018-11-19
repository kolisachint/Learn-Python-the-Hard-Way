#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Basic Object- Oriented
# Alter Before or After

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super().altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()