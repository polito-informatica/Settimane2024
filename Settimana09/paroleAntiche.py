"""
Nella lingua di una strana tribù antica,
le parole vengono scritte separando le consonanti dalle vocali,
in particolare per ciascuna parola si scrivono per prime tutte le consonanti,
e poi tutte le vocali.
Quindi la frase italiana "prova in itinere" verrebbe scritta come
"prvoa ni tnriiee"

Si scriva un frammento di codice Python che,
data una stringa di testo memorizzata nella variabile 'frase',
la trasformi in una stringa scritta secondo le regole della lingua
della tribù antica.
Si supponga che le lettere siano tutte minuscole.
Si memorizzi la stringa risultante nella variabile 'antica'.

(Suggerimento: può essere comodo trasformare la frase in una lista di stringhe,
come passaggio intermedio).
"""
VOCALI = "aeiou"
CONSONANTI = "bcdfghjklmnpqrstvwxyz"

frase = "noi studiamo ingegneria"
lista_parole = frase.split(" ")
frase_antica=""
for parola in lista_parole: 
    #lista_vocali=[]
    #lista_consonanti=[]
    vocali=""
    consonanti=""
    for lettera in parola:
        if lettera in VOCALI:
            #lista_vocali.append(lettera)
            vocali = vocali + lettera
        elif lettera in CONSONANTI:
            #lista_consonanti.append(lettera)
            consonanti = consonanti + lettera
    parola_antica = consonanti + vocali
    #lista_consonanti + lista_vocali
    #print("".join(parola_antica))
    frase_antica = frase_antica + parola_antica + " "
print(frase_antica)
