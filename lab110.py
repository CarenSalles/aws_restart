# -*- coding: utf-8 -*-
# Crear un script que imprima el string "This is a string."

myString =  "This is a string."
print(myString)

#  Creado una función integrada type() para obtener el tipo de dato de la variable.
print(type(myString))


#Para convertir el valor de retorno del tipo en una cadena, utilice la función integrada str():

print(myString + " is of the data type" + str(type(myString)))

# Trabajar con concatenación de cadenas:

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Utilizará una función integrada denominada input() para obtener información del usuario. La función input() detendrá el código hasta que un usuario escriba una cadena y presione ENTER (Intro):

name = input("what is your name?")
print(name)

# Utilizando la función print() con una sola variable, pero también se puede usar con múltiples variables para dar formato a una cadena:
# La instrucción final print() utiliza la función format(). En la función format(), las llaves de apertura y cierre “{}” actúan como marcadores de posición para las variables que se transmitirán, es decir, se ubicarán entre los paréntesis de la función.

color = input("what is your favorite color? ")
animal = input("what is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))

