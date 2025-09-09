# Ejercicio 4, Mariana Vergara 
try:
    # Pedir dos números enteros 
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    #  división
    resultado = num1 / num2

except ValueError:
    # Si el valor ingresado no es un entero
    print("Error: Debe ingresar números enteros.")

except ZeroDivisionError:
    # Si intenta dividir entre cero
    print("Error: No se puede dividir entre cero.")

else:
    # Si no hubo error, mostrar el resultado
    print(f"El resultado de la división es: {resultado}")
