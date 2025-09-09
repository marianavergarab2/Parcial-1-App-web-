def promedio_notas(estudiantes):
    if not estudiantes:
        return 0
    total = sum(est["nota"] for est in estudiantes)
    return total / len(estudiantes)

def mejor_estudiante(estudiantes):
    if not estudiantes:
        return None
    mejor = max(estudiantes, key=lambda est: est["nota"])
    return mejor["nombre"], mejor["nota"]

def peor_estudiante(estudiantes):
    if not estudiantes:
        return None
    peor = min(estudiantes, key=lambda est: est["nota"])
    return peor["nombre"], peor["nota"]

def main():
    estudiantes = []
    
    while True:
        nombre = input("Ingrese nombre del estudiante (o 'fin' para terminar): ").strip()
        if nombre.lower() == "fin":
            break
        
        try:
            nota = float(input(f"Ingrese nota de {nombre}: "))
        except ValueError:
            print("Por favor ingrese un número válido para la nota.")
            continue
        
        estudiantes.append({"nombre": nombre, "nota": nota})
    
    print("\n--- Reporte Final ---")
    print(f"Número de estudiantes: {len(estudiantes)}")
    
    if estudiantes:
        promedio = promedio_notas(estudiantes)
        mejor = mejor_estudiante(estudiantes)
        peor = peor_estudiante(estudiantes)
        
        print(f"Promedio de notas: {promedio:.2f}")
        print(f"Mejor estudiante: {mejor[0]} con nota {mejor[1]:.2f}")
        print(f"Peor estudiante: {peor[0]} con nota {peor[1]:.2f}")
        
        # Ordenar estudiantes por nota de menor a mayor
        estudiantes_ordenados = sorted(estudiantes, key=lambda est: est["nota"])
        
        print("\nEstudiantes ordenados de menor a mayor nota:")
        for est in estudiantes_ordenados:
            print(f"{est['nombre']}: {est['nota']:.2f}")
    else:
        print("No se ingresaron estudiantes.")

if __name__ == "__main__":
    main()
