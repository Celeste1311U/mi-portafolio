a = int(input('Ingrese el número a: '))
b = int(input('Ingrese el número b: '))
c = int(input('Ingrese el número c: '))

bhaskara1 = (-b+((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
bhaskara2 = (-b-((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

print(f'las raices del trinomio son {round(bhaskara1, 2)} y {round(bhaskara2, 2)}')