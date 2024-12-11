"""
Leggi le informazioni sugli studenti (matricola, cognome, nome, cdl)
e costruisci una lista di record (=dizionari)

Stampiamo gli studenti divisi per corso di studi
"""

import csv
import operator


def main():
    studenti = leggi_studenti('14BHDOA_2024_shuffled.csv')

    # elenco dei corsi di studio
    cdl = set()
    for studente in studenti:
        cdl.add(studente['cdl'])

    cdl_sorted = sorted(cdl)

    # cdl = { studente['cdl'] for studente in studenti }

    print(cdl_sorted)

    for corso in cdl_sorted:
        studenti_cdl = []
        print('*'*20, corso, '*'* 20)
        for studente in studenti:
            if studente['cdl'] == corso:
                studenti_cdl.append(studente)
                print(f"{studente['cognome']} {studente['nome']}")

        # studenti_cdl = [ studente for studente in studenti if studente['cdl']==corso ]

def per_cognome(studente):
    return studente['cognome']

def per_lunghezza_cognome(studente):
    return len(studente['cognome'])

def per_cognome_nome(studente):
    # return studente['cognome'] + ' ' + studente['nome']
    return (studente['cognome'], studente['nome'])


def leggi_studenti_altra(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')
    studenti = []
    reader = csv.DictReader(f)
    for record in reader:
        studenti.append(record)
    f.close()
    print(studenti)
    return studenti

def leggi_studenti(nome_file):
    studenti = []

    with open(nome_file, 'r', encoding='utf-8') as f:

        f.readline() # salta la prima riga

        for riga in f:
            campi = riga.rstrip('\n').split(',')

            studente = {
                'matricola': int(campi[0]),
                'cognome': campi[1],
                'nome': campi[2],
                'cdl': campi[6]
            }

            studenti.append(studente)


    studenti.sort(key=per_cognome)
    studenti.sort(key=operator.itemgetter('cognome'))

    return studenti



main()