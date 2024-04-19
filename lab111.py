# Crear un script en Python para almacenar una colección de nombres de frutas o una lista: 

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Accesar a una lista por posición. El posicionamiento en una lista comienza en el cero (0). Los corchetes indican a Python qué posición en la lista desea:

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

# Modificación de los valores de una lista. Los valores de una lista se pueden cambiar fácilmente. Para hacer esto, simplemente asigna una nueva cadena o valor a la posición que desea modificar:

myFruitList[2] = "orange"
print(myFruitList)

# Definición de una tupla => Una tupla es similar a una lista, pero no se puede cambiar. Un tipo de dato que no se puede cambiar después de su creación se conoce como inmutable. Para definir una tupla, se utilizan paréntesis en lugar de corchetes ([]). Creando una tupla: 

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Acceder una tupla por posición:
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Definición de un diccionario => Un diccionario es una lista cuyas posiciones tienen nombres asignados (claves). Imagine que su lista muestra la fruta favorita de distintas personas.

myFavoriteFruitDictionary = {"Akua" : "apple", "Saanvi" : "banana", "Paulo" : "pineapple"}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Acceder al diccionario por nombre, en lugar de utilizar números, recurrirá al nombre de las personas para acceder a su fruta favorita:
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

