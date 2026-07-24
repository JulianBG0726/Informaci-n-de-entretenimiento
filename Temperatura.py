celsius = float(input("Ingresa la temperatura en °C: "))
print("")
print("Selecciona una opción:")
print("opción 1: F")
print("opción 2: K")
opcion = int(input())
match opcion:
    case 1:
        resultado=celsius*9/5+32
        unidad="F"
    case 2:
        resultado=celsius+273.15
        unidad="F"
    case _:
        unidad=None
        resultado="Opción inválida"
if unidad!=None:
    print(resultado, "°", unidad)
else:
    print(resultado)
        