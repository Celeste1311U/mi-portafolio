import pandas as pd

df = pd.read_excel('Hidroxidos.xlsx')
formulas = df['Formula']
tradicionales = df['Tradicional']
modernas = df['Moderna']

def formula(df):
  hidroxido = input('\nIngrese la formula del hidroxido: ')
  while hidroxido not in df['Formula'].values:
    print('\nFormula no valida\n')
    hidroxido = input('\nIngrese la formula del hidroxido: ')
  print('\nElija en qué nomenclatura quiere ver el hidroxido\n1. Moderna\n2. Tradicional\n')
  operacion = input('\n')
  if operacion == '1':
    return df[df['Formula'] == hidroxido]['Moderna'].values[0]
  elif operacion == '2':
    return df[df['Formula'] == hidroxido]['Tradicional'].values[0]
  while operacion not in ['1', '2']:
    print('\nOpcion no valida, ingrese 1 o 2\n')
    operacion = input('\n')

def moderna(df):
  hidroxido = input('\nIngrese la nomenclatura moderna del hidroxido: ')
  while hidroxido not in df['Moderna'].values:
    print('\nNomenclatura no valida\n')
    hidroxido = input('\nIngrese la nomenclatura moderna del hidroxido: ')
  print('\nElija en qué nomenclatura quiere ver el hidroxido\n1. Formula\n2. Tradicional\n')
  operacion = input('\n')
  if operacion == '1':
    return df[df['Moderna'] == hidroxido]['Formula'].values[0]
  elif operacion == '2':
    return df[df['Moderna'] == hidroxido]['Tradicional'].values[0]
  while operacion not in ['1', '2']:
    print('\nOpcion no valida, ingrese 1 o 2\n')
    operacion = input('\n')

def tradicional(df):
  hidroxido = input('\nIngrese la nomenclatura tradicional del hidroxido: ')
  while hidroxido not in df['Tradicional'].values:
    print('\nNomenclatura no valida\n')
    hidroxido = input('\nIngrese la nomenclatura tradicional del hidroxido: ')
  print('\nElija en qué nomenclatura quiere ver el hidroxido\n1. Formula\n2. Moderna\n')
  operacion = input('\n')
  if operacion == '1':
    return df[df['Tradicional'] == hidroxido]['Formula'].values[0]
  elif operacion == '2':
    return df[df['Tradicional'] == hidroxido]['Moderna'].values[0]
  while operacion not in ['1', '2']:
    print('\nOpcion no valida, ingrese 1 o 2\n')
    operacion = input('\n')

nomenclatura = input('Qué me vas a ingresar?\n1. Formula\n2. Moderna\n3. Tradicional\n4. salir\n')
while True:
  if nomenclatura == '1':
    print(formula(df) + '\n')
  elif nomenclatura == '2':
    print(moderna(df) + '\n')
  elif nomenclatura == '3':
    print(tradicional(df) + '\n')
  elif nomenclatura == '4':
    break

  else:
    print('\nOpcion no valida\n')

  nomenclatura = input('Qué me vas a ingresar?\n\n1. Formula\n\n2. Moderna\n\n3. Tradicional\n\n4. salir\n\n')
