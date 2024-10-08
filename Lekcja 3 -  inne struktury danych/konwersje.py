zbior = {1,2,3}
krotka = (4,5,6)
lista = [7,8,8,9]

# konwersja zbioru na liste
print(list(zbior))
# konwersja krotki na liste
print(list(krotka))

#konwersja zbioru na krotke
print(tuple(zbior))
#konwersja listy na krotke
print(tuple(lista))

# konwersja krotki na zbior
print(set(krotka))

# konwersja listy na z zbior
print(set(lista))