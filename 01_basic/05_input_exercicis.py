###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

print("Introdueix el nom del tècnic i el nom de la xarxa que està instal·lant.")
nom_tecnic = input("Nom del tècnic: ")
nom_xarxa = input("Nom de la xarxa: ")

print(f"El tècnic {nom_tecnic} està instal·lant la xarxa {nom_xarxa}.")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

print("\nIntrodueix la longitud de l'enllaç de fibra i la velocitat de transmissió.")
longitud_km = float(input("Longitud de l'enllaç (km): "))
velocitat_Gbps = float(input("Velocitat de transmissió (Gbps): "))
segons_per_GB = (8 / velocitat_Gbps)  # Temps en segons per transmetre 1 GB
print(f"Caldrien {segons_per_GB:.2f} segons per transmetre 1 GB de dades a {velocitat_Gbps} Gbps.")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

print("\nIntrodueix les hores de feina, el preu per hora i el preu del material.")
hores_feina = float(input("Hores de feina: "))
preu_hora = float(input("Preu per hora: "))
preu_material = float(input("Preu del material: "))

cost_total = (hores_feina * preu_hora) + preu_material
print(f"El cost total de la instal·lació és de {cost_total} €.")