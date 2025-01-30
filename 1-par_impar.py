# Solicita que se ingrese un número entero
numero = int(input("Por favor, ingresa un número entero: "))

# nos verifica si el número es par o impar usando el operador módulo
if numero % 2 == 0:
    print(f"El número {numero} es par porque es divisible entre 2.")
else:
    print(f"El número {numero} es impar porque no es divisible entre 2.")
