# Creación de un programa de inventario de vehículos.
# Leerá el archivo a través de un módulo denominado csv. Además, realizará una copia profunda de los datos para almacenarlos en la memoria mediante un módulo denominado copy:

import csv
import copy 

# definir el diccionario que funcionará como tipo compuesto para leer los datos tabulares:

myVehicle = {
    "vin" : "<empty>", 
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
    }

# Utilizar un bucle for para recorrer las claves y valores del diccionario:
# La función items () pertenece al tipo de datos de diccionario. La función items() indica al bucle for que recorra la colección que pertenece al tipo de datos de diccionario.

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    

# Defir una lista vacía para almacenar el inventario de vehículos que leerá:
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader: 
        if lineCount == 0:
            print(f'Column names are: {",".join(row)}')
            lineCount += 1
        else: 
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed:{row[5]}, zerSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0] 
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)
            lineCount +=1
    print(f'Processed {lineCount} lines.')   

currentVehicle = copy.deepcopy(myVehicle)      

# Impresión del inventario de vehículos:
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")