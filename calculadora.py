#calculadora
n=1
while n!= 0:
    n= int(input("seleccione opcion: 1. sumar 2. restar 3. multiplicar 4. dividir 0.salir: "))
    if n==1:
        n1= int(input("Ingrese el primer numero a sumar: "))
        n2= int(input("Ingrese el segundo numero a sumar: "))
        print("Respuesta: "+str(n1+n2))
    elif n==2:
        n1= int(input("Ingrese el primer numero a restar: "))
        n2= int(input("Ingrese el segundo numero a restar: "))
        print("la respuesta es: "+ str(n1-n2))
    elif n==3:
        n1= int(input("Ingrese el primer numero a multiplicar: "))
        n2= int(input("Ingrese el segundo numero a multiplicar: "))
        print("repsuesta: "+str(n1*n2))
    elif n==4:
        n1= int(input("Ingrese el dividendo: "))
        n2= int(input("Ingrese el divisor: "))
        if n2!=0:
            print("la respuesta es " + str(n1/n2))
        else:
            print("El divisor no puede ser cero")
    elif n==0:
        print("Gracias por usar el programa")
    else:
        print("opción inválida")
        
        
