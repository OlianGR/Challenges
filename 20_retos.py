"""
Ejercicio
"""

import requests

response = requests.get("https://moure.dev")
if response.status_code == 200:
    print(response.text)
else:
    print(f"Eror con codigo {response.status_code} al realizar la peticion")

"""
Extra
"""
pokemon = input("Introduce un nombre o numero del Pokémon a buscar: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json()
    print(f"Nombre: ", data["name"])
    print(f"ID: ", data["id"])
    print(f"Peso: ", data["weight"])
    print(f"Altura: ", data["height"])
    print("Tipo(s):")
    for type in data["types"]:
        print(type["type"]["name"])

    print("Juegos: ")

    for game in data["game_indices"]:
        print(game["version"]["name"])

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        response = requests.get(url)

        if response.status_code ==200:
            data = response.json()
            
            print("Cadena de evolucion: ")

            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data: 
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])

    else:
        print(f"Error {response.status_code} al encontrar las evoluciones")


else:
    print("Pokemon no encontrado")





