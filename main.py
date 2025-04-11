def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    print("\n----------CALCULADORA----------")
    print("Seleccione lo que deseas hacer:\n1-Suma\n2-Resta\n3-Multiplicación\n4-División\n5-Salir")

    try:
        numero = int(input("Ingresa un numero: "))

        if numero == 1:
            a = int(input("Ingresa el primer numero: "))
            b = int(input("Ingresa el segundo numero: "))

            resultado = suma(a,b)
            print("El resultado de la suma es:", resultado)
            input("Presiona Enter para volver al menú...")

        elif numero == 2:
            a = int(input("Ingresa el primer numero: "))
            b = int(input("Ingresa el segundo numero: "))

            resultado = resta(a,b)
            print("El resultado de la resta es:", resultado)
            input("Presiona Enter para volver al menú...")

        elif numero == 3:
            a = int(input("Ingresa el primer numero: "))
            b = int(input("Ingresa el segundo numero: "))

            resultado = multiplicacion(a,b)
            print("El resultado de la multiplicación es:", resultado)
            input("Presiona Enter para volver al menú...")

        elif numero == 4:
            a = int(input("Ingresa el primer numero: "))
            b = int(input("Ingresa el segundo numero: "))
            if b == 0:
                print("¡Error! No se puede dividir por cero.")
            else:
                resultado = division(a,b)
                print("El resultado de la división es:", resultado)
            input("Presiona Enter para volver al menú...")

        elif numero == 5:
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")
            input("Presiona Enter para volver al menú...")

    except ValueError:
        print("¡Error! Ingresa un número entero.")
        input("Presiona Enter para volver al menú...")

