def palabra_correcta(palabra_ingresada, palabra_del_dia):
    lista_verificadas = []
    for i in range(len(palabra_ingresada)):
        if palabra_ingresada[i] == palabra_del_dia[i]:
            lista_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif palabra_ingresada[i] in palabra_del_dia:
            lista_verificadas.append(f"({palabra_ingresada[i]})")
        else:
            lista_verificadas.append(f"{palabra_ingresada[i]}")
    return lista_verificadas

palabra_del_dia = "hola" 
intentos = 5
while intentos > 0:
    palabra_ingresada = input('Ingrese una palabra: ')
    if len(palabra_ingresada) == len(palabra_del_dia):
        print(palabra_correcta(palabra_ingresada, palabra_del_dia))
        if palabra_ingresada == palabra_del_dia:
            print('¡Felicidades! Has adivinado la palabra del día')
            break
        else:
            intentos = intentos - 1
            print(f'Te quedan {intentos} intentos')
            if intentos == 0:
                print('Game Over')
    else:
        print(f'Vuelva a ingresar una palabra de {len(palabra_del_dia)} letras')