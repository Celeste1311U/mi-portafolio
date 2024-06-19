import pandas as pd

df = pd.read_excel('Tabla de valecias.xlsx')

elementos = df['Elemento']
valencias = df['Valencias']
simbolos = df['Simbolo']

elemento = input('Ingrese su elemento: ').capitalize()
while elemento != 'Fin':

    while elemento not in elementos.values and elemento not in simbolos.values and elemento != 'Fin':
        elemento = input('Elemento inválido, ingrese su elemento: ').capitalize()

    if elemento in elementos.values:
        valencia = df[elementos == elemento]['Valencias'].values[0]
    elif elemento in simbolos.values:
        valencia = df[simbolos == elemento]['Valencias'].values[0]


    print(f'la valencia del elemento {elemento} es {valencia}')
    elemento = input('Ingrese su elemento: ').capitalize()