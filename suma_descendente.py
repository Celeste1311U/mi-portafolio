num = int(input('ingrese su numero: '))
numCopia = num
i = 0
while num > 0:
  i += num
  num -= 1
print(f'La suma por el anterior del {numCopia} hasta el 0 da {i}')