#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Person:

    def __init__(self, name, job=None, pay=0):

        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)  # call Person version

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print bob
    print sue
    print (bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print sue
    tom = Manager('Tom Jones', 'mgr', 5000)
    tom.giveRaise(0.10)
    print tom.lastName()
    print tom
