# Ejercicio 3, Mariana Vergara 
def analizar_texto(*args, **kwargs):
    contar_vocales = kwargs.get('contar_vocales', False)
    contar_palabras = kwargs.get('contar_palabras', False)

    texto_completo = " ".join(args)

    if contar_vocales:
        vocales = "aeiouAEIOU"
        total_vocales = sum(1 for char in texto_completo if char in vocales)
        print(f"Total de vocales: {total_vocales}")

    if contar_palabras:
        palabras = texto_completo.split()
        total_palabras = len(palabras)
        print(f"Total de palabras: {total_palabras}")


if __name__ == "__main__":
    texto = input("Escribe un texto: ")

    print("¿Qué deseas contar? (Escribe el número correspondiente)")
    print("1 - Vocales")
    print("2 - Palabras")
    print("3 - Ambos")

    opcion = input("Opción: ")

    if opcion == "1":
        analizar_texto(texto, contar_vocales=True)
    elif opcion == "2":
        analizar_texto(texto, contar_palabras=True)
    elif opcion == "3":
        analizar_texto(texto, contar_vocales=True, contar_palabras=True)
    else:
        print("Opción no válida.")
