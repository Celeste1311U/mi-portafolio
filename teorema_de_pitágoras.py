c1 = float(input('Ingrese su cateto: '))
c2 = float(input('Ingrese su segundo cateto: '))
hal2 = c1 ** 2 + c2 ** 2
print(f'la suma de los cuadrados de los catetos {c1} y {c2} da {c1**2} + {c2**2} = {hal2} por lo que la hipotenusa vale {round(hal2**0.5, 2)}')