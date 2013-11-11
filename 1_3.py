#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Zadanie 1.3: Print, zmienne, int
# Mamy wzory skróconego mnożenia:
# http://pl.wikipedia.org/wiki/Wzory_skr%C3%B3conego_mno%C5%BCenia
# Proszę wybrać sobie jedne ze wzorów z tej strony (każdy oprócz (a+b)^2 i (a-b)^2)
# i analogicznie (jak w przykladzie nizej) go zaprezentować
# Nastepnie zamienić wartości na inne i sprawdzić czy się dobrze liczy.
# (dlaczego raz w print używany jest , raz + i dlaczego jest tam str() pozostawiam 
# do eksperymentów)
a = 1
b = 2

print "(a + b)^2 = "
print "= (" + str(a) + " + " +str(b) + ")^2 ="
print "=" , str(a) + "^2" , "+ 2*" + str(a) + "*" + str(b) , "+" , str(b) + "^2 ="
print "=", a**2 , "+" , 2*a*b , "+" , b**2 , "="
print "=", a**2 + 2*a*b + b**2


