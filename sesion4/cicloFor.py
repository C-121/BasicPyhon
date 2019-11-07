edades = []
n_personas = int(input("Cuantas personas va a registrar"))
for i in range(n_personas):
    dato = int(input ("Ingrese la edad de la persona {}: ".format(i + 1)))
    edades.append(dato)
suma = 0
for i in range(len(edades)):
    suma += edades[i]
    
'''
for edad in edades:
    suma += edad 
'''
    
promedio = suma // n_personas 

print("La media de edad de los datos capturados es: {}".format(promedio))
