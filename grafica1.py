# Representación de una gráfica
# Javier Burgos. 2019

# Importo los módulos necesarios
import math
import numpy as np                   # Importo el módulo numpy pero lo usaré como np para abreviar
import matplotlib.pyplot as plt      # En plt podemos poner cualquier nombre, pero luego al gráfico lo tenemos que llamar con ese nombre. Matplotlib tiene que estar instalado

# Datos para el gráfico
x = np.array (range(500))*0.1
y = np.zeros (len(x))

for i in range(len(x)):
    y[i] = math.sin(x[i])

# Creamos el gráfico
plt.plot (x,y,'c')      # El caracter indica el color de la función
plt.xlabel("x")
plt.ylabel("y=sin(x)")
plt.title("Representación de una función")
plt.legend(['y=sin(x)'])

# Colores para una función:
# b blue
# g green
# r red
# c cyan
# m magenta
# y yellow
# k black
# w white

plt.text(10,0,"Ey", fontsize=25)
plt.show()      # Para mostrar el gráfico por pantalla
