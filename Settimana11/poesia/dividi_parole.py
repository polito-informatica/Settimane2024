# leggere il file "apelle.txt" e creare un nuovo file
# "parole_apelle.txt" che contiene le stesse parole,
# una per riga.
# Spazi e punteggiatura vanno ignorati (soppressi).

import string

NOME_FILE_POESIA = 'apelle.txt'

f_in = open(NOME_FILE_POESIA, 'r', encoding='utf-8')
f_out = open('parole_'+NOME_FILE_POESIA, 'w', encoding='utf-8')

for riga in f_in:
    parole = riga.rstrip('\n').split()
    # parole è lista di sequenze di caratteri prive di spazi
    # tendenzialmente saranno parole, eventualmente circondate
    # da simboli di punteggiatura
 
    # se voglio lasciare la riga vuota nel file di uscita
    # if parole == []:
    #     print()

    for parola in parole:
        parola = parola.strip(string.punctuation)

        # problema apostrofi

        # Primo caso: separa le parole con apostrofo interno (parzialmente funzionante)
        # if "'" in parola:
        #     parola_divisa = parola.split("'")
        #     for pezzo in parola_divisa:
        #         print(pezzo)
        # else:
        #     print(parola)

        # elimina apostrofi interni come se non ci fossero mai stati
        parola = parola.replace("'", "")

        # print(parola, file=f_out)
        f_out.write(parola+'\n')

    # print('---')


f_in.close()
f_out.close()