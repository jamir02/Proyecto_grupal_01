# Tarea 2

# Programa sobre la PokeApi https://pokeapi.co/docs/v2

# Escribir un programa que tenga las siguientes opciones:
# Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.
# Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.
# Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.
# Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.
# Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.

# Nota: listar pokemons involucra: nombre, habilidad y URL de la imagen

# Se importa el paquete requests

import requests

# Se declara el URL de la version 2 de la pokeapi
URL = "https://pokeapi.co/api/v2/"

# Listas para la opcion 1

list_generations = []
list_url_generations = []

# Listas para la opcion 2

list_shapes = []
list_url_shapes = []

# Listas para la opción 3

list_ability = []
list_url_ability = []

# Listas para la opción 4

list_habitat = []
list_url_habitat = []

# Listas en comun utilizadas
list_pokemon_selected = []
url_list_pokemon_species = []
url_list_pokemon_selected = []


def get_generations():
    # Funcion que guarda el nombre de las generaciones con sus respectivos urls
    url_generation = "https://pokeapi.co/api/v2/generation/"

    response = requests.get(url_generation)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])

        if results:
            for generation in results:
                name_generation = generation["name"]
                url_generation = generation["url"]
                list_generations.append(name_generation)
                list_url_generations.append(url_generation)


def get_generation_pokemon(url2_generation):
    # Funcion encargada de guardar cada pokemon perteneciente a la generacion escogida, y sus respectivos urls
    response = requests.get(url2_generation)
    if response.status_code == 200:
        payload = response.json()
        pokemon = payload.get("pokemon_species", [])

        if pokemon:
            for generation in pokemon:
                name_pokemon = generation["name"]
                url_species_pokemon = generation["url"]
                url_pokemon = "".join(url_species_pokemon.split("-species"))
                list_pokemon_selected.append(name_pokemon)
                url_list_pokemon_selected.append(url_pokemon)


def Opcion_1():
    # Funcion encargada de listar pokemons por generación.
    list_pokemon_selected.clear()
    url_list_pokemon_selected.clear()
    # El usuario/a ingresa la generación
    input_generation = input(
        "Ingresa la generación (Ej: generation-i, generation-ii, generation-iii, generation-iv): "
    ).lower()
    # Se valida que la generación ingresada se encuentre en la lista de generaciones
    while not (input_generation in list_generations):
        input_generation = input(
            "Debe ingresar el nombre de una generación válida (Ej: generation-i, generation-ii, generation-iii, generation-iv): "
        ).lower()
    # Se imprime la generación escogida
    print("La generación escogida es:", input_generation)
    print()
    # Se extrae el url de la generación escogida
    generation_index = list_generations.index(input_generation)
    url2_generation = list_url_generations[generation_index]
    # Se procede a obtener los pokemons de la generación escogida
    get_generation_pokemon(url2_generation)
    # Se lista los pokemons de la generación escogida incluyendo su nombre, habilidades y URL de su imagen
    for pokemon in list_pokemon_selected:
        list_pokemon(pokemon)
        print()
    # Se pregunta al usuario si desea escoger otra generación
    response_yn = input("¿Deseas escoger otra generación? [y/n]: ").lower()
    while not (response_yn in ["y", "n"]):
        response_yn = input("¿Deseas escoger otra generación? [y/n]: ").lower()
    # En caso la respuesta sea afirmativa, se ejecuta nuevamente la funcion
    if response_yn == "y":
        Opcion_1()


def get_shapes():
    # Funcion que guarda el nombre de las formas de los pokemon, con sus respectivos urls
    url_generation = "https://pokeapi.co/api/v2/pokemon-shape/"

    response = requests.get(url_generation)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])

        if results:
            for shapes in results:
                name_shape = shapes["name"]
                url_shape = shapes["url"]
                list_shapes.append(name_shape)
                list_url_shapes.append(url_shape)


def get_shape_pokemon(url2_shape):
    # Funcion encargada de guardar cada pokemon perteneciente a la forma escogida, y sus respectivos urls
    response = requests.get(url2_shape)
    if response.status_code == 200:
        payload = response.json()
        pokemon = payload.get("pokemon_species", [])

        if pokemon:
            for shape in pokemon:
                name_pokemon = shape["name"]
                url_species_pokemon = shape["url"]
                url_pokemon = "".join(url_species_pokemon.split("-species"))
                list_pokemon_selected.append(name_pokemon)
                url_list_pokemon_selected.append(url_pokemon)


def Opcion_2():
    # Funcion encargada de listar pokemons por forma.
    list_pokemon_selected.clear()
    url_list_pokemon_selected.clear()
    input_shape = input(
        "Ingresa la forma (Ej: ball, squiggle, fish, arms, blob, upright): "
    ).lower()
    while not (input_shape in list_shapes):
        input_shape = input(
            "Debe ingresar el nombre de una forma válida (Ej: ball, squiggle, fish, arms, blob, upright): "
        ).lower()

    print("La forma escogida es:", input_shape)
    print()

    shape_index = list_shapes.index(input_shape)
    url2_shape = list_url_shapes[shape_index]

    get_shape_pokemon(url2_shape)

    for pokemon in list_pokemon_selected:
        list_pokemon(pokemon)
        print()
    response_yn = input("¿Deseas escoger otra forma? [y/n]: ").lower()
    while not (response_yn in ["y", "n"]):
        response_yn = input("¿Deseas escoger otra forma? [y/n]: ").lower()
    if response_yn == "y":
        Opcion_2()


def get_ability(offset=0):
    # Funcion que guarda el nombre de las habilidades de los pokemons, con sus respectivos urls. Existe un offset debido a que
    # en cada pagina solo muestra un máximo de 20 pokemon por habilidad
    url_ability = "http://pokeapi.co/api/v2/ability/"

    args = {"offset": offset} if offset else {}

    response = requests.get(url_ability, params=args)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])

        if results:
            for ability in results:
                name_ability = ability["name"]
                url_ability = ability["url"]
                list_ability.append(name_ability)
                list_url_ability.append(url_ability)
            get_ability(offset=offset + 20)


def get_ability_pokemon(url2_ability):
    # Funcion encargada de guardar cada pokemon perteneciente a la habilidad escogida, y sus respectivos urls
    response = requests.get(url2_ability)
    if response.status_code == 200:
        payload = response.json()
        pokemon = payload.get("pokemon", [])

        if pokemon:
            for ability in pokemon:
                name_pokemon = ability["pokemon"]["name"]
                url_pokemon = ability["pokemon"]["url"]
                list_pokemon_selected.append(name_pokemon)
                url_list_pokemon_selected.append(url_pokemon)


def list_pokemon(pokemon):
    # Funcion encargada de listar los pokemons por nombre, habilidades y url de su imagen (artwork)
    pokemon_index = list_pokemon_selected.index(pokemon)
    url_pokemon = url_list_pokemon_selected[pokemon_index]
    response = requests.get(url_pokemon)
    if response.status_code == 200:
        payload = response.json()
        abilities = payload.get("abilities", [])
        sprite = payload.get("sprites", [])

        print("El nombre del pokemon es", pokemon)
        print("Las habilidades de", pokemon, "son las siguientes: ")
        if abilities:
            for ability in abilities:
                ability_pokemon = ability["ability"]["name"]
                print(ability_pokemon)
        print("El artwork oficial de", pokemon, "es: ")
        if sprite:
            # for sprites in sprite.values():
            sprite_pokemon = sprite["other"]["official-artwork"]["front_default"]
            print(sprite_pokemon)


def Opcion_3():
    # Funcion encargada de listar pokemons por habilidad.
    list_pokemon_selected.clear()
    url_list_pokemon_selected.clear()
    input_ability = input(
        "Ingresa el nombre de la habilidad (Ej: torrent, infiltrator, insomnia, damp, volt-absorb): "
    ).lower()
    while not (input_ability in list_ability):
        input_ability = input(
            "Debe ingresar el nombre de una habilidad válida (Ej: torrent, infiltrator, insomnia, damp, volt-absorb): "
        ).lower()

    print("La habilidad escogida es:", input_ability)
    print()
    ability_index = list_ability.index(input_ability)
    url2_ability = list_url_ability[ability_index]

    get_ability_pokemon(url2_ability)

    for pokemon in list_pokemon_selected:
        list_pokemon(pokemon)
        print()
    response_yn = input("¿Deseas escoger otra habilidad? [y/n]: ").lower()
    while not (response_yn in ["y", "n"]):
        response_yn = input("¿Deseas escoger otra habilidad? [y/n]: ").lower()
    if response_yn == "y":
        Opcion_3()


def get_habitat():
    # Funcion que guarda el nombre de los habitats de los pokemons, con sus respectivos urls
    url_habitat = "https://pokeapi.co/api/v2/pokemon-habitat/"

    response = requests.get(url_habitat)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])

        if results:
            for habitat in results:
                name_habitat = habitat["name"]
                url_habitat = habitat["url"]
                list_habitat.append(name_habitat)
                list_url_habitat.append(url_habitat)


def get_habitat_pokemon(url2_ability):
    # Funcion encargada de guardar cada especie de pokemon perteneciente al habitat escogida, y sus respectivos urls
    response = requests.get(url2_ability)
    if response.status_code == 200:
        payload = response.json()
        pokemon = payload.get("pokemon_species", [])

        if pokemon:
            for habitat in pokemon:
                name_pokemon = habitat["name"]
                url_species_pokemon = habitat["url"]
                list_pokemon_selected.append(name_pokemon)
                url_list_pokemon_species.append(url_species_pokemon)


def get_pokemon():
    # Funcion encargada de guardar cada pokemon perteneciente al habitat escogida, y sus respectivos urls
    for pokemon_species in url_list_pokemon_species:
        response = requests.get(pokemon_species)
        if response.status_code == 200:
            payload = response.json()
            pokemon = payload.get("varieties", [])

            if pokemon:
                i = 0
                for pokemon_url in pokemon:
                    if i == 0:
                        url_pokemon = pokemon_url["pokemon"]["url"]
                        url_list_pokemon_selected.append(url_pokemon)
                        i = i + 1
                    else:
                        i = i + 1


def Opcion_4():
    # Funcion encargada de listar pokemons por habitat.
    list_pokemon_selected.clear()
    url_list_pokemon_selected.clear()
    url_list_pokemon_species.clear()
    input_habitat = input(
        "Ingresa el nombre del habitat (Ej: cave, forest, grassland, mountain, rare): "
    ).lower()
    while not (input_habitat in list_habitat):
        input_habitat = input(
            "Debe ingresar el nombre de un habitat válido (Ej: cave, forest, grassland, mountain, rare): "
        ).lower()

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
    while not (response_yn in ["y", "n"]):
        response_yn = input("¿Deseas escoger otro habitat? [y/n]: ").lower()
    if response_yn == "y":
        Opcion_4()


def get_pokemon_by_type(tipo: str):
    # Funcion encargada de listar pokemons por tipo.
    foo = f"{URL}type/{tipo}"
    response = requests.get(foo)
    if response.status_code == 200:
        response = response.json()
        # print(response.json())
        moves = [move["name"] for move in response["moves"]]
        pokemon_list = [pokemon["pokemon"] for pokemon in response["pokemon"]]
        print(f"nombres de {len(pokemon_list)} pokemon de tipo {tipo}: ")
        for pokemon in pokemon_list:
            print(f"{pokemon['name']} - {pokemon['url']}")
        print(f"habilidades de pokemons de tipo {tipo}: ")
        for move in moves:
            print(move)
    else:
        print("Tipo de pokemon no encontrado")


def Opcion_5():
    # Funcion encargada de consultar al usuario sobre el tipo de pokemon a buscar
    tipo = input("Que tipo de pokemon quieres buscar (grass, poison, fire, water): ")
    if tipo:
        get_pokemon_by_type(tipo)


def run():
    # Funciones a inicializar:
    get_generations()
    get_ability()
    get_habitat()
    get_shapes()
    # Interfaz  de usuario
    while True:
        print(
            "\nEstimado Usuario/a, por favor escoja una de las siguientes opciones:\n"
        )
        print("Opción 1: Listar pokemons por generación")
        print("Opción 2: Listar pokemons por forma")
        print("Opción 3: Listar pokemons por habilidad")
        print("Opción 4: Listar pokemons por habitat")
        print("Opción 5: Listar pokemons por tipo")
        print("Opción 6: Salir")

        opcion = input("\nElija una opción (1,2,3,4,5 o 6): ")

        while not (opcion in ["1", "2", "3", "4", "5", "6"]):
            opcion = input("Por favor, escoja una opción (1,2,3,4,5 o 6): ")

        if opcion == "1":
            Opcion_1()
        elif opcion == "2":
            Opcion_2()
        elif opcion == "3":
            Opcion_3()

        elif opcion == "4":
            Opcion_4()

        elif opcion == "5":
            Opcion_5()

        elif opcion == "6":
            break


run()
