#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Zadanie 1.4: for
# Zmienić poniższy program tak by obliczał silnie zadanej zmiennej x.
# Czyli dla zaanej wartości x chce mieć wynik x!
# np. dla x=4, wynik ma być 4!=24

x=3
silnia=1
for i in xrange(1,x):
	print "wartosc silni dla przebiegu przebiegu petli", i , "wynosi:",silnia
    silnia = silnia + i
print str(x)+"! = " + str(silnia)
