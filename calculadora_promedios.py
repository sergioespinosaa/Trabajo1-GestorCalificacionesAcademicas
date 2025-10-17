UMBRAL = 5.0 # Calificación mínima para aprobar

def ingresar_calificaciones():
    """Solicita materias y calificaciones (0-10) y retorna dos listas paralelas.

    Retorna:
        tuple[list[str], list[float]]: (materias, calificaciones)
    """

    materias = []
    calificaciones = []

    while True:
        # Solicitar nombre de la materia
        materia = input("Ingrese el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue

        # Solicitar calificación válida entre 0 y 10
        while True:
            entrada = input("Ingrese la calificación (0 a 10): ").strip().replace(',', '.')
            try:
                calificacion = float(entrada)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entre 0 y 10.")
                continue

            if 0 <= calificacion <= 10:
                break
            else:
                print("La calificación debe estar entre 0 y 10.")

        materias.append(materia)
        calificaciones.append(calificacion)

        # Preguntar si se desea continuar
        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar not in ("s", "si", "sí", "y", "yes"):
            break

    return materias, calificaciones
    
    
def calcular_promedio(calificaciones):
    """Calcula el promedio de una lista de calificaciones.
    Args:
        calificaciones (list[float]): Lista de calificaciones.
    Returns:
        float: Promedio de las calificaciones.
    """
    promedio = float(sum(calificaciones)) / len(calificaciones) if calificaciones else 0.0
    return promedio

def determinar_estado(calificaciones, umbral):
    """Determina si el estudiante aprobó o reprobó según el umbral.
    Args:
        calificaciones (list[float]): Lista de calificaciones.
        umbral (float): Calificación mínima para aprobar.
    Returns:
    """
    if not calificaciones:
        return None, None

    aprobadas_idx, suspendidas_idx = list(), list()
    for calificacion in calificaciones:
        if calificacion >= umbral:
            start = aprobadas_idx[-1] + 1 if aprobadas_idx else 0
            idx = calificaciones.index(calificacion, start)
            aprobadas_idx.append(idx)
            
        else:
            start = suspendidas_idx[-1] + 1 if suspendidas_idx else 0
            idx = calificaciones.index(calificacion, start)
            suspendidas_idx.append(idx)

    return aprobadas_idx, suspendidas_idx


def encontrar_extremos(calificaciones):
    """Encuentra el indice de la calificación más alta y más baja en una lista.
    Args:
        calificaciones (list[float]): Lista de calificaciones.
    Returns:
        tuple[int, int]: (índice de la calificación más alta, índice de la calificación más baja)
    """
    if not calificaciones:
        return None, None
    calificacion_maxima_idx = calificaciones.index(max(calificaciones))
    calificacion_minima_idx = calificaciones.index(min(calificaciones))
    return calificacion_maxima_idx, calificacion_minima_idx


if __name__ == "__main__":
    print("=== Calculadora de Promedios ===")
    materias, calificaciones = ingresar_calificaciones()
    promedio = calcular_promedio(calificaciones)    
    aprobadas_idx, suspendidas_idx = determinar_estado(calificaciones, UMBRAL)
    calificacion_maxima_idx, calificacion_minima_idx = encontrar_extremos(calificaciones)

    print("\n--- Resumen de Calificaciones ---")
    for i in range(len(materias)):
        print(f"{materias[i]}: {calificaciones[i]}")

    print(f"Promedio: {promedio:.2f}")
    
    aprobadas = [materias[i] for i in aprobadas_idx]
    suspendidas = [materias[i] for i in suspendidas_idx]
    print(f"Materias aprobadas: {aprobadas}")
    print(f"Materias suspendidas: {suspendidas}")
    print(f"Calificación máxima: {materias[calificacion_maxima_idx]} con un {calificaciones[calificacion_maxima_idx]}")
    print(f"Calificación mínima: {materias[calificacion_minima_idx]} con un {calificaciones[calificacion_minima_idx]}")
