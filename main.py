def suma(a, b):
    return a + b

print ("----------CALCULADORA----------")
print ("Seleccione lo que deseas hacer:\n1-Suma\n")


numero = int(input("Ingresa un número: "))

if numero == 1:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    
    resultado = suma(a, b)
    print ("La suma es: ",resultado)