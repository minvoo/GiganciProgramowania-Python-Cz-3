##### METODY LIST #####

#tworzenie listy 
przykladowa_lista = [1,1,"pieski", 2,3,"pieski",2]
print(przykladowa_lista)

## dodawanie do listy - metoda append()
przykladowa_lista.append("cokolwiek")
print(przykladowa_lista)

## poszerzanie listy o dowolny element, po ktorym mozna iterowac - extend()
#innymi slowy - mozna dodawac kilka elementow na raz
przykladowa_lista.extend(["pies", 3.14, "pi"])
print(przykladowa_lista)

## wstawianie elementu do listy w dowolnym miejscu - insert()
przykladowa_lista.insert(2, "giganci")
print(przykladowa_lista)

## usuwanie elementu z listy - remove()
przykladowa_lista.remove("giganci")
print(przykladowa_lista)


## usuwanie elementu z listy - ale na podstawie indeksu - pop()
przykladowa_lista.pop(0)
print(przykladowa_lista)

# zwracanie indeksu pierwszego wystpienia elementu w liscie - index()
pierwszy_indeks = przykladowa_lista.index("pieski")
print(pierwszy_indeks)

# zwracanie liczby wystpien elementu w liscie - count()
ile_pieskow = przykladowa_lista.count("pieski")
print(ile_pieskow)

#odwracanie listy - reverse()
print('Oryginalna lista')
print(przykladowa_lista)
przykladowa_lista.reverse()
print('Odwrocona lista')
print(przykladowa_lista)

# kopiowanie listy - copy()
skopiowana_lista = przykladowa_lista.copy()
print(skopiowana_lista)
skopiowana_lista.append(666) ## pozniej mozemy wykonywac operacje tylko na tej skopiownej liscie
#bez ingerencji w oryginalny byt
print(skopiowana_lista)
print(przykladowa_lista)

## czyszczenie listy - clear()
print(f'Rozmiar listy skopiowanej przed usunieciem: {len(skopiowana_lista)}')
skopiowana_lista.clear()
print(f'Skopiowana lista {skopiowana_lista}')
print(f'Rozmiar skopiowanej listy po usunieciu wszystkiego za pomoca clear: {len(skopiowana_lista)}')