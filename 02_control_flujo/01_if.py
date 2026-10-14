###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

a = float(input("Escull el valor de A: "))
b = float(input("Escull el valor de B: "))

if a>b:
    print("A és major que B")
elif a<b:
    print("A és menor que B")
else:
    print("A i B són iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

num1 = float(input("Introdueix el primer numero: "))
num2 = float(input("Introdueix el segon numero: "))
op = (input("Introdueix l'operador (+, -, *, /): "))

if op == '+':
    print(f"La suma {num1} + {num2} dona {num1 + num2}.")
elif op == '-': 
    print(f"La resta {num1} - {num2} dona {num1 - num2}.")
elif op == '*':
    print(f"La multiplicació {num1} * {num2} dona {num1 * num2}.")
elif op == '/':
    if num2 == 0:
        print("ERROR: El denominador no pot ser 0")
    else:
        print(f"La divisió {num1} / {num2} dona {num1 / num2}.")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any = int(input("Introdueix un any: "))

if any % 4 == 0 and not (any % 100 == 0 and any % 400 != 0):
    print(f"{any} és un any de traspàs.")
else:
    print(f"{any} NO és un any de traspàs.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(float(input("Introdueix una edat: ")))
while edat < 0:
    print("El valor no pot ser negatiu.")
    edat = int(float(input("Introdueix una edat vàlida: ")))

if 0 <= edat < 3:
    print("Nadó")
elif 3 <= edat < 13:
    print("Infant")
elif 13 <= edat < 18:
    print("Adolescent")
elif 18 <= edat < 65:
    print("Adult")
elif 65 <= edat < 117:
    print("Persona gran")
else:
    print("Presenta't als records guinness! Ets més gran que la persona més longeva del món!")