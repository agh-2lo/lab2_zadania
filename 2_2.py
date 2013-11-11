#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Zadanie 2.2 : Operacje na stringach
# Do zawartości stringa mozemy dostać się podobnie jak do tablicy
# hello="hello"
# print hello[1] (wypisze 'e')
# proszę pobawić się tym mechanizmem we własnym zakresie, a następnie:
# 
# Mając tablice imion, poczyńmy założenie/obserwacje, że
# gdy imie kończ się na literę "a", to jest to imie zeńskie,
# w przeciwnym wypadku jest to imie męskie.
# Proszę zmofyfikować program w skazanym miejscu, tak by poprawnie
# rozpoznał które z imion zawartych w tablicy jest męskie, a króre
# żeńskie

imiona = ["Marek","Monika","Tomek","Alicja","Amadeusz","Anna","Xymena"]

for i in xrange(0,len(imiona)):
    if(1): #tutaj prosze wymyśleć warunek
        print imiona[i], "jest kobieta"
    else:
        print imiona[i], "jest mezczyzna"