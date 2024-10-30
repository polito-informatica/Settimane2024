"""
Si scriva un programma che
- acquisisca da tastiera un numero intero positivo N 
- acquisisca da tastiera N frasi (una per riga) composte da più parole
- per ciascuna frase, indentifichi i nomi propri presenti
(i nomi propri hanno la prima lettera maiuscola, le altre minuscole)
Xxxxx

VARIANTE 1: si stampino tutti i nomi propri incontrati
VARIANTE 2: si stampi solo il primo nome proprio incontrato su ciascuna riga
VARIANTE 3: si stampi solo la prima occorrenza di ciascun nome proprio incontrato su ciascuna riga

"""

#frase = "oggi Ginevra sta andando alla festa con Luigi e Ginevra."

import string


N = int(input("Inserisci un numero: "))
variante = int(input("Scegli una variante tra 1, 2 e 3:"))

for i in range(N):
    frase = input("Inserisci una frase: ")

    if variante == 2:
        conta_nomi_propri = 0

    if variante == 3:
        lista_nomi = []
    for i in range(len(frase)):
        if frase[i].isupper():
            #print(frase[i], i)
            if (i == 0 or not frase[i-1].isalnum()) and (frase[i+1].isalpha() and frase[i+1].islower()):
                #print("Abbiamo trovato l'inizio di un nome proprio!")

                j = i + 1
                while j < len(frase) and frase[j] not in " ,;'." and frase[j].islower():
                    j = j + 1
                
                if variante == 2:
                    conta_nomi_propri = conta_nomi_propri + 1
                    print("Conta nomi propri:", conta_nomi_propri)

                if variante == 1:
                    print("Nome proprio:", frase[i:j])
                elif variante == 2:
                    if conta_nomi_propri == 1:
                        print("Nome proprio:", frase[i:j])
                elif variante == 3:
                    if frase[i:j] not in lista_nomi:
                        print("Nome proprio:", frase[i:j])
                                        
                    lista_nomi.append(frase[i:j])
                
                print("Lista dei nomi:", lista_nomi)