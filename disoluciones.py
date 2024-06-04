Vc = float(input('Ingrese el volumen inicial de la solución: '))
while Vc == 0:
  print('no se puede')
  Vc = float(input('Ingrese el volumen inicial de la solución: '))

Cc = float(input('Ingrese la molaridad inicial de la solución: '))
while Cc == 0:
  print('no se puede')
  Cc = float(input('Ingrese la molaridad inicial de la solución: '))

Cd = float(input('Ingrese la molaridad final de la disolución: '))
while Cd == 0:
  print('no se puede')
  Cd = float(input('Ingrese la molaridad final de la disolución: '))


Vd = Cc * Vc / Cd
print(f'\nLa disolución de {round(Vc,2)}L y {round(Cc,2)}G/L teniendo en cuenta que la molaridad final es {round(Cd,2)}G/L da un volumen de {round(Vd, 2)}L')
print(f'\nPodría parecer que la cuenta terminó ahí pero no \nFalta encontrar cuanta agua (o h2o para las ratas de laboratorio) tuvimos que agregar, para ello hacemos la formula de ΔV\nΔV = Vf - Vi')
deltaV = Vd - Vc
if deltaV > 0:
  print(f'\nTuvimos que agregar {round(deltaV,2)}L de agua para diluir la solución')
elif deltaV < 0:
  print(f'\nTuvimos que quitar {round(deltaV,2)}L de agua para diluir la solución')
else:
  print('No tuvimos que agregar agua')