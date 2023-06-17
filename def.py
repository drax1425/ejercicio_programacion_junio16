import time


# Definición de variables y estructuras de datos
mesas = [
    {"numero": 1, "capacidad": 2, "disponible": True},
    {"numero": 2, "capacidad": 2, "disponible": True},
    {"numero": 3, "capacidad": 2, "disponible": True},
    {"numero": 4, "capacidad": 4, "disponible": True},
    {"numero": 5, "capacidad": 4, "disponible": True},
    {"numero": 6, "capacidad": 4, "disponible": True},
    {"numero": 7, "capacidad": 6, "disponible": True},
    {"numero": 8, "capacidad": 6, "disponible": True},
    {"numero": 9, "capacidad": 6, "disponible": True},
]

reservas = []

# Definición de funciones

def ver_restaurant():
    print("Salón principal del restaurante:")
    for mesa in mesas:
        capacidad = mesa["capacidad"]
        estado = "Disponible" if mesa["disponible"] else "Ocupada"
        print(f"Mesa {mesa['numero']} - Capacidad: {capacidad} personas - Estado: {estado}")

def validar_rut(rut):
    # Validar que el rut esté en el rango especificado
    if not 1000000 <= rut <= 99999999:
        return False
    return True

def validar_nombre(nombre):
    # Validar que el nombre tenga al menos 3 letras sin espacios
    if len(nombre) < 3 or " " in nombre:
        return False
    return True

def validar_correo(correo):
    # Validar que el correo tenga formato válido con el símbolo '@'
    if "@" not in correo:
        return False
    return True

def validar_cantidad_personas(cantidad):
    # Validar que la cantidad de personas esté en el rango especificado
    if not 1 <= cantidad <= 6:
        return False
    return True

def reservar_mesa():
    rut = int(input("Ingrese el rut del cliente: "))
    if not validar_rut(rut):
        print("Rut inválido. Intente nuevamente.")
        return

    nombre = input("Ingrese el nombre del cliente: ")
    if not validar_nombre(nombre):
        print("Nombre inválido. Intente nuevamente.")
        return

    correo = input("Ingrese el correo del cliente: ")
    if not validar_correo(correo):
        print("Correo inválido. Intente nuevamente.")
        return

    cantidad_personas = int(input("Ingrese la cantidad de personas: "))
    if not validar_cantidad_personas(cantidad_personas):
        print("Cantidad de personas inválida. Intente nuevamente.")
        return

    mesas_disponibles = []
    for mesa in mesas:
        if mesa["capacidad"] >= cantidad_personas and mesa["disponible"]:
            mesas_disponibles.append(mesa)

    if not mesas_disponibles:
        print("No hay mesas disponibles para la cantidad de personas ingresada.")
        return

    print("Mesas disponibles:")
    for mesa in mesas_disponibles:
        print(f"Mesa {mesa['numero']} - Capacidad: {mesa['capacidad']} personas")

    numero_mesa = int(input("Ingrese el número de mesa deseado: "))
    mesa_seleccionada = None
    for mesa in mesas_disponibles:
        if mesa["numero"] == numero_mesa:
            mesa_seleccionada = mesa
            break

    if mesa_seleccionada is None:
        print("Número de mesa inválido. Intente nuevamente.")
        return

    mesa_seleccionada["disponible"] = False
    reserva = {
        "rut": rut,
        "nombre": nombre,
        "correo": correo,
        "mesa": mesa_seleccionada
    }
    reservas.append(reserva)
    print("Reserva realizada con éxito.")

def mostrar_menu_carta():
    print("----- Carta -----")
    print("1. Bebestibles")
    print("2. Platos")
    print("3. Postres")
    print("4. Pedir")
    print("5. Cancelar")

def mostrar_menu_principal():
    print("----- Menú Principal -----")
    print("1. Ver restaurant")
    print("2. Reservar mesa")
    print("3. Carta")
    print("4. Pagar")
    print("5. Cancelar reserva")
    print("6. Salir")

# Función principal que ejecuta el programa

def ejecutar_programa():
    while True:
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ver_restaurant()
        elif opcion == 2:
            reservar_mesa()
        elif opcion == 3:
            mostrar_menu_carta()
        elif opcion == 4:
            # Implementar la función de pagar
            pass
        elif opcion == 5:
            # Implementar la función de cancelar reserva
            pass
        elif opcion == 6:
            print("Gracias, adiós.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
time.sleep(3)
# Ejecutar el programa
ejecutar_programa()
