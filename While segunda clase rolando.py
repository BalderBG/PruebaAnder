#while repite el bloque de codigo mientras la condicion sea verdadera (True )

seguir = True

print (10 == 12 )

while seguir:
    print ("esto funciona")

    fin = input("Desea seguir con esto? s/n")
    if fin == "n":
        seguir = False
        print("Esto se ha acabado")


#While con else

nombre = "Alberto"
while nombre == "Juana":
    print("Hola ",nombre)#Esto se repite si es True
else:
    print("No eres Juana") #se ejecuta una sola vez si es False


#Imprimir valores del 1 al 100
cont = 0
while cont <= 100:
    print (cont)
    cont += 1
    

#imprimir valores del 1 al 100
#for, se repite mientras se cumpla el numero de iteraciones definidas
#metodo dentro del for range (inicio,final(el numero dado menos uno)), salto (Opcional))
print("#########for##########")
for iteracion in range(1, 101):
    print(iteracion)



#realizar un programa que muestre la tabla de multiplicar dado un numero
print("tabla")


def tablaMultiplicar(numero,forma):
    if forma == "for":
        for i in range (1, 11):
            print(f"{i}x{numero}={i *numero}")

    elif forma == "while":
        i = 1
        while i<=10:
            print(f"{i}x{numero}={i *numero}")
            i += 1
    else:
        print("No selecciono la forma de ejecucion")

seguirMultiplicando = True

while seguirMultiplicando:

    numero = int(input("introduce un numero"))
    forma = input("Ingrese la forma")
    tablaMultiplicar(numero, forma)


    valor = input("Desea continuar? s/n")
    if valor == "n":
        seguirMultiplicando = False
        print("Fin de la trayectoria")



lista_todo = ["Maria" , 10, True, 3.99 , [1,2,3] ]

print( len(lista_todo) ) #obtengo la longitud de lista
print(lista_todo[-1]) #obtengo  el valor de la primera posicion
print ( len(lista_todo) - 1 )#Obtengo la ultima posicion de la lista

print(lista_todo [ len(lista_todo) - 1 ])  #Obtengo el valor de la ultima posicion de la lista

lista_todo[0] = "Javier"
#print(lista_todo)



print("#Recorrer lista con for")



for valores in lista_todo :
    if valores == 10:
        print(valores)


for iteration in range (0,len(lista_todo)):
    if iteration == 3:
        print(lista_todo[iteration])
        
"""   
print("#recorrer lista con while")
cont = 0
while cont < len(lista_todo):
    if lista_todo [cont] == True:
            print( lista_todo [cont] )
        cont += 1
"""
     
     
     
     
print("recorrer string con while")
for i in "Ander Sierra":
    print(i)





