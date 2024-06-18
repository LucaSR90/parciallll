# parcial:Realizar un programa que capture 4 notas de los estudiantes y determine el promedio.

def capturar_notas():
    estudiantes = []

    while True:
        # Solicitar información del estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        matricula = input("Ingrese la matrícula del estudiante: ")

        # Capturar las 4 notas
        notas = []
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {i}: "))
                    if nota >= 0:
                        notas.append(nota)
                        break
                    else:
                        print("La nota no puede ser negativa. Inténtelo de nuevo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

        # Calcular el promedio
        promedio = sum(notas) / 4

        # Guardar la información del estudiante
        estudiante = {
            "nombre": nombre,
            "matricula": matricula,
            "promedio": promedio
        }
        estudiantes.append(estudiante)

        # Preguntar si se quiere capturar otro estudiante
        continuar = input("¿Desea capturar otro estudiante? (si/no): ")
        if continuar.lower() != 's':
            break

    # Imprimir los promedios de cada estudiante
    print("\nPromedios de los estudiantes:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}, Promedio: {estudiante['promedio']:.2f}")


capturar_notas()
