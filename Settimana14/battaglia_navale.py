# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

"""

Tabella in cui memorizzo la posizione delle navi

navi = [ 
    [0, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    ... 10 righe
]

Tabella in cui memorizzo i colpi andati a vuoto oppure che hanno colpito

colpi = [
                            [ 0 non provato, 1 acqua, 2 colpito ],
                            [ ' ' non provato, 'o' acqua, '*' colpito ],  <-- questa
    [ ' ', ' ', ' ', 'o', 'o', ' ', '*' ]
    [ ' ', ' ', ' ', 'o', 'o', ' ', '*' ]
    ... 10 righe
]

mosse = [  # lista di stringhe
    'A,1',
    'F,5',
    'A,4'
]

mosse = [  # lista di coppie (liste da 2 o tuple da 2)   <--- questa
    ['A', '1'],
    ['F', '5'],
    ['A', '4']
]

mosse = [  # lista di coppie di INTERI (liste da 2 o tuple da 2) già corrispondenti a righe e colonne
    [1, 1],
    [6, 5],
    [1, 4]
]

"""

from pprint import pprint


def leggi_navi(nome_file):
    navi = []
    with open(nome_file, "r") as f:
        for riga in f:
            campi = riga.strip().split(",")
            numeri = []
            for campo in campi:
                if campo == "":
                    numeri.append(0)
                else:
                    numeri.append(int(campo))
            navi.append(numeri)
    return navi


def crea_colpi_vuoti():
    colpi = []
    for r in range(10):
        riga = [" "] * 10
        colpi.append(riga)
    return colpi


def leggi_mosse(nome_file):
    mosse = []
    with open(nome_file, "r") as f:
        for riga in f:
            campi = riga.strip().split(",")
            mosse.append(campi)
    return mosse


def controlla_mossa(mossa, navi, colpi):
    # mossa = [ 'A', '7' ]  -> riga = 1-1, col = 7-1
    riga = ord(mossa[0]) - ord("A")
    col = int(mossa[1]) - 1

    if navi[riga][col] != 0:
        esito = "Colpito"
        colpi[riga][col] = "*"
    else:
        esito = "Acqua"
        colpi[riga][col] = "o"

    return esito


def controlla_fine_gioco(navi, colpi):
    for riga in range(len(navi)):
        for col in range(len(navi[riga])):
            if navi[riga][col] != 0 and colpi[riga][col] != "*":
                return False
    return True


def stampa_colpi(colpi):
    print("  | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|")
    print("_" * 33)
    for riga in range(len(colpi)):
        carattere = chr(ord("A") + riga)
        print(f"{carattere} |", end="")
        for col in range(len(colpi[riga])):
            print(f"{colpi[riga][col]} |", end="")
        print()
        print("_" * 33)


def main():
    nome_navi1 = input("Giocatore 1: inserisci il nome del file: ")
    nome_navi2 = input("Giocatore 2: inserisci il nome del file: ")

    navi1 = leggi_navi(nome_navi1)
    navi2 = leggi_navi(nome_navi2)

    # pprint(navi1)
    # pprint(navi2)

    colpi1 = crea_colpi_vuoti()
    colpi2 = crea_colpi_vuoti()

    # pprint(colpi1)
    # pprint(colpi2)

    mosse = leggi_mosse("mosse.txt")
    # pprint(mosse)

    fine_gioco = False

    i = 0
    while i < len(mosse) and fine_gioco is False:

        mossa = mosse[i]

        if i % 2 == 0:
            # giocatore 1 (indice 'i' pari)
            print("È turno del giocatore 1")
            print(f"Coordinate dell'attacco: {mossa[0]}, {mossa[1]}")
            # gioca la mossa su 'navi2' e salva l'esito in 'colpi2'
            esito = controlla_mossa(mossa, navi2, colpi2)
            # stampa l'esito e la tabella 'colpi2'
            print(esito)
            stampa_colpi(colpi2)
            fine_gioco = controlla_fine_gioco(navi2, colpi2)
        else:
            # giocatore 2 (indice 'i' dispari)
            print("È turno del giocatore 2")
            print(f"Coordinate dell'attacco: {mossa[0]}, {mossa[1]}")
            # gioca la mossa su 'navi1' e salva l'esito in 'colpi1'
            esito = controlla_mossa(mossa, navi1, colpi1)
            # stampa l'esito e la tabella 'colpi1'
            print(esito)
            stampa_colpi(colpi1)
            fine_gioco = controlla_fine_gioco(navi1, colpi1)

        i = i + 1


main()
