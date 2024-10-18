# creare un programma che legge in input 10 numeri
# e che si ferma se viene dato in input il numero 0

i = 0
numero = int(input(f"Inserisci il {i+1}o numero: "))

continua = numero!=0
#esci = numero==0

while i < 9 and continua:
    
    print(f"Hai inserito {numero}")

    i = i + 1
    numero = int(input(f"Inserisci il {i+1}o numero: "))
    if continua:
        print("Errore, dovrei proprio uscire dal ciclo")
    
print(f"Hai inserito {numero}")

