Before = [1, 2, 5, 6, 9]
After = [1, 2, 8, 10]

conjB = set(Before)
conjA = set(After)

# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print("Antes:", Before)
print("Depois:", After)
print("Elementos que não mudaram: ", conjB & conjA)
print("Elementos novos", conjA - conjB)
print("Elementos que foram removidos", conjB - conjA)
