# Ejercicio 1, Mariana Vergara 

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Pedir al usuario un número entero positivo
while True:
    try:
        limite = int(input("Ingrese un número entero positivo: "))
        if limite > 0:
            break
        else:
            print("El número debe ser mayor que 0.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Imprimir los números primos hasta el número ingresado
print(f"Números primos hasta {limite}:")
for numero in range(1, limite + 1):
    if es_primo(numero):
        print(numero)