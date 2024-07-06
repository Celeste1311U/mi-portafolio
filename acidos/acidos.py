import pandas as pd

df = pd.read_excel('acidos.xlsx')
formula = df['formula']
tradicional = df['tradicional']
moderna = df['moderna']


def formulaAtm(acido, df):
    print('1. tradicional\n2. moderna')
    opcion = input(f'ingrese el número de la nomenclatura en la que quiere ver el elemento {acido}: ')
    while opcion not in ['1', '2']:
        print('\nopcion invalida\n')
        opcion = input(f'ingrese el número de la nomenclatura en la que quiere ver el elemento {acido}: ')
    if opcion == '1':
        resultado = df[formula == acido]['tradicional'].values[0]
        return f'el acido {acido} en nomenclatura tradicional se llama {resultado}'
    elif opcion == '2':
        resultado = df[formula == acido]['moderna'].values[0]
        return f'el acido {acido} en nomenclatura moderna se llama {resultado}'

def tradicionalAfm(acido, df):
    print('1. formula\n2. moderna')
    opcion = input(f'ingrese el número de la nomenclatura en la que quiere ver el elemento {acido}: ')
    while opcion not in ['1', '2']:
        print('\nopcion invalida\n')
        opcion = input(f'ingrese el número de la nomenclatura en la que quiere ver el elemento {acido}: ')
    if opcion == '1':
        resultado = df[tradicional == acido]['formula'].values[0]
        return f'el acido {acido} en formula se escribe {resultado}'
    elif opcion == '2':
        resultado = df[tradicional == acido]['moderna'].values[0]
        return f'el acido {acido} en nomenclatura moderna se llama {resultado}'
    

def modernaAft(acido, df):
    print('1. formula\n2. tradicional')
    opcion = input(f'ingrese el número de la nomenclatura en la que quiere ver el elemento {acido}: ')
    while opcion not in ['1', '2']:
        print('\nopcion invalida\n')
        opcion = input(f'ingrese el número de la nomenclatura en la que quiere ver el elemento {acido}: ')
    if opcion == '1':
        resultado = df[moderna == acido]['formula'].values[0]
        return f'el acido {acido} en formula se escribe {resultado}'
    elif opcion == '2':
        resultado = df[moderna == acido]['tradicional'].values[0]
        return f'el acido {acido} en nomenclatura tradicional se llama {resultado}'

while True:
    acido = input('ingrese la formula o nomenclatura tradicional o moderna del acido: ')
    if acido in formula.values:
        print(formulaAtm(acido, df))
    elif acido in tradicional.values:
        print(tradicionalAfm(acido, df))
    elif acido in moderna.values:
        print(modernaAft(acido, df))
    elif acido == 'fin':
        print('chau')
        break
    else:
        print('\nopcion invalida\n')