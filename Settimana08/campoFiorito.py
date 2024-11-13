"""
Consideriamo il gioco del Campo Fiorito,
in cui in una griglia quadrata di NxN caselle di prato sono presenti M fiori.

🐝 Chi gioca deve scoprire tutte le caselle che contengono fiori,
evitando di perdere tempo esplorando quelle che invece contengono solo una zolla d'erba.

Il programma deve innanzitutto creare una matrice NxN e posizionare
gli M fiori in posizioni casuali (distinte tra loro).
I fiori possono essere rappresentati da un valore Booleano True/False.

In seguito, il programma calcoli una matrice NxN di numeri interi,
in cui ciascuna cella contenga il numero di fiori presenti
nelle 8 celle adiacenti (se esistono).
Si stampi il contenuto di queste due matrici,
per verificare la correttezza dei calcoli.

Si permetta poi all'utente di selezionare una casella
(inserendone le coordinate di riga e colonna).
In funzione del contenuto di tale casella, sono possibili i 
seguenti tre casi:
- casella già selezionata in precedenza: si stampi un messaggio di errore
- casella contenente una zolla d'erba: si stampi un messaggio di sconfitta, e il numero di fiori nelle caselle adiacenti
- casella contenente un fiore: si stampi il numero di fiori trovati fino a quel momento

Esempio:
🟢🟢🟢🟢  1110
🟢🌸🟢🟢  2121
🌸🟢🟢🌸  1331
🟢🟢🌸🟢  1212

[[False, False, False, False],
[False, True, False, False],
...]

"prato", "prato","prato","prato"
"prato","fiore","prato","prato".
...
"""

# larghezza == lunghezza della mappa
#N = int(input("Inserire dimensione mappa: "))
from random import randint


N = 4

# numero di fiori
#M = int(input("inserire numero di fiori: "))
M = 8

mappa = [] 

for i in range(N):
    mappa.append([False]*N)

for i in range(M):
    c = randint(0, N-1)
    r = randint(0, N-1)

    while mappa[r][c]:
        c = randint(0, N-1)
        r = randint(0, N-1)

    mappa[r][c] = True

vicini = []
for i in range(N):
    vicini.append([0]*N)

for r in range(N):
    for c in range(N):

        # conta vicini
        conta=0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):

                if 0 <= i < N and 0 <= j < N and not(i==r and j==c):
                    if mappa[i][j]:
                        conta = conta + 1

        vicini[r][c]=conta


# visualizza la mappa
for i in range(N):
    for j in range(N):
        if mappa[i][j]:
            print("🌸", end="")
        else:
            print("🟢", end="")
    print()

# visualizza la mappa
for i in range(N):
    for j in range(N):
        print(vicini[i][j], end="")
    print()
