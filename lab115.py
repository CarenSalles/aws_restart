# Trabajo con bucles
# Un bucle while hace que una sección del código se repita hasta que se cumpla una determinada condición. En este ejercicio, creará un script en Python que pedirá al usuario adivinar un número.

 # función print() para informar al usuario acerca del juego:
print( "Welcome to guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#  Utilizará el comando import para incluir el código que escribió otra persona. Hasta ahora, ha utilizado funciones integradas. Recuerde que una función es un fragmento de código reutilizable:
# Al inicio del archivo, incluya el módulo de Python (que es un tipo de biblioteca) llamado random.Las instrucciones import se colocan al inicio del script por convención:

import random
# Luego, escriba una instrucción que generará un número aleatorio entre 1 y 10 mediante el uso de la función randint() del módulo random.
number = random.randint(1,10)

# Monitoree si el usuario adivinó su número con la creación de una variable llamada isGuessRight:

isGuessRight = False
# Para gestionar la lógica del juego, cree un bucle while:
# Si el usuario no ha adivinado la respuesta correcta, ingrese el bucle.

"""Pida al usuario que adivine el número.

¿Es el número correcto?

Si la respuesta es correcta, dígaselo al usuario y salga del bucle.

Si no ha adivinado el número, indique al usuario que fue una suposición incorrecta y continúe con el bucle. """

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))