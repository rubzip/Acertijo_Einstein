from funciones import condicion

#La funcion busca_tipo, recibe el nombre de un objeto (por ejemplo: "Noruego") y devuelve el tipo de característica ("Nacionalidad")
def busca_tipo(objeto):
	posibilidades = {"Numero":["1","2","3","4","5"],"Nacionalidad":["Noruego", "Sueco", "Aleman", "Britanico", "Danes"],"Tabaco":["Dunhill", "Blends", "PallMall", "Prince", "BlueMaster"], "Mascota":["Gato", "Caballo", "Pez", "Pajaro", "Perro"], "Bebida":["Agua", "Te", "Leche", "Cafe", "Cerveza"], "Color":["Amarillo", "Azul", "Rojo", "Verde", "Blanco"]}
	for key in posibilidades:
		if objeto in posibilidades[key]:
			return(key)

def lee_condiciones (nombre_fich):
	condiciones = list()
	fich = open (nombre_fich, "r")
	try:
		for line in fich:
			line = line.replace("\n", "")           #Eliminamos el \n
			obj1, cond, obj2 = line.split(" ", 3)   #Separamos line en 3
			nueva_condicion = condicion(busca_tipo(obj1), obj1, cond, busca_tipo(obj2), obj2)
			condiciones.append(nueva_condicion)
	finally:
		fich.close()
	return (condiciones)
