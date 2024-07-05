import pandas as pd

df = pd.read_excel('lista_sales.xlsx')


formula = df['formula']
tradicional = df['tradicional']
moderna = df['moderna']

def FormulaAtm(sal):
    operacion = input('1. tradicional\n2. moderna: \n')
    while operacion not in ['1', '2']:
        print('\nopción inválida\n\n')
        operacion = input('1. tradicional\n2. moderna: \n')
    
    if operacion == '1':
        resultado = df[df['formula'] == sal]['tradicional'].values[0]
        return f'La sal {sal} en nomenclatura tradicional es {resultado}'
    elif operacion == '2':
        resultado = df[df['formula'] == sal]['moderna'].values[0]
        return f'La sal {sal} en nomenclatura moderna es {resultado}'

def TradicionalAfm(sal):
    operacion = input('1. formula\n2. moderna: \n')
    while operacion not in ['1', '2']:
        print('\nopción inválida\n\n')
        operacion = input('1. formula\n2. moderna: \n')
    
    if operacion == '1':
        resultado = df[df['tradicional'] == sal]['formula'].values[0]
        return f'La sal {sal} en formula es {resultado}'
    elif operacion == '2':
        resultado = df[df['tradicional'] == sal]['moderna'].values[0]
        return f'La sal {sal} en nomenclatura moderna es {resultado}'

def ModernaAft(sal):
    operacion = input('1. formula\n2. tradicional: \n')
    while operacion not in ['1', '2']:
        print('\nopción inválida\n\n')
        operacion = input('1. formula\n2. tradicional: \n')
    
    if operacion == '1':
        resultado = df[df['moderna'] == sal]['formula'].values[0]
        return f'La sal {sal} en formula es {resultado}'
    elif operacion == '2':
        resultado = df[df['moderna'] == sal]['tradicional'].values[0]
        return f'La sal {sal} en nomenclatura tradicional es {resultado}'


while True:
    sal = input('ingrese la formula, nomenclatura tradicional o nomenclatura moderna de la sal: ')
    if sal in formula.values:
        print(FormulaAtm(sal))
    elif sal in tradicional.values:
        print(TradicionalAfm(sal))
    elif sal in moderna.values:
        print(ModernaAft(sal))
    elif sal == 'Salir':
        print('chau')
        break
    else:
        print('\n\noperación inválida\n\n')