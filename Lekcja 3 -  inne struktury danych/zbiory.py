######################## ZBIORY (set) ###################

slownik = {"klucz": 1, "klucz2" : 2} # para: klucz:wartosc
zbior = {1,2,3,4,1} #same wartosci
print(f'Zbior: {zbior}')

#dodawanie czegos do zbioru
zbior.add('4')
print(zbior)

#usuwanie - remove()
zbior.remove(1)  ### jezeli element nie istnieje to mamy blad
print(zbior)

#usuwanie - discard()
zbior.discard(2) ### jezeli element nie istnieje, to po prostu nic nie usunie
print(zbior)

#usuwnie LOSOWEGO elementu ze zbioru - pop() I ZWROCENIE GO 
print(zbior)
usuniety = zbior.pop()

print(usuniety)

### clear() - czyszczenie zbioru
zbior.clear()
print(zbior)

pusty_zbior = set()
## union()
zbior1 = {1,2,3}
zbior2 = {4,5,6}
zlaczony_zbior = zbior1.union(zbior2)
print(zlaczony_zbior)

## issubset() - czy dany zbior jest podzbiorem innego zbioru 
wyrazenie = zbior1.issubset(zbior2)

if wyrazenie:
    print('Huraaa')

