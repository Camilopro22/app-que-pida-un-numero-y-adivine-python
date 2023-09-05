#Aplicacion de adivinar un numero.
import random

intentos_realizados = 0

print("hola, ¿como te llamas?  ")
mi_nombre = input()

numero = random.randint(1, 100)
print(" bueno "  +  mi_nombre  +  "estoy pensando en un numero entre 1 y 100. ")

while intentos_realizados <6:
    print("intenta adivinar.")
    estimacion = input()
    estimacion = int(estimacion)

    intentos_realizados = intentos_realizados + 1

    if estimacion < numero:
        print("tu estimacion es muy baja.")

    if estimacion > numero:
        print("tu estimacion es muy alta.")

    if estimacion == numero:
        break

if estimacion == numero:
    intentos_realizados = str(intentos_realizados)
    print("buen trabajo," + "has adivinado mi numero en" + intentos_realizados + "intentos!")

if estimacion != numero:
    numero = str(numero)
    print("pues no. el numero que estaba pensando era" + numero)

