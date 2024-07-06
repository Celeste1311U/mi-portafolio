import pandas as pd

df = pd.read_excel('tabla de radicales.xlsx')

formulas = df['formula']
radicales = df['nombreRadical']
cargas = df['cargaRadical']

# Función para obtener el nombre y la carga del radical a partir de la fórmula
def formula(df, radical):
    resultado = df[df['formula'] == radical]['nombreRadical'].values[0]
    carga = df[df['formula'] == radical]['cargaRadical'].values[0]
    return f'{radical} es {resultado} y su carga es de -{carga}'

# Función para obtener la fórmula y la carga del radical a partir del nombre
def nombreAradical(df, radical):
    resultado = df[df['nombreRadical'] == radical]['formula'].values[0]
    carga = df[df['nombreRadical'] == radical]['cargaRadical'].values[0]
    return f'{radical} es {resultado} y su carga es de -{carga}'

while True:
    radical = input('Ingresa la formula o nombre del radical: ')
    if radical in formulas.values:
        print(formula(df, radical))
    elif radical in radicales.values:
        print(nombreAradical(df, radical))
    elif radical == 'fin':
        break
    else:
        print('formula o nombre inválido')
    