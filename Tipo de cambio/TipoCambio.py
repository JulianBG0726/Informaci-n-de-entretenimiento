pesos=float(input("Ingresa la cantidad en pesos MXN: "))

print("Opcion 1: USD")
print("Opcion 2: EUR")
print("Opcion 3: THB")
print("Opcion 4: JPY")
print("Opcion 5: KRW")
print("Opcion 6: AUD")
print("Opcion 7: PEN")
print("Opcion 8: CAD")
print("Opcion 9: VES")
print("Opcion 10: ARS")

opcion=int(input())

match opcion:
    case 1:
        resultado=pesos/16.5
        moneda="USD"
    case 2:
        resultado=pesos/18
        moneda="EUR"
    case 3:
        resultado=pesos/0.45
        moneda="THB"
    case 4:
        resultado=pesos/0.12
        moneda="JPY"
    case 5:
        resultado=pesos/0.013
        moneda="KRW"
    case 6:
        resultado=pesos/11.5
        moneda="AUD"
    case 7:
        resultado=pesos/2.8
        moneda="PEN"
    case 8:
        resultado=pesos/8.2
        moneda="CAD"
    case 9:
        resultado=pesos/0.0023
        moneda="VES"
    case 10:
        resultado=pesos/0.046
        moneda="ARS"
    case _:
        resultado=None


if resultado != None:
    print("La moneda de", moneda, "está en: $", resultado, "pesos")
else:
    print("resultado inválido")