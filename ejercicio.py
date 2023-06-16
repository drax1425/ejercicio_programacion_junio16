l_bebidad = []
l_platos = []
l_postres = []
while True:
    print("""MENU PRINCIPAL:
    ------------------------------------------
    1. Ver:
    2. Reserva:
    3. Carta:
          carta
            1.bebidas(3)
            2.platos(3)
            3.postre(3)
            4.Pedir
            5.Cancelar

    4.Pagar: imprimir voleta
    5.Cancelar:
    6.Salir:
    ------------------------------------------""")
    while True:
        opciones = int("ingrese una de las opciones :")
        if opciones == 1:
            pass
        elif opciones == 2:
            pass
        elif opciones == 3:
            print("""Carta:
            -----------------------
            1. Bebidas
            2. Platos
            3. Postres
            4. Pedir
            5. Cancelar
            -------------------------""")
            opcion_carta = int(input("escoja la opción que desea: "))  
            if opcion_carta == 1:
                
        elif opciones == 4:
            pass
        elif opciones == 5:
            pass
        else:
           break