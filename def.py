import time
import funciones_def as fd

# Definición de variables y estructuras de datos

while True:
    fd.mostrar_menu_principal()
    opcion = fd.validar_opcion

    if opcion == 1:
            fd.ver_restaurant()
    elif opcion == 2:
            fd.reservar_mesa()
    elif opcion == 3:
            fd.mostrar_menu_carta()
            
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

