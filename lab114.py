# Trabajo con condicionales: 
# la función input() para obtener información del usuario:

userReply = input("Do you need to ship a package? (Enter yes or no)")
# Utilice la instrucción if para mostrar una respuesta.

# Las instrucciones de una declaración if deben mantener una sangría de un tabulador, debajo de la instrucción if. En otros lenguajes de programación, a menudo se utilizan corchetes ({}) para indicar el inicio y el final de un bloque lógico, pero Python utiliza espaciado:
# El símbolo == es un operador de comparación. Significa es igual a.
if userReply == "yes": 
    print("We can help you ship that package!")

# Trabajo con la instrucción else
# La instrucción else se utiliza para especificar una acción alternativa si la condición especificada en la instrucción if no se cumple.
else: 
    print("Please come back when you need to ship a package. Thank you.")

# Crear script de Python ofreciendo al usuario servicios adicionales. Cuando tenga varias condiciones, puede utilizar la instrucción elif, que es la abreviatura de else-if:
# La instrucción elif siempre va después de la instrucción if y antes de la instrucción else.
# Las instrucciones if, elif y else permiten que se ejecute solo una ruta a la vez. El programa no comprueba las demás instrucciones luego de encontrar una condición que es verdadera.

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy)")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number)")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")    

