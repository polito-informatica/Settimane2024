"""Quante volte compare ciascuna parola?"""
import string

def main():
    parole = leggi_parole('story.txt')
    #  print(parole)

    frequenze = {}
    for parola in parole:
         if parola in frequenze:
              frequenze[parola] = frequenze[parola]+1
         else:
              frequenze[parola] = 1
    # print(frequenze)
    # for parola in sorted(frequenze):
    #      print(f'{parola} - {frequenze[parola]}')

    # per stampare in ordine di freq descrescente
    # mi faccio una lista di liste
    #  [ [ frequenza, parola ], [frequenza, parola], ...]
    coppie = []
    for parola, frequenza in frequenze.items():
         coppie.append( [frequenza, parola] )
    coppie.sort(reverse=True)
    print(coppie[:20])

def leggi_parole(nome_file):
    """
    Legge tutte le parole contenute nel file di cui è specificato
    in mome in nome_file, e restituisce una lista con tutte
    le parole.

    Le parole sono tutte considerate minuscole e la punteggiatura
    viene ignorata.
    """
    parole = []
    f = open(nome_file, 'r', encoding='utf-8')
    for riga in f:
        campi = riga.rstrip('\n').replace('-', ' ').split()
        for campo in campi:
                p = campo.lower().strip(string.punctuation) 
                if p: # non aggiungere parole vuote ''
                    parole.append( p )
    f.close()
    return parole    


main()