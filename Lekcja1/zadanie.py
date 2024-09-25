import json
import pprint

gra = {
    'name': 'Counter Strike',
    'release_date': 1999,
    'releaser': 'valve',
    'genre': 'fps'
}


### wczytywanie słownika
with open("l1.json","r" ) as file:
    spis_gier = json.load(file)
spis_gier["spis_gier"].append(gra) #dopisujemy cos do slownika
pprint.pprint(spis_gier["spis_gier"])


#zapisywanie słownika do innego pliku
with open("l1_2.json", "w") as file:
   json.dump(spis_gier, file,  indent = 4, sort_keys = True)


#łączenie słowników
dict1 = {"a" : 4, "b": 3}
dict2 = {"c" : 1, "d": 2}
dict3 = {**dict1, **dict2} # 3.5
dict4 = dict1 | dict2 # 3.9
print(dict3)
print(dict4)