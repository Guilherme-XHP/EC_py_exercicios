print("Digite os numeros para verificar")

n_faz=0

faz_parte=0

for num in range(0,10):
    
    num = int(input("Digite um número : "))

    if(num>=10 and num<=20):

        faz_parte= faz_parte + 1

    else:

        n_faz= n_faz + 1

print("São: ",faz_parte,"números que estão dentro do intervalo[10,20]")
print("São: ",n_faz,"números que estão fora do intervalo[10,20]")