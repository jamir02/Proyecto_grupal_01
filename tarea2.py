import requests

URL = "https://pokeapi.co/api/v2/"

# Todo 1
# Todo 2
# Todo 3
# Todo 4
# Todo 5


def get_pokemon_by_type(tipo: str):
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


def run():
    while True:
        # Todo
        tipo = input("Que tipo de pokemon quieres buscar: ")
        if tipo:
            get_pokemon_by_type(tipo)


run()
