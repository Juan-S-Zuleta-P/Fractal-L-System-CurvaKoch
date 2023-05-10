import turtle #Importa el módulo de turtle para poder utilizarlo en el código.

axioma = "F" #Axioma inicial para el sistema de Lindenmayer.
reglas = {"F": "F+F-F-F+F"} #Reglas de producción para el sistema de Lindenmayer.

# número de iteraciones que se aplicarán al sistema de Lindenmayer.
iteraciones = 4

# Aplicamos las reglas de producción iterativamente
for i in range(iteraciones): # Itera sobre el número de iteraciones para aplicar las reglas de producción al axioma inicial.
    nueva_cadena = "" #Inicializa una cadena vacía para almacenar el nuevo axioma generado después de aplicar las reglas de producción.
    for caracter in axioma: #Itera sobre cada caracter en el axioma actual y aplica las reglas de producción según corresponda.
        if caracter in reglas:
            nueva_cadena += reglas[caracter]
        else:
            nueva_cadena += caracter
    axioma = nueva_cadena #Asigna el nuevo axioma generado después de aplicar las reglas de producción al axioma actual.

# Dibujamos el fractal utilizando turtle
t = turtle.Turtle() #Crea un objeto de tortuga de la biblioteca de turtle.
t.speed("fastest") # Configura la velocidad de la tortuga en su valor más rápido.t.penup()
for caracter in axioma: #Itera sobre cada caracter en el axioma actual y dibuja la curva de Koch según corresponda.
    if caracter == "F":
        t.forward(5)
    elif caracter == "+":
        t.right(90)
    elif caracter == "-":
        t.left(90)


turtle.done() # presione una tecla para cerrar la ventana
