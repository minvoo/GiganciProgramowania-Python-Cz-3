import json
import pprint

samochod = {
    'Marka': 'Toyota',
    'Model': 'Corolla',
    'Rok': 2020,
}

#with open('./Python/l1.json', 'r') as file:
#    spis_samochodu = json.load(file)
#    pass
#spis_samochodu['spis_samochodu'].append(samochod)
#pprint.pprint(spis_samochodu['spis_samochodu'])

samochod_as_json = json.dumps(samochod)
with open('./Lekcja 1 - zadania domowe/Szymon/samochod.json', 'w') as file:
    json.dump(samochod_as_json, file, indent = 3, sort_keys = False)

print(samochod_as_json)