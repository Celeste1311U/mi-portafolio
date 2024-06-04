#importamos la librería periodictable como pt para no poner su nombre entero a la hora de programar
import periodictable as pt

#definimos un diccioneario en el que se guardan los simbolos de los elementos y los pasa a su número atómico o Z

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
    proton = 0
    protonprint2 = ""

#guardamos el nombre del elemento en z gracias al diccionario que vimos anteriormente

if nombre in elementos_dict:
    z = elementos_dict[nombre]

#acá invertimos el signo y quitamos el espacio de la variable protón ya creada anteriormente

if '+' in str(proton):
    print(f'\n{compuesto} es un cation\n')
    proton = proton.replace('+', '-')
    protonprint2 = proton.replace('-', ' ')
    proton = int(proton)
elif '-' in str(proton):
    print(f'\n{compuesto} es un anion\n')
    proton = proton.replace('-', '+')
    protonprint2 = proton.replace('+', ' ')
    proton = int(proton)
z = int(z)

resultado = z + proton

#acá ponemos si ganó o perdió protones

if proton > 0:
    protonprint = 'obtuvo'
elif proton < 0:
    protonprint = 'perdió'
else:
    protonprint = 'no ganó ni perdió protones'

#imprimimos en pantalla el resultado

print(f'El elemento {nombre} tuvo {z} protones y {protonprint}{protonprint2}, tiene {resultado} protones')