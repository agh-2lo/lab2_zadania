#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Zadanie 1.5: while
# Prosze analogicznie jak wyzej, poprawić ten program tak by liczył silnie.
# Po oczywistej modyfikacji (jak wyżej) - program dalej nie będzie działał :)
# By zadziałał neleży zamienić ze sobą miejscami 2 sąsiadujące linie kodu.
# Proszę je odnaleźć, i doprowadzić do działania. Proszę zastanowić się które ;)
x = 4
silnia = 1
i = 0
while (i<x):
    print "wartosc silni dla przebiegu przebiegu petli", i , "wynosi:",silnia
    silnia = silnia * i
    i = i + 1
print str(x)+"! = " + str(silnia)