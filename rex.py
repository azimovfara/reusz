# -*- coding: utf-8 -*-

from random import randint
chislo = randint(1,5)

print (u"какое число я загадал?")
answer = raw_input("> ")
if chislo:
    print (u"правильно")
else: 
    print (u"неправильно")
