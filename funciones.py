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
mi_lista = ["Hola","manzana","calculadora", 3.14159, 18]
mi_lista.append("Palabra final")            # Agrega un elemento al final de la lista
mi_lista.insert(0,"Muse")                   # Agregamos un elemento en la posición de índice 0 (se empieza a contar en cero)
mi_lista.remove("manzana")                  # Para eliminar un elemento de la lista. También se puede escribir el índice.
mi_lista.pop()                              # Elimina el último elemento de la lista
print (mi_lista)
print(mi_lista.index("Muse"))               # Para mostrar en qué índice se encuentra el elemento "Muse"
print("Muse" in mi_lista)                   # Devuelve True o False según si el elemento "Muse" se encuentra en "mi_lista"
mi_lista *= 3                               # Repite 3 veces los elementos de la lista
print(mi_lista)

# Tuplas. Las tuplas son listas inmutables, no se pueden modificar después de su cración.
# Tampoco se permiten búsquedas, pero sí se permite comprobar si un elemento se encuentra en la tupla
# Una tupla se va a ejecutar más rápido que una lista, además de que ocupa menos espacio.
