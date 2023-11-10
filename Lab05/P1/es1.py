PIN_correct = "5983"
cont = 0
tentativo = False
while cont != 3 and tentativo == False:
    PIN = input("Digitare il PIN (4 cifre)")
    if(PIN == PIN_correct):
        tentativo = True
        print("Your PIN is correct")
    else:
        print("Your PIN is incorrect")
        cont = cont + 1
        tentativo = False
if(cont == 3):
    print("Your bank card is blocked")


