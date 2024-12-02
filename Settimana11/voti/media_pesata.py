# Dato il file `voti.txt`, che contiene i voti che uno studente ha acquisito nei vari esami superati,
# si calcoli il valore della "media pesata" per lo studente.
#
# Ciascuna riga del file "voti.txt" contiene 3 campi, separati da spazi: il nome del corso (si assuma privo di spazi),
# il numero di CFU (numero intero positivo), il voto acquisito (numero intero tra 18 e 30)

# media pesata = somma ( voto * CFU ) / somma( CFU )

NOME_FILE_VOTI = 'voti.txt'

f = open(NOME_FILE_VOTI, 'r', encoding='utf-8')

somma_voti_cfu = 0
somma_cfu = 0

for riga in f:
    campi = riga.split()
    # print(campi)
    cfu = int(campi[1])
    voto = int(campi[2])

    somma_voti_cfu += voto * cfu
    somma_cfu += cfu

media_pesata = somma_voti_cfu / somma_cfu

print(f"Media pesata: {media_pesata:.2f}")

f.close()