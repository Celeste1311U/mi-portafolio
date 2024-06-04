def suma():
  a = float(input('ingrese el primer numero: '))
  b = float(input('ingrese el segundo numero: '))
  print(f'la suma de {a} y {b} da {a+b}')

def resta():
  a = float(input('ingrese el primer numero: '))
  b = float(input('ingrese el segundo numero: '))
  print(f'la resta de {a} y {b} da {a-b}')

def mult():
  a = float(input('ingrese el primer numero: '))
  b = float(input('ingrese el segundo numero: '))
  print(f'el producto de {a} y {b} da {a*b}')
  tabla = input('querés la tabla de multiplicar de uno de los 2 elementos? (si quiere la tabla, ponga el elemento a o el b): ')
  if tabla == 'a':
    end = round(float(input('hasta qué número?')))
    a = round(a)
    for n, x in enumerate(range(0, end+1, a)):
      print(f'{a} * {n} = {x}')

  elif tabla == 'b':
    end = round(float(input('hasta qué número?')))
    b = round(b)
    for n, x in enumerate(range(0, end+1, b)):
      print(f'{b} * {n} = {x}')

def div():
  a = float(input('ingrese el primer numero: '))
  b = float(input('ingrese el segundo numero: '))
  print(f'la división entre {a} y {b} da {a//b} y su resto es {a%b}')

def pot():
  a = float(input('ingrese la base del numero: '))
  b = float(input('ingrese el exponente numero: '))
  print(f'{a} elevado a {b} da {a**b}')

def square():
  a = float(input('ingrese el radicando: '))
  b = float(input('Ingrese el índice de la raíz: '))
  print(f'la raiz de {a} con índice {b} es {round(a**(1/b), 2)}')

op = input('calculadora\n1 - suma\n2 - resta\n3 - multiplicacion\n4 - division\n5 - potencia\n6 - raíz\n7 - finalizar\n')
while op != '7':
  if op == '1':
    suma()
  elif op == '2':
    resta()
  elif op == '3':
    mult()
  elif op == '4':
    div()
  elif op == '5':
    pot()
  elif op == '6':
    square()
  op = input('calculadora\n1 - suma\n2 - resta\n3 - multiplicacion\n4 - division\n5 - potencia\n6 - raíz\n7 - finalizar\n')