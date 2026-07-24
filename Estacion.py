mes = int(input("Escribe el número del mes: "))

match mes:
    case 6 | 7 | 8:
        estacion = ("Verano")
    case 9 | 10 | 11:
        estacion = ("Otoño")
    case 12 | 1 | 2:
        estacion = ("Invierno")
    case 3 | 4 | 5:
        estacion = ("Primavera")
    case _:
        estacion = ("Mes inválido")

if estacion != "Mes inválido":
    print("")
    print("Estamos en", estacion)
    print("")
else:
    print("")
    print(estacion)
    print("")