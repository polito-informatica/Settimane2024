# chiedere in input un numero da 1 a 10
# se diverso, chiedere nuovamente il numero in input

numero = int(input("Inserisci un numero: "))

"""
if numero < 1 or numero > 10: 
    print("Errore... riprova!")
    numero = int(input("Inserisci un numero: "))
    if numero < 1 or numero > 10: 
        print("Errore... riprova!")
        numero = int(input("Inserisci un numero: "))
"""
while numero < 1 or numero > 10:
    print("Errore... riprova!")
    numero = int(input("Inserisci un numero: "))


print(numero)