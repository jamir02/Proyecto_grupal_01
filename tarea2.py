import requests 

# Listas para la opción 3

list_ability = []
list_url_ability = []

#Listas para la opción 4

list_habitat = []
list_url_habitat = []

#Listas utilizadas
list_pokemon_selected = []
url_list_pokemon_species = []
url_list_pokemon_selected = []

def get_ability(offset = 0):
    url_ability = 'http://pokeapi.co/api/v2/ability/'

    args = {'offset': offset} if offset else {}

    response = requests.get(url_ability, params = args)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])

        if results:
            for ability in results:
                name_ability = ability['name']
                url_ability = ability['url']
                list_ability.append(name_ability)
                list_url_ability.append(url_ability)
            get_ability(offset= offset +20)

def get_ability_pokemon(url2_ability):
    response = requests.get(url2_ability)
    if response.status_code == 200:
        payload = response.json()
        pokemon = payload.get('pokemon', [])

        if pokemon:
            for ability in pokemon:
                name_pokemon = ability['pokemon']['name']
                url_pokemon = ability['pokemon']['url']
                #print(name_pokemon)
                #print(url_pokemon)
                list_pokemon_selected.append(name_pokemon)
                url_list_pokemon_selected.append(url_pokemon)

def list_pokemon(pokemon):
    pokemon_index = list_pokemon_selected.index(pokemon)
    url_pokemon = url_list_pokemon_selected[pokemon_index]
    response = requests.get(url_pokemon)
    if response.status_code == 200:
        payload = response.json()
        abilities = payload.get('abilities', [])
        sprite = payload.get('sprites',[])

        print("El nombre del pokemon es", pokemon)
        print("Las habilidades de", pokemon, "son las siguientes: ")
        if abilities:
            for ability in abilities:
                ability_pokemon = ability['ability']['name']
                print(ability_pokemon)
        print("El artwork oficial de", pokemon, "es: ")
        if sprite:
            #for sprites in sprite.values():
            sprite_pokemon = sprite['other']['official-artwork']['front_default']
            print(sprite_pokemon)

def Opcion_3 ():
    list_pokemon_selected.clear()
    url_list_pokemon_selected.clear()
    input_ability = input("Ingresa el nombre de la habilidad (Ej: torrent, infiltrator, insomnia, damp, volt-absorb): ").lower()
    while (not(input_ability in list_ability)):
        input_ability = input("Debe ingresar el nombre de una habilidad válida (Ej: torrent, infiltrator, insomnia, damp, volt-absorb): ").lower()

    print("La habilidad escogida es:", input_ability)
    print()
    ability_index = list_ability.index(input_ability)
    url2_ability = list_url_ability[ability_index]

    get_ability_pokemon(url2_ability)

    for pokemon in list_pokemon_selected:
        list_pokemon(pokemon)
        print()
    response_yn = input("¿Deseas escoger otra habilidad? [y/n]: ").lower()
    while (not(response_yn in ['y','n'])):
        response_yn = input("¿Deseas escoger otra habilidad? [y/n]: ").lower()
    if response_yn == 'y':
        Opcion_3()

def get_habitat():
    url_habitat = 'https://pokeapi.co/api/v2/pokemon-habitat/'

    response = requests.get(url_habitat)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])

        if results:
            for habitat in results:
                name_habitat = habitat['name']
                url_habitat = habitat['url']
                list_habitat.append(name_habitat)
                list_url_habitat.append(url_habitat)

def get_habitat_pokemon(url2_ability):
    response = requests.get(url2_ability)
    if response.status_code == 200:
        payload = response.json()
        pokemon = payload.get('pokemon_species', [])

        if pokemon:
            for habitat in pokemon:
                name_pokemon = habitat['name']
                url_species_pokemon = habitat['url']
                list_pokemon_selected.append(name_pokemon)
                url_list_pokemon_species.append(url_species_pokemon)

def get_pokemon():
    for pokemon_species in url_list_pokemon_species:
        response = requests.get(pokemon_species)
        if response.status_code == 200:
            payload = response.json()
            pokemon = payload.get('varieties', [])

            if pokemon:
                i=0
                for pokemon_url in pokemon:
                    if (i==0):
                        url_pokemon= pokemon_url['pokemon']['url']
                        url_list_pokemon_selected.append(url_pokemon)
                        i=i+1
                    else:
                        i=i+1
                

def Opcion_4():
    list_pokemon_selected.clear()
    url_list_pokemon_selected.clear()
    url_list_pokemon_species.clear()
    input_habitat = input("Ingresa el nombre del habitat (Ej: cave, forest, grassland, mountain, rare): ").lower()
    while (not(input_habitat in list_habitat)):
        input_habitat = input("Debe ingresar el nombre de un habitat válido (Ej: cave, forest, grassland, mountain, rare): ").lower()

    print("El habitat escogida es:", input_habitat)
    print()
    habitat_index = list_habitat.index(input_habitat)
    url2_habitat = list_url_habitat[habitat_index]

    get_habitat_pokemon(url2_habitat)
    get_pokemon()
    for pokemon in list_pokemon_selected:
        list_pokemon(pokemon)
        print()
    response_yn = input("¿Deseas escoger otro habitat? [y/n]: ").lower()
    while (not(response_yn in ['y','n'])):
        response_yn = input("¿Deseas escoger otro habitat? [y/n]: ").lower()
    if response_yn == 'y':
        Opcion_4()

get_ability()
Opcion_3()
get_habitat()
Opcion_4()

