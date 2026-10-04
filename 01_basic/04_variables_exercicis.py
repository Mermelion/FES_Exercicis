###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom = input("\nIntrodueix el nom de l'encaminador: ")
ubicacio = input("Introdueix la ubicació de l'encaminador: ")
nombre_ports = int(input("Introdueix el nombre de ports: "))
estat = input("Està encès? (sí/no): ")

print("\n")
print(f"Encaminador: {nom}", f"Ubicació: {ubicacio}", f"Nombre de ports: {nombre_ports}", f"Encès?: {estat}", sep = "\n")
print("\n")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

while(input() != "1", "2", "3"):
    print("Selecciona un pla de dades mòbils:\n1. 5GB\n2. 10GB\n3. 20GB\n Selecció:")
    if input() == "1":
        gb_totals = 5
    elif input() == "2":
        gb_totals = 10
    elif input() == "3":
        gb_totals = 20
    else:
        print("Selecció no vàlida. Torna-ho a intentar.")
        continue

    consum = float(input("GB consumits: "))
    restants = gb_totals - consum
    print(f"Queden {restants} GB del teu pla de dades.")

    nou_consum = float(input("Introdueix el nou consum de GB: "))
    restants = restants - nou_consum
    print(f"Queden {restants} GB del teu pla de dades després del nou consum.")