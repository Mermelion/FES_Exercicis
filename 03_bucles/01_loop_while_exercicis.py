###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

i=10
while i >= 1:
    print(f"{i}")
    i -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

num = 1
sum = 0
while num <= 20:
    if num % 2 == 0:
        sum += num
    num += 1
print(f"La suma de tots els números parells de l'1 al 20 dona {sum}.")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

j = 0
entrada = -1
while entrada < 0:
    try:
        entrada = int(input("Introdueix un número per saber el seu factorial: "))
        if entrada < 0:
            print("El número ha de ser positiu! Torna-ho  a provar: ")
    except:
        print("Has d'introduir un número enter!")

fact = 1

if entrada not in (0, 1):
    while j < entrada:
            j += 1
            fact = fact * j

print(f"El factorial de {entrada} és {fact}.")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya = ""

while len(contrasenya) < 8:
    contrasenya = input("Introdueix una contrasenya: ")
    if len(contrasenya) < 8:
        print("La contrasenya ha de tenir almenys 8 caràcters!")
print("Contrasenya vàlida.")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

number = -1
while number < 0 or number > 10:
    try:
        number = int(input("Introdueix un número enter del 0 al 10: "))
        if number < 0 or number > 10:
            print("Has d'introduir un número enter del 0 al 10!")
    except:
        print("L'entrada ha de ser un número enter!")

print("··············································")
print("·            TAULA DE MULTIPLICAR            ·")
print("··············································")

k = 0

while k <= 10:
    mult = k*number
    print(f"\n{number} · {k} = {mult}")
    k += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

numero = -1
while numero <= 1:
    try:
        numero = int(input("Introdueix un número enter major que 1: "))
        if numero <= 1:
            print("Has d'introduir un número enter major que 1!")
    except:
        print("L'entrada ha de ser un número!")

v = 2
n_primers = 0

print(f"\nNúmeros primers de l'1 al {numero}:\n")
while v <= numero:
    w = 1
    contador = 0
    while w <= v:
        if v % w == 0:
            contador += 1
        w += 1
    if contador == 2:
        n_primers += 1
        print(f"- {v}\n")
    v += 1
print(f"En total, des de l'1 fins al numero {numero} n'hi ha {n_primers} numeros primers.")

