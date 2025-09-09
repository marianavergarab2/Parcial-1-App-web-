# Ejercicio 2, Mariana Vergara
def calcular_descuento(precio, descuento=10):
    # precio final después del descuento
    return precio * (1 - descuento / 100)

total = 0

for i in range(3):
    precio = float(input(f"Ingresa el precio del producto {i+1}: "))
    total += calcular_descuento(precio)  # descuento por defecto es 10

print(f"El valor total a pagar es: {total:.2f}")
