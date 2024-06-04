import periodictable as pt

def isoelectronico():
    global nombre, z, proton, protonprint2, resultado  # Definimos estas variables como globales para que sean accesibles fuera de la función
    elementos_dict = {}
    for elemento in pt.elements:
        elementos_dict[elemento.symbol] = elemento.number
    #creamos una variable que guardará la respuesta del input y separará el string por sus espacios
    compuesto = input('Ingrese el elemento y cuantos protones ganó o perdió (con espacios por favor): ').capitalize()
    compuestin = compuesto.split(' ')
    #definimos el nombre del elemento que será la primera posición
    nombre = compuestin[0]

    #definimos si gana o pierde protones y también si no sufre cambios
    if len(compuestin) > 1:
        proton = compuestin[1]
    else:
        proton = '0'
        protonprint2 = ""

    #guardamos el nombre del elemento en z gracias al diccionario que vimos anteriormente
    if nombre in elementos_dict:
        z = elementos_dict[nombre]

    #acá invertimos el signo y quitamos el espacio de la variable protón ya creada anteriormente
    if '+' in proton:
        print(f'\n{compuesto} es un cation\n')
        proton = proton.replace('+', '-')
        protonprint2 = proton.replace('-', '')
        proton = int(proton)
    elif '-' in proton:
        print(f'\n{compuesto} es un anion\n')
        proton = proton.replace('-', '+')
        protonprint2 = proton.replace('+', '')
        proton = int(proton)
    else:
        protonprint2 = '0'
        proton = int(proton)
    z = int(z)

    resultado = z + proton

    #acá ponemos si ganó o perdió protones
    if proton > 0:
        protonprint = 'obtuvo'
    elif proton < 0:
        protonprint = 'perdio'
    else:
        protonprint = 'no ganó ni perdió protones'

    #imprimimos en pantalla el resultado
    print(f'El elemento {nombre} tuvo {z} protones y {protonprint} {protonprint2}, tiene {resultado} protones')
    isoincognita(elementos_dict, nombre, resultado)

def isoincognita(elementos_dict, nombre, resultado):
    z2 = 0  # Inicializamos z2
    isoincognita = input(f'Ingrese el elemento con el que {nombre} es isoelectrónico y cuantos protones ganó o perdió (con espacios por favor): ').capitalize()
    isoincognitin = isoincognita.split(' ')
    nombre2 = isoincognitin[0]

    if len(isoincognitin) > 1:
        protonI = isoincognitin[1]
    else:
        protonI = '0'
        protonprint2 = ""

    if nombre2 in elementos_dict:
        z2 = elementos_dict[nombre2]
    protonprint3 = ""
    if '+' in protonI:
        protonI = protonI.replace('+', '-')
        protonprint3 = protonI.replace('-', '')
        protonI = int(protonI)
    elif '-' in protonI:
        protonI = protonI.replace('-', '+')
        protonprint3 = protonI.replace('+', '')
        protonI = int(protonI)
    else:
        protonprint3 = '0'
        protonI = int(protonI)
    z2 = int(z2)

    resultado2 = z2 + protonI

    if resultado2 == resultado:
        print(f'El elemento {nombre2} con {protonprint3} protones es isoelectrónico con {nombre} con {protonprint3} protones.')
    else:
        diferencia = resultado - resultado2
    if diferencia > 0:
      incognita = resultado - resultado2
      print(f'El Z de {nombre2} es {z2 + incognita} por lo que es el elemento {pt.elements[z2 + incognita].symbol}')
      print(f'\n{pt.elements[z2 + incognita].symbol} {isoincognitin[1]} es un cation')
    else:
      incognita = resultado2 - resultado
      print(f'El Z de {nombre2} es {z2 - incognita} por lo que es el elemento {pt.elements[z2 - incognita].symbol}')
      print(f'\n{pt.elements[z2 - incognita].symbol} {isoincognitin[1]} es un anion')


isoelectronico()