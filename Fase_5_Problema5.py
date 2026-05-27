# ==========================================================
# PROGRAMA: CONTROL DE HORAS SEMANALES
# DESCRIPCIÓN:
# El usuario ingresa trabajadores y las horas
# trabajadas de lunes a viernes.
# El programa calcula el total semanal y clasifica
# la jornada laboral.
# ==========================================================

# ----------------------------------------------------------
# FUNCIÓN: validar_numero_positivo
# OBJETIVO:
# Validar que el usuario ingrese un número positivo 
# de la cantidad de trabajadores
# ----------------------------------------------------------
def validar_numero_positivo(mensaje):

    # Ciclo infinito hasta ingresar un valor válido
    while True:
        try:
            # Solicitar número
            numero = float(input(mensaje))

            # Verificar que sea positivo
            if numero >= 0:

                # Retornar número válido
                return numero
            else:
                # Mensaje de error
                print("Debe escribir un valor numérico positivo.")
        except ValueError:

            # Mensaje si escribe texto
            print("Debe escribir un valor numérico positivo.")


# ----------------------------------------------------------
# FUNCIÓN: calcular_horas
# OBJETIVO:
# Calcular el total semanal y clasificar la jornada
# ----------------------------------------------------------
def calcular_horas(horas):
    # Calcular suma total
    total = sum(horas)

    # Verificar si supera las 40 horas
    if total > 40:
        # Clasificación de sobretiempo
        clasificacion = "Sobretiempo"

    else:
        # Clasificación estándar
        clasificacion = "Horario Estándar"

    # Retornar resultados
    return total, clasificacion


# ----------------------------------------------------------
# CREAR MATRIZ VACÍA
# ----------------------------------------------------------
recursos = []

# ----------------------------------------------------------
# PEDIR CANTIDAD DE TRABAJADORES
# ----------------------------------------------------------
cantidad = int(
    validar_numero_positivo(
        "¿Cuántos trabajadores desea registrar?: "
    )
)

# ----------------------------------------------------------
# REGISTRO DE DATOS
# ----------------------------------------------------------
for i in range(cantidad):
    # Mostrar encabezado
    print("\n===================================")
    print(f"REGISTRO DEL TRABAJADOR {i + 1}")
    print("===================================")

    # Solicitar nombre
    nombre = input("Ingrese el nombre del trabajador: ")

    # Solicitar horas trabajadas
    lunes = validar_numero_positivo(
        "Horas trabajadas el lunes: "
    )

    martes = validar_numero_positivo(
        "Horas trabajadas el martes: "
    )

    miercoles = validar_numero_positivo(
        "Horas trabajadas el miércoles: "
    )

    jueves = validar_numero_positivo(
        "Horas trabajadas el jueves: "
    )

    viernes = validar_numero_positivo(
        "Horas trabajadas el viernes: "
    )

    # Guardar datos en la matriz
    recursos.append([
        nombre,
        lunes,
        martes,
        miercoles,
        jueves,
        viernes
    ])


# ----------------------------------------------------------
# MOSTRAR RESULTADOS
# ----------------------------------------------------------
print("\n===================================")
print("RESULTADOS FINALES")
print("===================================")

# ----------------------------------------------------------
# RECORRER MATRIZ
# ----------------------------------------------------------
for recurso in recursos:

    # Obtener nombre
    nombre = recurso[0]

    # Obtener horas
    horas = recurso[1:]

    # Calcular resultados
    total, clasificacion = calcular_horas(horas)

    # Mostrar resultados
    print(f"\nTrabajador: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificación: {clasificacion}")
    print("===================================")
    