num = int(input('ingrese el número: '))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1

print(factorial)