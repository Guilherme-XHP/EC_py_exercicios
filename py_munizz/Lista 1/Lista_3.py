list1 = [1, 2, 6, 8]
list2 = [3, 6, 8, 9]

print(f"Lista 1: {list1}")
print(f"Lista 2: {list2}")

conj1 = set(list1)
conj2 = set(list2)


print("Os valores comuns às duas listas:", conj1 & conj2)
print("Os valores que só existem na primeira:", conj1 - conj1)
print("Os valores que só existem na segunda:", conj2 - conj1)
print("Elementos não repetidos nas duas listas:", conj1 ^ conj2)
print("Primeira lista, sem os elementos repetidos na segunda:", conj1 - conj2)