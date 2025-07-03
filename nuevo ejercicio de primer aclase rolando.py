numero1 = 0
numero2 = 0
operacion = ""
continuar = True;
seguir = ""

#Funcion que realice las operacion aritmeticas segun opcion
def operaciones_matematicas(n1,n2,op):
    n1 = float(n1)
    n2 = float(n2)
    
    
    if op == "+":
        print(f"la suma es: {n1+n2}")
    elif op == "-":
        print(f"la resta es: {n1-n2}")
    elif op == "*":
        print(f"la multiplicacion es: {n1*n2}")
    elif op == "/":
        print(f"la division es: {n1/n2}")
    else:
        print("El operador no es valido")
    


while continuar:

    #entrada
    numero1 = input("introduce el primer numero: ") 
    numero2 = input("introduce el segundo numero: ")
    operacion = input("ingrese la operacion: +,-,*./")
    

    while numero1.isnumeric() == False or numero2.isnumeric() == False or operacion not in " +,-,*./ ":
        numero1 = input("introduce el primer numero: ") 
        numero2 = input("introduce el segundo numero: ")
        operacion = input("ingrese la operacion: +,-,*./")
        
    
    operaciones_matematicas(numero1, numero2, operacion)

    seguir = input("¿Quieres continuar? si/no")
    if seguir == "no":
        continuar = False