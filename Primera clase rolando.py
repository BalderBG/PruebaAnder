numero1 = 0
numero2 = 0
suma = 0
resta = 0
producto = 0
division = 0
continuar = True;
seguir = ""


while continuar:

    #entrada
    numero1 = input("introduce el primer numero: ") 
    numero2 = input("introduce el segundo numero: ") 


    while numero1.isnumeric() == False or numero2.isnumeric() == False:
        numero1 = input("introduce el primer numero: ") 
        numero2 = input("introduce el segundo numero: ") 

    #transformacion
    numero1 = float ( numero1 ) 
    numero2 = float ( numero2 ) 

    suma = numero1 + numero2
    resta = numero1 - numero2
    producto = numero1 * numero2
    division = numero1 / numero2


    #salida
    print(f"La suma es: {suma} \n La resta es: {resta} \n el producto es: {producto} \n la division es: {division}")

    seguir = input("¿Quieres continuar? si/no")
    if seguir == "no":
        continuar = False