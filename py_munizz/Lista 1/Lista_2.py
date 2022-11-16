list = [-10,-8,0,1,2,5,-2,-4]

min = list[0]

soma = 0

for e in list:

    if e < min:

        min = e
        
print(f"Temperatura mínima: {min} °C")