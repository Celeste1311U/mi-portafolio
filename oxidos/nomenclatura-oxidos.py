import pandas as pd
import periodictable as pt
# Cargar el archivo Excel en un DataFrame
df = pd.read_excel('oxidos.xlsx')
formulas = df['Formula']
modernas = df['Moderna']
tradicionales = df['Tradicional']
densidad = df['Densidad']
pf = df['Fusión']
pe = df['Ebullición']

def formula(df):
    oxido = input("Ingrese la formula del óxido: ")
    while oxido not in formulas.values:
      print('\nIngrese una formula válida')
      oxido = input('\nIngrese la formula del óxido: ')
    print('\nElija en qué nomenclatura quiere ver el óxido\n1. tradicional\n2. moderna')
    operacion = input('')
    while operacion != '1' and operacion != '2':
      print('\nIngrese una opción válida')
      operacion = input('\nElija en qué nomenclatura quiere ver el óxido\n1. tradicional\n2. moderna\n')
    if operacion == '1':
        print(df[formulas == oxido]['Tradicional'].values[0])
    elif operacion == '2':
        print(df[formulas == oxido]['Moderna'].values[0])

    oxidatos = {
        'formula': oxido,
        'peso molar': round(pt.formula(oxido).mass, 2),
        'densidad': df[formulas == oxido]['Densidad'].values[0],
        'fusión': df[formulas == oxido]['Fusión'].values[0],
        'ebullición':df[formulas == oxido]['Ebullición'].values[0]
    }
    print(oxidatos)

def tradicional(df):
    oxido = input("Ingrese el nombre del óxido: ")
    while oxido not in tradicionales.values:
      print('\nIngrese un óxido válido')
      oxido = input('\nIngrese el nombre del óxido: ')
    print('\nElija en qué nomenclatura quiere ver el óxido\n1. formula\n2. moderna')
    operacion = input('')

    while operacion != '1' and operacion != '2':
      print('\nIngrese una opción válida')
      operacion = input('\nElija en qué nomenclatura quiere ver el óxido\n1. formula\n2. moderna\n')


    formula = df[tradicionales == oxido]['Formula'].values[0]
    if operacion == '1':
        print(formula)
    elif operacion == '2':
        print(df[tradicionales == oxido]['Moderna'].values[0])

    oxidatos = {
        'formula': formula,
        'peso molar': f'{round(pt.formula(formula).mass, 2)}g',
        'densidad': df[tradicionales == oxido]['Densidad'].values[0],
        'fusión': df[tradicionales == oxido]['Fusión'].values[0],
        'ebullición':df[tradicionales == oxido]['Ebullición'].values[0]
    }
    print(oxidatos)

def moderna(df):
    oxido = input("Ingrese el nombre del óxido: ")
    while oxido not in modernas.values:
      print('Ingrese un óxido válido')
      oxido = input('\nIngrese el nombre del óxido: ')
    print('Elija en qué nomenclatura quiere ver el óxido\n1. formula\n2. tradicional')
    operacion = input('')
    while operacion != '1' and operacion != '2':
      print('Ingrese una opción válida')
      operacion = input('\nElija en qué nomenclatura quiere ver el óxido\n1. formula\n2. tradicional\n')
    formula = df[modernas == oxido]['Formula'].values[0]
    if operacion == '1':
        return(formula)
    elif operacion == '2':
        print(df[modernas == oxido]['Tradicional'].values[0])
    oxidatos = {
        'formula': formula,
        'peso molar': f'{round(pt.formula(formula).mass, 2)}g',
        'densidad': df[modernas == oxido]['Densidad'].values[0],
        'fusión': df[modernas == oxido]['Fusión'].values[0],
        'ebullición':df[modernas == oxido]['Ebullición'].values[0]
    }
    print(oxidatos)

nomenclatura = input('Qué me vas a poner?\n1. formula\n2. tradicional\n3. Moderna\n4. salir\n\n')
while True:
    if nomenclatura == '1':
      formula(df)
    elif nomenclatura == '2':
      tradicional(df)
    elif nomenclatura == '3':
      moderna(df)
    elif nomenclatura == '4':
      break
    else:
        print('Ingrese una opción válida')
    nomenclatura = input('Qué me vas a poner?\n1. formula\n2. tradicional\n3. Moderna\n4. salir\n\n')
    
    
  