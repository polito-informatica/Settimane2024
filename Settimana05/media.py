# visualizzare la media di un insieme di numeri
# dati in input e uscire se il valore in input è "*"

somma = 0.0 
conteggio = 0
isValid = True
numero = input("Inserire un numero: ")
if numero == "*":
    isValid = False

while isValid:
    print(f'Hai inserito {numero}')

    somma = somma + float(numero)
    conteggio = conteggio + 1

    numero = input("Inserire un numero: ")
    if numero == "*":
        isValid=False

if conteggio == 0:
    print("Non hai inserito alcun numero valido.")
else:
    media = somma / conteggio
    print(media)