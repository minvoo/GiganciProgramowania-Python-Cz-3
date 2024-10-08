# 1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 elementy
slownik = {"klucz1": 1,
           "klucz2": 2,
           "klucz3": 3}
krotka = (2,5,1)
lista = [3,0,1]
zbior = {5,3,9}

#2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów
print(len(slownik))
print(len(krotka))
print(len(lista))
print(len(zbior))

# 3. Za pomoca petli for wypisz wszystkie elementy kazdego z tych obiektow
print('ZADANIE 3')
for i in lista:
    print(i)

for i in krotka:
    print(i)

for i in zbior:
    print(i)

for i in slownik:
    print(i)

# 4. Teraz wypisz wartosci slownika zamiast kluczy
print('ZADANIE 4')
for i in slownik.values():
    print(i)

# 5. wypisz te same elementy w odwroconej kolejnosci (dla list, slownikow, zbiorow, krotek) 
print('Zadanie 5')
lista.reverse()
for i in lista:
    print(i)

skonwertowany_zbior = list(zbior)
skonwertowany_zbior.reverse()
for i in skonwertowany_zbior: 
    print(i)

for i in krotka[::-1]:   # ::-1   - odwraca indeksy
    print(i)

for i in list(slownik)[::-1]:
    print(i)
    