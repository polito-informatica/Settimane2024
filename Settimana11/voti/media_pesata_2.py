# Dato il file `voti.txt`, che contiene i voti che uno studente ha acquisito nei vari esami superati,
# si calcoli il valore della "media pesata" per lo studente.
#
# Ciascuna riga del file "voti.txt" contiene 3 campi, separati da spazi: il nome del corso (si assuma privo di spazi),
# il numero di CFU (numero intero positivo), il voto acquisito (numero intero tra 18 e 30)

# media pesata = somma ( voto * CFU ) / somma( CFU )

NOME_FILE_VOTI = 'voti.txt'


def main():
    # Fase 1: leggo i dati dal file in una lista (???)
    voti = leggi_voti(NOME_FILE_VOTI)
    print(voti)

    # Fase 2: a partire dai dati nella lista, calcolo la media
    media_pesata = calcola_media(voti)

    print(media_pesata)

def leggi_voti(nome_file):
    """
    Dato un file, legge i voti in esso contenuti
    """
    voti = []
    f = open(nome_file, 'r', encoding='utf-8')
    for riga in f:
        campi = riga.split()
        voti.append( 
            [
                campi[0],
                int(campi[1]),
                int(campi[2])
            ]
        )

        # voti.append(campi) # solo se tutti i campi fossero stringhe
    f.close()
    return voti

def calcola_media(voti):
    s_cfu = 0
    s_voti_cfu = 0
    for voto in voti:
        s_cfu += voto[1]
        s_voti_cfu += voto[2]*voto[1]
    return s_voti_cfu/s_cfu

main()


# cfu = [8, 10, 10, 8, 10]
# voti = [30, 24, 18, 25, 28]

# voti = [
#     ['Informatica', 8, 30],
#     ['Analisi', 10, 24],
#     ['Chimica', 10, 18],
#     ['...', 8, 25],
#     ['...', 10, 28]
# ]