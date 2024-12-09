import string


STORIA = 'story.txt'
DIZIONARIO = 'words.txt'


def main():
    storia = leggi_parole(STORIA)
    print(storia)
    dizionario = leggi_parole(DIZIONARIO)
    errori = storia.difference(dizionario)
    print(errori)


def leggi_parole(nome_file):
    """
    Legge tutte le parole contenute nel file di cui è specificato
    in mome in nome_file, e restituisce un insieme con tutte
    le parole univoche.

    Le parole sono tutte considerate minuscole e la punteggiatura
    viene ignorata.
    """
    parole = set()
    f = open(nome_file, 'r', encoding='utf-8')
    for riga in f:
        campi = riga.rstrip('\n').split()
        for campo in campi:
            
            
            if '-' in campo:
                ## se c'è uno o più trattini '-' '--', dividi il campo e ripeti la rimozione della punteggiatura
                frammenti = campo.split('-')
                for frammento in frammenti:
                    p = frammento.lower().strip(string.punctuation) 
                    if p: # non aggiungere parole vuote ''
                        parole.add( p )
            else:
                p = campo.lower().strip(string.punctuation) 
                if p: # non aggiungere parole vuote ''
                    parole.add( p )
    f.close()
    return parole    


main()

