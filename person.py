# ! /usr/bin/env python
# Clase Person

class Person:


    def __init__(self, name, job=None, pay=0):
        self.name = name #  atributo nombre
        self.job = job #  atributo trabajo
        self.pay = pay #  atributo sueldo
# lo que se va a ejecutar cuando >>> python person.py


if __name__ == '__main__':
    # test

    martin = Person('Martin Noblia')
    sue = Person('Sue Jones', job='dev', pay = 10000)
    print martin.name, martin.pay
    print sue.name , sue.pay

