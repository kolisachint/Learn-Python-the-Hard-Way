#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Is- A, Has- A, Objects, and Classes


## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	typename="Animal"

## Dog is-a Animal
class Dog(Animal):            # Inheritance

	def __init__(self, name):   # Object Initialisation
		## Dog has- a its own attributes as well as has- a animal attributes
		self.name = name
		self.type = "Dog"

## ??
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ??
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name

		## Person has- a pet of some kind
		self.pet = None

## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass

## ??
class Halibut(Fish):
	pass


## rover is- a Dog
rover = Dog("Rover")
print("%s is- a %s & %s is- a %s" % (rover.name,rover.type,rover.type,rover.typename))
## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

print(rover.name)
print(mary.name)
print(frank.name, frank.salary)