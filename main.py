def suma(a, b):
    return a + b

def resta(a, b):
    return a - b 

print("----------CALCULADORA----------")
print("Seleccione lo que deseas hacer:\n1-Suma\n2-resta")

numero = int(input("Ingresa un numero: "))

if numero == 1:
    a = int(input("Ingresa el primer numero: "))
    b = int(input("Ingresa el segundo numero: "))
    
    resultado = suma(a, b)
    print("La suma es:", resultado)

elif numero == 2:
    a = int(input("ingresa el primer numero: "))
    b = int(input("ingresa el segund numero: "))
    resultado = resta(a,b)
    print("la esta es:", resultado)

else: 
    print("opcion no valida.")