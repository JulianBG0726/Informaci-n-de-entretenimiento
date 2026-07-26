#Brindar información acerca de una película, serie o artísta
consulta=input("Por favor, escriba el artísta, película o serie de la que deseé información: ")
consulta=consulta.lower()#Aquí estamos transformando la cadena de caracteres que fue introducida a minúsculas
x=True#Aquí creé una variable que me ayudará a determinar si la entrada fué válida
match consulta:#aqui se crea el match
    case "inception":
        info="Película de ficción dirigida por Cristipher Nolan en 2010 que nadie entendió "
    case "beattles":
        info="Banda británica de rock formada en la década de los 60´s"
    case "rick and morty":
        info="Serie de animación de Adult Swim con un enfoque en la ciencia ficción y la comedia"
    case "stranger things":
        info="Serie de streaming de terror y ciencia ficción creada por Netflix a mediados de la década pasada"
    case "avengers":
        info="Película del UCM estrenada en 2012"
    case _:
        info="No se encontró información"#En caso de que sea una entrada inválida
        x=False #Aquí definimos la entrada como inválida

if x!=False:#Aquí está la condición que determinará qué mensaje se va a imprimir
    print("Se trata de la", info)
else:
    print(info)
