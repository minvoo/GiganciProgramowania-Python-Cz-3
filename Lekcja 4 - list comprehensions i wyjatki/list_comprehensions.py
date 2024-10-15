#  Definicja - jak to wlasciwie wyglada 
# [expression for item in iterable if condition]
# expression - operacj lub wartosc, ktora bedzie zastosowana dla kazdego elementu listy
# item - pojedynczy element listy 
# iterable - sekwencja po ktorej sie iterujemy (czyli przechodzimy petla np for) -
# moga to byc listy, krotki, set-y, slowniki, zakresy (range(10))
# condition - OPCJONALNY warunek ktory zostanie zastosowany na petli i po spelnieniu tego
# warunku wykona sie dopiero ten expression
# 

### PRZYKLAD ### 
lista = [1,2,3,4,5,6,7,8,9,10]
# 1 * 1 = 1 
# 2 * 2 = 4    **2 
# 3 * 3 = 9
kwadraty = [item*item for item in lista]  #kwadraty sa typu lista
# item - pojedynczy element
# item**2 - expression czyli item podniesiony do kwadratu
# lista - iterable (element po ktorym sie iterujemy czyli przechodzimy za pomoca petli, np for)
print(kwadraty)

###  SCIAGA   ###
zbior = {1,2,3,2} #brak dostepu do indeksu, nie przechowuje duplikatow 
krotka = (4,5,6) 
lista = [7,8,8,9] # mozemy przechowywac duplikaty

kwadraty = {item*item for item in lista}  # kwadraty sa zbiorem
print(kwadraty)
kwadraty = (item*item for item in lista) # kwadraty to krotka 
print(kwadraty)



### list comprehensions z warunkiem 
lista = [1,2,3,4,5,6,7,8,9,10]
kwadraty = [i*i for i in lista if i%2 != 0]
print(kwadraty)

### metoda zip 

panstwa = ['Polska', 'Niemcy', 'Francja', 'Hiszpania']
stolice = ['Warszawa', 'Berlin', 'Paryz', 'Madryt']

# Warszawa jest stolica kraju: Polska
# Berlin jest stolica kraju: Niemcy
# itd.

informacje = [f'{stolica} jest stolica kraju: {panstwo}' for panstwo, stolica in zip(panstwa, stolice)]

for i in informacje:
    print(i)

