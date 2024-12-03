import requests
from bs4 import BeautifulSoup
from fpdf import FPDF


def scrap_pokemon_list():
    url = "https://pokelife.pl/pokedex/index.php?title=Lista_Pokemon%C3%B3w_Kanto"
    response = requests.get(url)
    #print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    pokemons_list = []
    table  = soup.find('table', class_ = 'Tabela1')
    rows = table.find_all('tr')

    for row in rows[1:]:
        columns  = row.find_all('td')
        pokemon =  (columns[2].text[:-1], f"No.{columns[0].text[:-1]}")          # No. 001 Bulbasaur 
        pokemons_list.append(pokemon)

    pokemons_without_mega = (pokemon for pokemon in pokemons_list if "Mega " not in pokemon[0])
    return pokemons_without_mega


def get_pokemon_image(pokemon_info):
    link = pokemon_info['sprites']['front_default']
    return link

def get_pokemon_info(pokemon_name):
    pokemon_name = pokemon_name.replace('\'','')
    pokemon_name = pokemon_name.replace('. ','-')
    pokemon_name = pokemon_name.replace('♀','-f')   
    pokemon_name = pokemon_name.replace('♂', '-m')                                 
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    return response.json()

pokemon_list = scrap_pokemon_list()

for pokemon in pokemon_list:
    try:
        pokemon_info = get_pokemon_info(pokemon[0])
    except:
        print(pokemon[0])