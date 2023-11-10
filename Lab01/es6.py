anni = 3
conto = 1000
cont = 0
while cont < anni:
    conto = conto * 1.05
    cont = cont + 1
    print("Saldo anno " + str(cont) + " : " + str(conto))