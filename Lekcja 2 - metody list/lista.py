

przykladowa_lista = [
    "lista", #0
    111, #1 
    {"llala": 11}, #2
]
## 
# 1. listy moga zawierac elementy dowolnego typu
# 2. mozemy zmieniac dlugosc listy 
# 3. mozemy elementy w danej liscie czyli np. #0 jest typu string, to mozemy go zmienic na int

print(przykladowa_lista[1])


## Zadanie rozgrzewkowe.

## Napisz program w którym stworzysz listę z 10 liczbami, a następnie wypiszesz co drugą z nich.
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(len(lista)):
    if i % 2 != 0:
        print(lista[i])

