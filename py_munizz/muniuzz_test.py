print("Programa de energia pau no seu cu")

kwh = int(input("Quantos KWh foi consumido: "))
tipo_base = input("Qual a instalação: ")

if (tipo_base == "r"):
    
    if (kwh <= 500):
        print("O Preco Se Pagar e de R$",kwh * 0.40)
    if (kwh >= 501):
        print("O Preco Se Pagar e de R$",kwh * 0.65)

elif (tipo_base == "i"):
    
     if (kwh <= 1000):
         print("O Preco Se Pagar e de R$",kwh * 0.55)
     if (kwh >= 1001):
         print("O Preco Se Pagar e de R$",kwh * 0.60)

elif (tipo_base == "c"):
    
    if (kwh <= 5000):
        print("O Preco Se Pagar e de R$",kwh * 0.55)
    if (kwh >= 5001):
        print("O Preco Se Pagar e de R$",kwh * 0.60)
        





