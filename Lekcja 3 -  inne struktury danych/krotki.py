# deklaracja krotki (tuple)
krotka = (4,2,11,2,4)
krotka_jednoelementowa = (4,)
print(krotka)
#print(krotka_jednoelementowa)

#pobieranie wycinka krotki
wycinek = krotka[1:4]   # wycinek to tak na prawde nadal tuple
print(wycinek)  #pobieranie np od indeksu pierwszego do czwartego WLACZNIE

#wyswietlenie konkretnego elementu z krotki
liczba  = krotka[2]  # tutaj ta liczba to juz nie jest krotka (tuple) tylko konkretny element z tej krotki
# w tym wypadku liczba (int)
print(liczba)

###### METODY KROTEK##### 
# count, index
# count() - zliczanie ilosci elementow w krotce
ilosc = krotka.count(11)
print(f'Ilosc liczby 11 w krotce: {ilosc}')

# index()  - pobranie pierwszego elementu o podanej wartosci 
pierwszy_indeks = krotka.index(2)
print(f'Pierwszy indeks pod jakim znajduje sie liczba 2 to {pierwszy_indeks}')