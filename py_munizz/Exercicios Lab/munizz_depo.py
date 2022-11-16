depo = float(input("Qual o deposito atual: "))
taxa = float(input("Tada de: (3 para 3%)"))
mes = 1
saldo = depo
while mes <= 24:
    saldo=saldo+(saldo*(taxa/100))
    print("O saldo do mes {mes} e de R$: ", saldo)
    mes = mes+1

print("Ganho de ", saldo - depo)
