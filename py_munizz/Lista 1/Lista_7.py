def procura_string(s, lista):
    return s in lista


L = ["AB",  "CD", "EF", "FG"]

print(procura_string("AB", L))
print(procura_string("CD", L))
print(procura_string("EF", L))
print(procura_string("FG", L))
print(procura_string("XYZ", L))