#funcion para tranajar con paises y capitales
def paisescapitales():
	#diccionario de almacenamiento de paises y capitales
	pcapitales = {}
	x = True
	conteo=0
	while x == True: 
		#pide el pais y capital
		pais = input("ingrese el nombre del pais:")
		capital = input("ingrese su capital:")
		pcapitales[pais] = capital
		print(pcapitales)
		#desea ingresar otro pais
		opcion = input("¿desea seguir operando?y/n")
		if opcion =="y":
			x= True
		else:
			x= False
			for a,b in pcapitales.items():
				conteo=conteo+1
				print(str(conteo)+" "+a,b)
			break
paisescapitales()
		