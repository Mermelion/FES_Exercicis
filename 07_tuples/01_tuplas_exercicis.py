# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.

tupla_ciutats = ("Barcelona", "Berlin", "Birmingham", "Boston", "Bucarest")
print(tupla_ciutats[1], tupla_ciutats[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.

tupla_nums = (0, 3, 1, 3, 2, 3, 3, 4, 5, 6, 7, 8, 9)
tupla_nums.count(3)

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.

def ord_tupla(tupla):
    return tuple(sorted(tupla))

print(ord_tupla(tupla_nums))