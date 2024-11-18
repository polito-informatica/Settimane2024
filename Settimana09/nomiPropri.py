"""
Scrivere un codice Python che, dato un testo contenente parole e caratteri vari, si occupi di:
   - Identificare tutti i nomi propri (Parole che iniziano con la maiuscola)
   - Generare una nuova lista con gli stessi nomi scritti al contrario.
   - Ogni nome invertito deve iniziare con una lettera maiuscola seguito da lettere minuscole.
Esempio:

testo = "Ciao a tutti, mi chiamo Anna e lui è Luigi. Paolo è mio fratello, Giovanni è mio cugino."

Il programma deve produrre:

nomi = ['Mario', 'Luigi', 'Paolo', 'Giovanni']
rovescio = ['Oiram', 'Iugil', 'Olaop', 'Innavoig']
"""

import string


testo = "Ciao a tutti, mi chiamo Anna, ho il VAT number, e lui è Luigi. Paolo è mio fratello, Giovanni è mio cugino."

lista_parole = testo.split(" ")
nomi=[]
for parola in lista_parole[1:]:

    if parola[0].isupper() and parola[1:].islower():
    
        parola_filtrata = parola.strip(string.punctuation)
        nomi.append(parola_filtrata)

print(nomi)

nomi_rovesciati = []

for nome in nomi: 

    nome_rovesciato = nome[::-1]
    nomi_rovesciati.append(nome_rovesciato.capitalize())

print(nomi_rovesciati)
