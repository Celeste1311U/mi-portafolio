import periodictable

#Definir los valores del grupo orbital
s = 2
p = 6
d = 10
f = 14

#Definir el diccionario de configuraciones electrónicas
confE = {
    '1s': s,
    '2s': s,
    '2p': p,
    '3s': s,
    '3p': p,
    '3d': d,
    '4s': s,
    '4p': p,
    '4d': d,
    '4f': f,
    '5s': s,
    '5p': p,
    '5d': d,
    '5f': f,
    '6s': s,
    '6p': p,
    '6d': d,
    '7s': s,
    '7p': p
}

# Solicitar al usuario que ingrese el número atómico del elemento
z = int(input('Ingrese el Z del elemento: '))

while z!=0:
  ce=''
  elemento = periodictable.elements[z]
  for orbitales, electrones in confE.items():
    if z >= electrones:
      ce += orbitales + str(electrones) + ' '
      z -= electrones
    else:
      if z!=0:
        ce += orbitales + str(z)
      break
  print(f'La CE del elemento {elemento} es: {ce}')
  z = int(input('Ingrese otro Z o 0 para finalizar: '))