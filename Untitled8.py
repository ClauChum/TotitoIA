#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
tablero = [' ' for _ in range(9)]
def MostrarTablero():
    F1 = '|'.join(tablero[0:3])
    F2 = '|'.join(tablero[3:6])
    F3 = '|'.join(tablero[6:9])
    print(F1)
    print('-----')
    print(F2)
    print('-----')
    print(F3)
    
def Win(jugador):
    for i in range(0, 9, 3):
        if tablero[i:i+3] == [jugador]*3:
            return True
    for i in range(3):
        if tablero[i::3] == [jugador]*3:
            return True
    if tablero[0] == jugador and tablero[4] == jugador and tablero[8] == jugador:
        return True
    if tablero[2] == jugador and tablero[4] == jugador and tablero[6] == jugador:
        return True
    return False

def movimiento(jugador):
    if jugador == 'O':
        mov = random.randint(0, 8)
    else:
        mov = int(input("Ingrese la cantidad 1-9:")) - 1
    if tablero[mov] == ' ':
        tablero[mov] = jugador
    else:
        print("casilla ocupada")
        movimiento(jugador)
        
while True:
    MostrarTablero()
    movimiento('X')
    if Win('X'):
        MostrarTablero()
        print("Ha ganado X")
        break
    MostrarTablero()
    movimiento('O')
    if Win('O'):
        MostrarTablero()
        print("Ha ganado O")
        break


# In[ ]:





# In[ ]:




