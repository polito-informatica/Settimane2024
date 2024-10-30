lista_vuota = []
numeri = [1, 3, 45, 900]

numeri[0] = 34 # riassegna il valore all'indice 0 
numero = numeri[0] # legge il valore all'indice 0 e lo assegna ad un'altra variabile
nuova_lista = [6] # crea una lista e la inizializza con il solo elemento 6

lucky = ['star', 13, 17, '🍀', "zzz"]

# pericoloso perché non c'è legame tra la dimensione del range e la lunghezza della lista
#for i in range(2):
#    print(lucky[i])

for i in range(len(lucky)):
    print(lucky[i])

print()

for element in lucky:
    print(element)

print()

for i, element in enumerate(lucky):
    print(i, element)

