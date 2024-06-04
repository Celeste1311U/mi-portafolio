nombre = input('Hola, por favor ingresa tu nombre: ')

print(f'\nBienvenido/a {nombre}, ¿qué operación deseas realizar?\n')

def FaC(Fahrenheit):
    return (Fahrenheit - 32) * 0.5556

def CaF(Celsius):
    return (Celsius * 1.8) + 32

operación = ''

while operación != 'Finalizar':
    operación = input('1. Fahrenheit a Celsius\n2. Celsius a Fahrenheit\n3. Finalizar\n\n')
#reemplaza la , por un . ya que muchos usamos la , para los números
    if operación == '1' or operación.lower() == 'fahrenheit a celsius':
        Fahrenheit = input('\nIngrese los grados en Fahrenheit: ')
        if ',' in Fahrenheit:
            Fahrenheit = float(Fahrenheit.replace(',', '.'))

        elif '.' in Fahrenheit:
          Fahrenheit = float(Fahrenheit)

        else:
            Fahrenheit = int(Fahrenheit)
        FahrenheitResultado = FaC(Fahrenheit)
        print(f'\n{Fahrenheit}° Fahrenheit a Celsius son {round(FahrenheitResultado, 2)}°\n')

    elif operación == '2' or operación.lower() == 'celsius a fahrenheit':
        Celsius = input('\nIngrese los grados en Celsius: ')
        if ',' in Celsius:
            Celsius = float(Celsius.replace(',', '.'))

        elif '.' in Celsius:
          Celsius = float(Celsius)

        else:
            Celsius = int(Celsius)
        CelsiusResultado = CaF(Celsius)
        print(f'\n{Celsius}° Celsius a Fahrenheit son {round(CelsiusResultado, 2)}°\n')

    elif operación == '3' or operación.lower() == 'Finalizar':
        print('\nGracias por usar mi convertidor :D\n')
        break

    else:
        print('\nOpción no válida. Por favor, selecciona una operación válida.\n')

print('Hecho por Celeste Piccione de 5to 2da')

