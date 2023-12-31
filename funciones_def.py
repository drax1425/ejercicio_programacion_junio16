import numpy as np
restaurante = np.array([3,3])


reservas = []

def ver_restaurant():
    print("Salón principal del restaurante:")
    for x in range(3):
        print(f"personas{(x+1)*2}:", end=" ")
        for y in range (3):
            print(restaurante[x][y], end=" ")
        print()
    

def validar_rut(rut):     
  if not 1000000 <= rut <= 99999999:
     return rut
    

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
    try:
      rut = input("Ingrese el rut del cliente: ")
    except:
        print("ingrresa un rut sin numero verificador")
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
    for restaurante in :
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
    opcion_carta = int(input("Seleccione una opción: "))
    if opcion_carta == 1:
        pass
    elif opcion_carta == 2:
        pass
    elif opcion_carta == 3:
        pass
    elif opcion_carta == 4:
        pass
    elif opcion_carta == 5:
        pass



def mostrar_menu_principal():
    print("----- Menú Principal -----")
    print("1. Ver restaurant")
    print("2. Reservar mesa")
    print("3. Carta")
    print("4. Pagar")
    print("5. Cancelar reserva")
    print("6. Salir")


def validar_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == (1,2,3,4,5,6,):
            return opcion
        else:
            print ("solo tienes opciones del 1 al 6")
    except:
        print("ingresa solo numeros enteros ")
            

