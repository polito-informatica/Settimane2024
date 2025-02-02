# Soluzione proposta tema d'esame "Akinator"

import random
import string

LIVELLI = ["facile", "medio", "difficile"]


def parola_segreta(livello):

    # leggi tutte le parole del livello selezionato
    nome_file = livello + ".txt"
    parole = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for line in f:
            parole.append(line.strip())

    # scegli una delle parole
    segreto = random.choice(parole)
    # print(f'Parola segreta: {segreto}')
    return segreto


def gioca_partita(livello):
    segreto = parola_segreta(livello)  # parola da indovinare, come stringa (es: 'ciao')

    # spacchetta la parola in una lista, con una lettera per ciascuna posizione [ 'c', 'i', 'a', 'o']
    lettere_segreto = list(segreto)
    # preparo una lista con tutte '_'
    lettere_indovinate = ["_"] * len(lettere_segreto)

    # spacchetta la parola in una lista, con una lettera per ciascuna posizione [ 'c', 'i', 'a', 'o']
    alfabeto = list(string.ascii_lowercase)

    # rimescolo in ordine casuale tale stringa: sarà l'ordine con cui faccio i tentativi
    random.shuffle(alfabeto)
    # print(alfabeto)

    punti = 10
    trovato = False

    # ciclo di gioco
    while punti > 0 and not trovato:

        print(
            f'Punti {punti} - La parola da indovinare è: {" ".join(lettere_indovinate)}'
        )

        lettera = alfabeto.pop()  # prossima lettera da tentare
        print(f"    Lettera scelta dal bot: {lettera}")

        if lettera in lettere_segreto:  # lettera indovinata oppure no?
            print(f"    Lettera {lettera} presente")

            # sostituisco i trattini con la lettera
            for i in range(len(lettere_segreto)):
                if lettere_segreto[i] == lettera:
                    lettere_indovinate[i] = lettera
            # vedo se ho vinto
            if "_" not in lettere_indovinate:
                print(
                    f"Complimenti, il bot ha vinto! la parola {segreto} è stata indovinata correttamente"
                )
                trovato = True

        else:
            print(f"    Lettera {lettera} non presente")
            punti = punti - 1
            if punti == 0:
                print(
                    f"Peccato, il bot ha perso! La parola da indovinare era {segreto}"
                )

    return trovato  # sono uscito perché ho vinto?


def main():
    n_partita = 1
    continua_partita = True
    partite_vinte = 0
    partire_perse = 0

    while continua_partita:

        print(f"Partita numero {n_partita}")

        livello = random.choice(LIVELLI)  # scegli a caso uno dei 2 liveli
        print(f"Il bot seleziona la difficoltà: {livello}")

        vittoria = gioca_partita(livello)
        if vittoria:

            partite_vinte = partite_vinte + 1
        else:
            partire_perse = partire_perse + 1

        # fine partita, vedi se continuare
        risp = input("Vuoi continuare a giocare?[S|N] ")
        if risp.strip().upper() == "N":
            continua_partita = False
        n_partita += 1

    print("SESSIONE TERMINATA")
    print(f"    Il bot ha vinto {partite_vinte} partita/e")
    print(f"    Il bot ha perso {partire_perse} partita/e")


main()
