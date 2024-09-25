import pprint
import json

game = {
    'name': 'Counter Strike',
    'release_date': 1999,
    'releaser': 'valve',
    'genre': 'fps'
}

print(game)
pprint.pprint(game)

# json.dumps()   konwersja slownika do formatu json (string)
# json.loads()   konwersja jsona (stringa) do formatu slownika
# json.dump()    zapis do pliku w formacie JSON
# json.load()    wczytanie z pliku json do naszej aplikacji
