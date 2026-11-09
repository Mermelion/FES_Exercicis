###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.

for parells in range(2,21,2):
    print(f"{parells}")

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.

mitjana = 0

for num in numeros:
    mitjana += num

mitjana /= len(numeros)
print(f"{mitjana}")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
numbers = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.

nummax = 0

for numb in numbers:
    if nummax < numb:
        nummax = numb

print(f"{nummax}")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.

m5 = [word for word in paraules if len(word) > 5]
print(f"{m5}")

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
words = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).

lletra = input("Introdueix una lletra: ").lower()
sum = 0
for lletres in words:
    if lletres.startswith(lletra):
        sum += 1
print(f"Hi ha {sum} paraules que comencin amb la lletra {lletra}.")
