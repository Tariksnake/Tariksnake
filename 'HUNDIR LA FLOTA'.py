'HUNDIR LA FLOTA'
from calendar import c
from os import system
import random
import time
import numpy as np
import pandas as pd



print("""
                                                                                             
.--. .--.                                            .--.                    ,-----.                                 
!  ! !  !                      ,--. ,--.             |  |                    !  ,_,!,--.           ,--.            
|  |_|  | ,--.,--. ,--,--,   ,-|  | `--' ,--.--.     |  |       .,--,--.     |  !-. |  |  ,---.  ,-'  '-.  ,--,--. 
|   _   | |  ||  | |      \ ' .-. | ,--. |  .--'     |  |      / ,-.   |     |  !-/ |  | | .-. | '-.  .-' ' ,-.  | 
|  | |  | '  ''  ' |  ||  | \ `-' | |  | |  |        |  |----. \ '-'   |     |  !   |  | ' '-' '   |  |   \ '-'  | 
`--' `--'  `----'  `--''--'  `---'  `--' `--'        `_______.  `--`--'      `--'   `--'  `---'    `--'    `--`--'                                                                                                                                                                                                                                                                                                   
                                                                                                                          
                                                                                                                           """)

time.sleep(2)
nombre = 'maquina'
nombre = input('BIENVENIDO A HUNDIR LA FLOTA, INGRESE SU NOMBRE DE JUGADOR:')
print('Gracias', nombre, 'que de comienzo el juego!!!')


'''
4 barcos de 1 posición de eslora
3 barcos de 2 posiciones de eslora
2 barcos de 3 posiciones de eslora
1 barco de 4 posiciones de eslora
'''

def poner_barco(eslora, contador, tablero):
    while contador > 0:
    
        orientacion = random.choice(["N", "S", "E", "O"])

        
        posicion = np.random.randint(9, size=2)
        fila = posicion[0]
        col = posicion[1]

        '''
        Recogemos los puntos cardinales y los asignamos a estas 4 posiciones. 
        Si os fijais podreis observar que  cuando nos referimos al sur, ya que es la direccion,
        es fila + eslora y por consguiene el este que se identifican,
        y a su vez el norte es fila - eslora, por la misma razon que la anterior, la dirección. En este caso también el oeste se identifica.
        '''

        norte = tablero[fila:fila - eslora: -1, col]  
        este = tablero[fila, col:col + eslora]
        sur = tablero[fila:fila + eslora, col]
        oeste = tablero[fila, col: col - eslora:-1]

        # Compruebo norte
        if (orientacion == "N") and (len(norte) == eslora) and ("O" not in norte):
            tablero[fila:fila - eslora:-1, col] = "O"
            contador = contador - 1


        # Compruebo este

        elif (orientacion == "E") and (len(este) == eslora) and ("O" not in este):
            tablero[fila, col:col + eslora] = "O"
            contador = contador - 1


        # compruebo Sur

        elif (orientacion == "S") and (len(sur) == eslora) and ("O" not in sur):
            tablero[fila:fila + eslora, col] = "O"
            contador = contador - 1

        # Compruebo Oeste
        elif (orientacion == "O") and (len(oeste) == eslora) and ("O" not in oeste):
            tablero[fila, col: col - eslora:-1] = 'O'
            contador = contador - 1

    return tablero

def creartablero():
    return np.full(fill_value = ' ', shape = (10, 10))


tablero_player = creartablero()
tablero_player_shots = creartablero()
tablero_machine = creartablero()
tablero_machine_shots = creartablero()

'''
A continuacion viene mostrado los contadores de shots de cada jugador, el player o la machine. 
¿ Quien ganará?
'''

contador_player = 0
contador_machine = 0

#False es el ordenador y True es el ordenador
tipo_jugador = False

#Mensaje de inicio

print("Introduce fila y columna para acabar con los barcos del enemigo. Por cada acierto se repite el disparo hasta que falles. Victoria con 20 aciertos. Suerte!")


'''
Ponemos un while del contador de los jugadores, 
el bucle seguirá ejecutandose hasta que alguno de los contadores llegue a 20, 
por lo que esta cifra es el sumatorio de las posiciones de los barcos de cada jugador.
'''

while contador_player < 20 and contador_machine < 20:

    # turno player
    if tipo_jugador == False:

        try:
            x = int(input("Elige un numero de fila entre 0 y 9: "))
            y = int(input("Elige un numero de columna entre 0 y 9: "))

            if tablero_machine[x, y] == "O":
                tablero_player_shots[x, y] = "X"
                tablero_machine[x, y] = "X"
                contador_player += 1
                print("Tocado!!\nTablero de shots del player\n", nombre)
                print(tablero_player_shots)
                print('Tablero del player')
                print(tablero_player)

            elif tablero_machine[x, y] == " ":
                tablero_player_shots[x, y] = "-"
                tablero_machine[x, y] = "-"
                tipo_jugador = False
                print("Al agua!!\nTablero de shots del player \n", nombre)
                print(tablero_player_shots)
                print('Tablero del player')
                print(tablero_player)
            elif  tablero_machine[x] == 0000:                  #Condicion para dar al jugador la opción de terminar la partida
                print('GAME OVER!!!')
            else:
                tipo_jugador = False
                print("Ya has eligido esta coordenada...\nTablero de shots del player \n", nombre)
                print(tablero_player_shots)
                print('Tablero del player')
                print(tablero_player)

        except (NameError, ValueError, IndexError):
            print("----Tienes que eligir un numero entero entre 0 y 9. Intentalo de nuevo.----")
            continue



    # turno de machine
    elif tipo_jugador == True:

        # disparo de forma aleatoria
        x2 = random.randint(0, 9)
        y2 = random.randint(0, 9)

        if tablero_player[x2, y2] == "O":
            tablero_machine_shots[x2, y2] = "X"
            tablero_player[x2, y2] = "X"
            contador_machine += 1
            time.sleep(0.5)
            print("Machine ha dado uno de tus barcos!!\nTablero de barcos del player\n", nombre)
            print(tablero_player_shots)

        elif tablero_player[x2, y2] == " ":
            tablero_machine_shots[x2, y2] = "-"
            tablero_player[x2, y2] = "-"
            tipo_jugador = True
            time.sleep(0.5)
            print("Machine ha disparado al agua!\n", "Tablero de disparos del player \n",nombre)
            print(tablero_player_shots)
        else:
            tipo_jugador = True
            time.sleep(0.5)
            print("El ordenador le ha vuelto a dar a la misma coordenada... \nTablero de disparos del player\n", nombre)
            print(tablero_player_shots)


if contador_player > contador_machine:
    print("Has ganado a Machine! Enhorabuena!!")
elif contador_machine > contador_player:
    print("Has perdido! Machine te ha vencido")





