# Soluzione esercizio "Briscola"

SEMI = "CQFP"
# VALORI = "A234567JQK"
VALORI = "24567JQK3A"

# Acquisizione dei dati

seme_briscola = input("Inserisci il seme della briscola: ").upper()
carta1 = input("Inserisci la prima carta: ").upper()
carta2 = input("Inserisci la seconda carta: ").upper()

# Controllo di validità dei dati
# seme_briscola sia 1 solo carattere tra i 4 permessi

# if len(seme_briscola)==1 and (seme_briscola in "CQFP"):

# if not( len(seme_briscola)==1 and (seme_briscola in "CQFP") ) :

err = False

if len(seme_briscola)!=1 or (seme_briscola not in SEMI):
    print("Seme della briscola non valido")
    err = True

if not(len(carta1)==2 and carta1[0] in VALORI and carta1[1] in SEMI):
    print("Carta 1 non valida")
    err = True

if not(len(carta2)==2 and carta2[0] in VALORI and carta2[1] in SEMI):
    print("Carta 2 non valida")
    err=True

if carta1==carta2:
    print("Carte identiche")
    err = True

# carta1 e carta2 siano di 2 caratteri, il primo un valore valido, il secondo un seme valido

# Controlla chi ha vinto e stampalo

if err:
    exit()
    

if carta1[1]==seme_briscola and carta2[1]!=seme_briscola:
    # caso 1: briscola vs non-briscola
    print(carta1)
elif carta1[1]!=seme_briscola and carta2[1]==seme_briscola:
    # caso 2: non-briscola vs briscola
    print(carta2)
elif carta1[1] != carta2[1]:
    # caso 3: semi diversi
    print(carta1)
else:
    # caso 4: semi uguali (entrambi briscola o entrambi non-briscola, ma uguali)

    # l'idea è di fare
    # if valoredi(carta1[0])>valoredi(carta2[0]):
    # quindi calcolo punti1 e punti2 sarebbero i "valori di" della carte


    # calcolo i punti di carta1
    if carta1[0]=='A':
        punti1 = 11
    elif carta1[0]=='3':
        punti1 = 10
    elif carta1[0]=='J':
        punti1 = 2
    elif carta1[0]=='Q':
        punti1 = 3    
    elif carta1[0]=='K':
        punti1 = 4
    else:
        punti1 = 0

    # calcolo punti2
    if carta2[0]=='A':
        punti2 = 11
    elif carta2[0]=='3':
        punti2 = 10
    elif carta2[0]=='J':
        punti2 = 2
    elif carta2[0]=='Q':
        punti2 = 3    
    elif carta2[0]=='K':
        punti2 = 4
    else:
        punti2 = 0

    if punti1>punti2:
        print(carta1)
    elif punti1<punti2:
        print(carta2)
    else:
        # se arrivo qui, punti1==punti2==0 DI SICURO
        if carta1[0]>carta2[0]: # controllo dei numeri 24567 come stringhe
            print(carta1)
        else:
            print(carta2)


    # caso 4 ALTERNATIVO
    # se i simboli nella stringa VALORI sono riportati in ordine
    # di valore crescente
    #if posizione di carta1[0] in VALORI > posizione di carta2[0] in VALORI:
    if VALORI.index(carta1[0]) > VALORI.index(carta2[0]):
        print(carta1)
    else:
        print(carta2)