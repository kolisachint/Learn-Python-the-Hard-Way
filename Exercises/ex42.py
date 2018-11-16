#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
# Is- A, Has- A, Objects, and Classes


## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    whoami="Animal"

## Dog is- a Animal
class Dog(Animal):                          # Inheritance

    def __init__(self, name):   # Object Initialisation
        ## Dog has- a its own attributes as well as has- a animal attributes
        self.name = name
        self.whoami = "Dog"
        self.myparentname = super().whoami
#       self.myparent= Animal()             # Composition

## Cat is- a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
        self.whoami = "Cat"
        self.myparentname = super().whoami
        
## Person is-a Object
class Person(object):

    def __init__(self, name):
        ## Person has- a name 
        self.name = name

        ## Person has- a pet of some kind
        self.pet = None
        self.whoami = "Person"

## Employee is- a Person
class Employee(Person):

    def __init__(self, name, salary):
        self.salary = salary
        ## Initialisation of parent class
        super().__init__(name)
        self.myparentname = self.whoami                         # Inherited whoami
        ## All statements from parent class init is executed
        self.whoami = "Employee"                                # Assigned whoami
        
## Fish is- a Object
class Fish(object):
    whoami = "Fish"

## Salmon is- a Fish
class Salmon(Fish):
    myparentname = Fish.whoami
    whoami = "Salmon"

## Halibut is- a Fish
class Halibut(Fish):
    myparentname = Fish.whoami           # Overriding super class's static variable # Evil
    whoami = "Halibut"



## Rover is- a Dog & Dog is- a Animal
rover = Dog("Rover")
print("%s is- a %s & %s is- a %s" % (rover.name,rover.whoami,rover.whoami,rover.myparentname))

## Satan is- a Cat & Cat is- a Animal
satan = Cat("Satan")
print("%s is- a %s & %s is- a %s" % (satan.name,satan.whoami,satan.whoami,satan.myparentname))

## Mary is- a Person
mary = Person("Mary")
print("%s is- a %s " % (mary.name,mary.whoami))

## Mary has- a Cat & Cat name is- a Satan
mary.pet = satan
print("%s has- a %s & %s name is- a %s" % (mary.name,mary.pet.whoami,mary.pet.whoami,mary.pet.name))

## Frank is- a Employee & Employee is- a Person
frank = Employee("Frank", 120000)
print("%s is- a %s & %s is- a %s" % (frank.name,frank.whoami,frank.whoami,frank.myparentname))

## Frank has- a Dog & Dog name is- a Rover
frank.pet = rover
print("%s has- a %s & %s name is- a %s" % (frank.name,frank.pet.whoami,frank.pet.whoami,frank.pet.name))

## flipper is- a Fish
flipper = Fish()
print("flipper is- a %s " % (flipper.whoami))

## Salmon is- a Fish
crouse = Salmon()
print("%s is- a %s " % (crouse.whoami,crouse.myparentname))

## Halibut is- a Fish
harry = Halibut()
print("%s is- a %s " % (harry.whoami,harry.myparentname))



# Traceback (most recent call last):
#   File "ex42.py", line 83, in <module>
#     frank = Employee("Frank", 120000)
#   File "ex42.py", line 47, in __init__
#     self.myparentname = super().whoami                        # Inherited whoami
# AttributeError: 'super' object has no attribute 'whoami'
    

