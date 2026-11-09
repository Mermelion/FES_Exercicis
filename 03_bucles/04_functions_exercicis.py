###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio} {nom}!")

def saludar_aa(nom):
    print(f"Hola {nom}!")

nombre = input("Introdueix un nom: ")
saludar_a(nombre)
saludar_aa(nombre)

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(numero):
    print("Es parell =", numero % 2 == 0)

es_parell(int(float(input("Introdueix un numero per saber si es parell o no: "))))

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma / len(numeros)

print ("La mitjana dels nombres de la llista es ", mitjana(range(0,101)))

# | UN ALTRE MODE MÉS SENZILL/SIMPLE DE FER-HO (NO SEGUEIX LES INSTRUCCIONS DE L'ENUNCIAT) |
# V                                                                                            V

def mitjana(numeros):
    print("La mitjana dels nombres de la llista és ", sum(numeros) / len(numeros))

mitjana(range(0,101))

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    return sum(args)

print(sumar_tot(*range(1,3)))
print(sumar_tot(*range(1,6)))
print(sumar_tot(*range(1,11)))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().

def taula_multiplicar(numero, limit=10):
    for num in range(0,limit+1):
        print(f"{numero} · {num} = ", numero*num)

taula_multiplicar(int(float(input("Introdueix un numero per saber la seva taula de multiplicar: "))))

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(Nom="Nicola Meloni Martínez", Edat=19, Grau="Telecomunicacions")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.

def factorial():
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

    return fact


def num_max(numbers = [15, 5, 25, 10, 20]):
    nummax = numbers[0]
    for numb in numbers[1:]:
        if nummax < numb:
            nummax = numb
    return nummax

print(factorial(), num_max(), sep=", ")