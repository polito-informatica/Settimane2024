nome = "Giovanna"

for lettera in nome:
    print(lettera)

#i = 0
#while i < len(nome):
#    letter = nome[i]
#    print(letter)
#    i = i + 1

for i in range(len(nome)):
    print(i)

i = 0
for carattere in nome:
    print(i)
    i = i + 1

for indice, carattere in enumerate(nome):
    print(indice, carattere)
