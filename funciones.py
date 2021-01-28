class condicion ():
    def __init__(self, tipo1, obj1, cond, tipo2, obj2):
        self.tipo1 = tipo1
        self.obj1 = obj1
        self.cond = cond
        self.tipo2 = tipo2
        self.obj2 = obj2
    def __str__(self):
        aux = "{} ({}) {} {} ({})"
        aux = aux.format(self.obj1, self.tipo1, self.cond, self.obj2, self.tipo2)
        return aux

class house ():
    def __init__ (self, numero):
        self.atributos = list()
        self.atributos.append(numero)
        for i in range(5):
            self.atributos.append("None")
        self.posibilidades = {"Numero":[str(numero)],"Nacionalidad":["Noruego", "Sueco", "Aleman", "Britanico", "Danes"],"Tabaco":["Dunhill", "Blends", "PallMall", "Prince", "BlueMaster"], "Mascota":["Gato", "Caballo", "Pez", "Pajaro", "Perro"], "Bebida":["Agua", "Te", "Leche", "Cafe", "Cerveza"], "Color":["Amarillo", "Azul", "Rojo", "Verde", "Blanco"]}

#La funcion busca_tipo, recibe el nombre de un objeto (por ejemplo: "Noruego") y devuelve el tipo de característica ("Nacionalidad")
def busca_tipo(objeto):
	posibilidades = {"Numero":["1","2","3","4","5"],"Nacionalidad":["Noruego", "Sueco", "Aleman", "Britanico", "Danes"],"Tabaco":["Dunhill", "Blends", "PallMall", "Prince", "BlueMaster"], "Mascota":["Gato", "Caballo", "Pez", "Pajaro", "Perro"], "Bebida":["Agua", "Te", "Leche", "Cafe", "Cerveza"], "Color":["Amarillo", "Azul", "Rojo", "Verde", "Blanco"]}
	for key in posibilidades:
		if objeto in posibilidades[key]:
			return(key)

def compara (casa1, casa2, cond):#Esta funcion, compara una casa1 con una cond1 con una
#casa2 con una cond2 (casa1 y casa2 pueden ser la misma)
    contenido1 = cond.obj1 in casa1.posibilidades[cond.tipo1]
    contenido2 = cond.obj2 in casa2.posibilidades[cond.tipo2]
    if not( contenido1 and contenido2 ):
        if (contenido1):
            casa1.posibilidades[cond.tipo1].remove(cond.obj1)
        elif (contenido2):
            casa2.posibilidades[cond.tipo2].remove(cond.obj2)


def compara3 (casa1, casa2, casa3, tipo1, obj1, tipo2, obj2):#Esta funcion compara una casa2 (central) con una cond2 con las casas
#casa1 y casa3 con una cond1, en este caso solo borramos posibilidades de la casa2
#Cuando la casa esta en la esquina, utilizaremos casa1=casa3 y casa2 sera la casa de la esquina
    contenido1 = obj1 in casa1.posibilidades[tipo1]
    contenido2 = obj2 in casa2.posibilidades[tipo2]
    contenido3 = obj1 in casa3.posibilidades[tipo1]
    #Continua por aqui
    if ( contenido2 and (not(contenido1 or contenido3)) ):
        casa2.posibilidades[tipo2].remove(obj2)


#LAS FUNCIONES:
def y (casas, condicion):
    for casa in casas:
        compara(casa, casa, condicion)


def al_lado (casas, condicion):
    for i in range (5):
        if (i==0):
            compara3 (casas[1], casas[0], casas[1], condicion.tipo1, condicion.obj1, condicion.tipo2, condicion.obj2)
            compara3 (casas[1], casas[0], casas[1], condicion.tipo2, condicion.obj2, condicion.tipo1, condicion.obj1)
        elif (i == 4):
            compara3 (casas[3], casas[4], casas[3], condicion.tipo1, condicion.obj1, condicion.tipo2, condicion.obj2)
            compara3 (casas[3], casas[4], casas[3], condicion.tipo2, condicion.obj2, condicion.tipo1, condicion.obj1)
        else:
            compara3 (casas[i-1], casas[i], casas[i+1], condicion.tipo1, condicion.obj1, condicion.tipo2, condicion.obj2)
            compara3 (casas[i-1], casas[i], casas[i+1], condicion.tipo2, condicion.obj2, condicion.tipo1, condicion.obj1)
    #Cuando en una casa son posibles las dos condiciones de allado y una de ellas es 100% segura, borramos la otra
    for casa in casas:
        if( (condicion.obj1 in casa.posibilidades[condicion.tipo1]) and (condicion.obj2 in casa.posibilidades[condicion.tipo2]) ): 
            if (len(casa.posibilidades[condicion.tipo1]) == 1):
                casa.posibilidades[condicion.tipo2].remove(condicion.obj2)
            if (len(casa.posibilidades[condicion.tipo2]) == 1):
                casa.posibilidades[condicion.tipo1].remove(condicion.obj1)                
    		

def izquierda (casas, condicion):
    for i in range (3):
        compara(casas[i], casas[i+1], condicion)
    #De este tipo de condicion podemos sacar dos resultados extra:
    #En las casas de las esquinas:
    #La casa 1 no puede estar a la dcha de ninguna casa:
    contenido1 = condicion.obj2 in casas[0].posibilidades[condicion.tipo2]
    if(contenido1):
        casas[0].posibilidades[condicion.tipo2].remove(condicion.obj2)
    #La casa 5 no puede estar a la izda de ninguna casa:
    contenido2 = condicion.obj1 in casas[4].posibilidades[condicion.tipo1]
    if(contenido1):
        casas[4].posibilidades[condicion.tipo1].remove(condicion.obj1)

#La funcion que recorre las condiciones:
def repasa_condiciones (casas, condiciones):
	for condicion in condiciones:
		if(condicion.cond == "y"):
			y(casas, condicion)
		elif (condicion.cond == "izquierda"):
			izquierda(casas, condicion)
		elif (condicion.cond == "allado"):
			al_lado(casas, condicion)
		else:
			print ("/nError, condicion: ({}), no se encuentra en la lista de condiciones/n".format(condicion.cond))


def convierte(tipo):
	CONVERSION = {"Numero":0, "Nacionalidad":1, "Tabaco":2, "Mascota":3, "Bebida":4, "Color":5}
	return( CONVERSION[tipo] )



#Si por ejemplo la única posible nacionalidad de el dueño de la casa 1 es Britanico, borrará esa nacionalidad de las posibilidades de cualquier casa.
def quita_repetidas (casas):#Funciona :)
	for casa in casas:
		for tipo in casa.posibilidades:
			#Recorremos todos los tipos de cada casa
			if ((len(casa.posibilidades[tipo])==1)and(tipo!="Numero")):
				elemento = casa.posibilidades[tipo][0]
				casa.atributos[convierte(tipo)] = elemento
				for casa2 in casas:
					if (casa != casa2)and(elemento in casa2.posibilidades[tipo]):
						casa2.posibilidades[tipo].remove(elemento)

#Todos si una caracteristica solo se encuentra en una casa, este valor será el valor definitivo de esa casa
#Por ejemplo, si en la casa 1 tenemos los colores: "Rojo", "Verde", "Azul", y "Azul" solo se encuentra en la casa1
#Los posibles valores de casa 1 pasan a ser: "Azul"
def quita_solas (casas):
    terminadas = 0
    contador = {'Noruego': 0, 'Sueco': 0, 'Aleman': 0, 'Britanico': 0, 'Danes': 0, 'Dunhill': 0, 'Blends': 0, 'PallMall': 0, 'Prince': 0, 'BlueMaster': 0, 'Gato': 0, 'Caballo': 0, 'Pez': 0, 'Pajaro': 0, 'Perro': 0, 'Agua': 0, 'Te': 0, 'Leche': 0, 'Cafe': 0, 'Cerveza': 0, 'Amarillo': 0, 'Azul': 0, 'Rojo': 0, 'Verde': 0, 'Blanco': 0}
    #Contamos cuantas cualidades son unicas de una casa
    for casa in casas:
        for tipo in casa.posibilidades:
            if (tipo != "Numero"):
                for posibilidad in casa.posibilidades[tipo]:
                    contador[posibilidad] += 1
    #Procedemos a borrarlas. Buscamos los que solo se repiten una vez, buscamos la casa en la que se encuentra
    #esa unica posibilidad y borramos el resto de posibilidades de esta casa (dentro de su tipo respectivo)
    for posibilidad in contador:
        if (contador[posibilidad] == 1):
            terminadas += 1
            tipo = busca_tipo(posibilidad)
            for casa in casas:
                if (posibilidad in casa.posibilidades[tipo]):
                    for posibilidad2 in casa.posibilidades[tipo]:
                        if (posibilidad != posibilidad2):
                            casa.posibilidades[tipo].remove(posibilidad2)
    #Terminaremos cuando ya tengamos todos determinados
    if (terminadas == 25):
        return False
    else:
        return True


#La funcion imprime los resultados obtenidos:
def imprime (casas):
	linea = "\n----------------------------------\n"
	texto = "Casa numero: {}\n\tColor: {}\n\tNacionalidad: {}\n\tBebida: {}\n\tTabaco: {}\n\tMascota: {}"
	texto = linea + texto
	for casa in casas:
		print(texto.format(casa.atributos[0], casa.atributos[5], casa.atributos[1], casa.atributos[4], casa.atributos[2], casa.atributos[3]))
