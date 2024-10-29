student = {
    'name': 'Jan',
    'surname': 'Kowalski',
    'age': 15,
    'courses': ['polish, english, IT, geography'], 
}
game = {
    'name': 'Counter Strike',
    'release_date': 1999,
    'releaser': 'valve',
    'genre': 'fps'
}
# para klucz: wartosc,
# pair: key: value

### pobierane danych ze slownika ###
# sposob 1 
name = game['name']
print(name) #CS
print(game['name']) #CS
# sposob 2
print(type(game.get('name'))) #CS

### iterowanie po wartosciach slownika ###
for value in game.values():
    print(value)

### iterowanie po kluczach slownika ###
for key in game.keys():
    print(key)

### iterowanie po parach (klucz: wartosc)
for para in game.items():
    print(para)

### dodawanie do slownika ###
game.setdefault("PEGI", 18)

print(game)

### usuwanie ze slownika - konkretnej wartosci pod kluczem ###
deleted = game.pop("name")
print(game)
print('deleted value: ' + deleted)


### usuwanie ze slownika - ostatniej pozycji w tym slowniku ###
game.popitem()
print(game)

### usuwanie na podstawie klucza - inny sposob ###
del game["genre"]
print(game)

### usuwanie wszystkiego ze slownika ###
game.clear()
print(game)