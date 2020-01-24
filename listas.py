#Listras separadas por coma y entre corchetes
l = [2,"tres",True,["uno",10],3,"diez"]
l[2] = 'a' #Cambiar valores de la lista
l2 = l[3][1] #Acceder a un elemento de una lista dentro de otra lista
l3 = l[0:3] #Primer elemento -> desde dónde 
			#Segundo elemeto -> cuántos
l4 = l[0:6:2] #Primeros dos -> rango 
			 #Último -> longitud del salto + 1
l5 = l[0::2] #Copia uno si y uno no de toda la lista
l [0:3] = ['b','a','h'] #A partir del primer elemento cambia cada
						# uno por b,a,h 
print (l2)
print (l)
print (l5)