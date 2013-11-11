#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Zadanie 1.7: Pętla, tablica
# Proszę tak zmodyfikować ten program by:
# - tablica była inicjalizowana nie wartościami 0 ale 10. 
# - była 10cio elementowa a nie 5cio
# - proszę tak zmodyfikować linijke "tablica[i]=i"
#	by w kolejnych komórkach tablic znalazły się elementy
#	im przeciwne. 
#	Np. dla tablicy posiadającej 10 elemetnów:
#	zamist 0 ma by 10. zamist 1 ma byc 9
#	zamist 2 ma być 8, zamist 3 ma być 7...

tablica = [0]*5

for i in xrange(0,len(tablica)):
	print "tablica[" + str(i) + "] przed przypisaniem:", tablica[i]
	tablica[i]=i
	print "tablica[" + str(i) + "] po przypisaniu:", tablica[i]

print "efekt końcowy:",tablica 