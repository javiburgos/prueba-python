# En python absolutamente todo son objetos

number = 5
type (number)   # Podemos usar la funcion type para saber de qué tipo de variable se trata

# Para una variable string podemos usar dobles comillas o triples dobles comillas
mensaje_corto = "Ey buenas, "
mensaje_largo = """Esto es un mensaje
con un salto de línea"""
print(mensaje_corto)
print(mensaje_largo)

num1 = 5
num2 = 7
if num1 > num2:
    print("El número 1 es mayor")
else:
    print("El número 2 es mayor")

# Funciones
# A las funciones en python también se le llaman métodos cuando se encuentran definidas dentro de una clase

# Declaración de la función
def mensaje():
    print("Has llamado a la función mensaje")
    print("Fin de la función")
mensaje()   # Llamada a la función

def suma(num1, num2):
    res = num1+num2
    return res
res = suma(4,18)
print(res)
# Python siempre pasa los valores por referencias

#Listas. (Arrays, vectores)
# En python las listas permiten almacenar varios valores y diferentes tipos de valores
