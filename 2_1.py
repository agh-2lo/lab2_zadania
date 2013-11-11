#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Zadanie 2.1: Pętla, tablica, element pierwszy i ostatni tablicy
# Mamy program który na wejściu przyjmuje tablice.
# a na wyjsciu zwraca tablice w której każdy element jest sumą 
# elementu i elementu po nim następującego.
# Np. dla [1,2,3,4]
# dostaniemy [1+2,2+3,3+4,4]
# Problematyczny jest tutaj element ostatni gdyż nic po nim nie następuje.
#
# Prosze tak zmodyfikować ten program by dodatkowo sumować element poprzedzajacy
# element i. Czyli zamiast
# Np. dla. [1,2,3,4,5]
# Dostaniemy [1+2,1+2+3,2+3+4,3+4+5,4+5]
#
# Wskazówki: 
# - należy dopisać jeszcze jeden warunek od if-a (korzystając z 'elif')
#	by uwzględnić teraz problematyczny element 'zerowy' (o indeksie zero)
# - należy zmodyfikować sposób dodawanie elementów tak by jeszcze uwzględnić
#	poprzedzający



wejscie = [1,2,3,4,5,6,7,9]
wyjscie = [0]*len(wejscie)

for i in xrange(0,len(tablica)):
	if i==len(tablica)-1:
		wyjscie[i]=wejscie[i]
	else:
		wyjscie[i]=wejscie[i]+wejscie[i+1]

print "efekt końcowy:",tablica 
