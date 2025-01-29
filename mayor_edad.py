# Solicita que se ingrese la edad
edad = int(input("Por favor, ingresa tu edad: "))

# Verifica si la edad corresponde a una persona mayor o a una persona menor de edad
if edad >= 18:
    print(f"Tienes {edad} años, por lo que eres mayor de edad.")
else:
    print(f"Tienes {edad} años, por lo que aún no eres mayor de edad.")
