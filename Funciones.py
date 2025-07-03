
def saludar():
    #Este es el bloque de codigo que pertenece a la funcion de saludar.
    nombre = "Olivia"
    print("Hola " +nombre)
    
    
    #invocacion de funcion en python siempre con los parentesis.
saludar()


def ver_numero():
    return 150


a = 10;b=5;c=a+b

suma = c + ver_numero()

print("La suma es " ,suma)

#Funcion con parametro de entrada
def saludoCustom(saludo):
    print(saludo)
    
saludoCustom("Buenas tardes")

#Funcion con multiples parametros de entrada
def datosCliente(nombre,apellido,email,telefono):
    datos_cliente = f"nombre: {nombre}. Apellido: {apellido}, Email: {email}, Telefono {telefono}";
    print(datos_cliente)
    
datosCliente("Jorge","Perez","jperez@email.com" ,678544122)
