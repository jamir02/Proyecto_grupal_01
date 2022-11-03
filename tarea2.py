import requests 

list_ability = []
list_url_ability = []
list_pokemon_selected = []
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

get_ability()
Opcion_3()


