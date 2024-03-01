import random
import sys

acciones = ["piedra", "papel", "tijeras"]

usuario = sys.argv[1].lower()
computador = random.choice(acciones)

if usuario not in acciones:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
else:
    print(f"Tu jugaste {usuario}\nComputador jugó {computador}.")
    if usuario == computador:
        print(f"Es un empate!")
    elif usuario == "piedra":
        if computador == "tijeras":
            print("Ganaste!!")
        else:
            print("Perdiste.")
    elif usuario == "papel":
        if computador == "piedra":
            print("Ganaste!!")
        else:
            print("Perdiste.")
    elif usuario == "tijeras":
        if computador == "papel":
            print("Ganaste!!")
        else:
            print("Perdiste.")




