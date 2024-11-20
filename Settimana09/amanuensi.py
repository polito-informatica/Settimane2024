"""
Amanuensi 🖋️

In un recondito monastero, gli e e le amanuensi hanno il compito di custodire la conoscenza sottoforma di manoscritti cartacei, ricopiando a mano noti testi letterari da varie fonti. 
Questi sono raccolti in libri organizzati per tema, che devono essere custoditi inalterati.
Ma il monastero incoraggia anche a prendere spunto dai testi, per poi modificarli e crearne di nuovi.
Inoltre, è importante crearne delle copie da spedire ai monasteri di tutto il mondo, per quanto più diffonderne gli importanti contenuti culturali.

Creare un programma che permetta di:
- organizzare i testi all'interno di libri tematici, dove i testi siano accessibili riga per riga
- analizzare i libri, elaborando il numero di manoscritti, di righe e di caratteri che contengono
- creare nuove versioni modificate dei manoscritti, garantendo che i libri originali restino inalterati
- creare copie dei libri da mandare ad altri monasteri, garantendo che i libri originali restino inalterati
"""

import copy

# Definizione delle funzioni 

def crea_libro(lista):
    # Organizza i manoscritti in un libro tematico, rendendo ogni testo accessibile riga per riga
    libro_elaborato = []
    for manoscritto in lista:
        # Divide il manoscritto in una lista di righe
        manoscritto_elaborato = manoscritto.split("\n")
        libro_elaborato.append(manoscritto_elaborato)
    return libro_elaborato

def analisi_libro(qualunque_libro):
    # Analizza il libro calcolando il numero di manoscritti, righe e caratteri
    n_manoscritti = len(qualunque_libro)
    n_righe = 0
    n_caratteri = 0
    for manoscritto in qualunque_libro:
        n_righe += len(manoscritto)
        for riga in manoscritto:
            n_caratteri += len(riga)
    print(f"Il libro contiene {n_manoscritti} manoscritti, {n_righe} righe e {n_caratteri} caratteri.")
    return n_manoscritti, n_righe, n_caratteri

def modifica_manoscritto(manoscritto, operazione):
    # Crea una nuova versione modificata del manoscritto senza alterare l'originale
    if operazione == "A":
        # Aggiunge una riga finale al manoscritto
        nuovo = aggiungi_finale(manoscritto)
    elif operazione == "R":
        # Rimuove la prima riga del manoscritto
        nuovo = rimuovi_inizio(manoscritto)
    return nuovo

def aggiungi_finale(manoscritto):
    # Aggiunge "THE END!" alla fine del manoscritto
    nuova_versione = manoscritto[:]
    nuova_versione.append("THE END!")
    return nuova_versione

def rimuovi_inizio(manoscritto):
    # Rimuove la prima riga del manoscritto
    nuova_versione = manoscritto[:]
    if nuova_versione:
        nuova_versione.pop(0)
    return nuova_versione

def crea_copia_libro(libro):
    # Crea una copia profonda del libro per garantire che l'originale resti inalterato
    #nuovo_libro = list(libro) # Creerebbe una copia superficiale (shallow copy) del libro
    nuovo_libro = copy.deepcopy(libro)
    return nuovo_libro




# Definizione dei manoscritti (testi letterari)


# Alla Sera - Foscolo
manoscritto1 = """Forse perché della fatal quiete
Tu sei l’immago a me sì cara, vieni,
O Sera! E quando ti corteggian liete
Le nubi estive e i zeffiri sereni,
E quando dal nevoso aere inquiete
Tenebre, e lunghe, all’universo meni,
Sempre scendi invocata, e le secrete
Vie del mio cor soavemente tieni.
Vagar mi fai co’ miei pensier su l’orme
Che vanno al nulla eterno; e intanto fugge
Questo reo tempo, e van con lui le torme
Delle cure, onde meco egli si strugge;
E mentre io guardo la tua pace, dorme
Quello spirto guerrier ch’entro mi rugge."""

# A Song of Opposites - Keats
manoscritto2 = """Welcome joy, and welcome sorrow,
Lethe’s weed and Hermes’ feather;
Come to-day, and come to-morrow,
I do love you both together!
I love to mark sad faces in fair weather;
And hear a merry laugh amid the thunder;
Fair and foul I love together.
Meadows sweet where flames are under,
And a giggle at a wonder;
Visage sage at pantomine;
Funeral, and steeple-chime;
Infant playing with a skull;
Morning fair, and shipwreck’d hull;
Nightshade with the woodbine kissing;
Serpents in red roses hissing;
Cleopatra regal-dress’d
With the aspic at her breast;
Dancing music, music sad,
Both together, sane and mad;
Muses bright and muses pale;
Sombre Saturn, Momus hale; –
Laugh and sigh, and laugh again;
Oh the sweetness of the pain!
Muses bright, and muses pale,
Bare your faces of the veil;
Let me see; and let me write
Of the day, and of the night –
Both together: – let me slake
All my thirst for sweet heart-ache!
Let my bower be of yew,
Interwreath’d with myrtles new;
Pines and lime-trees full in bloom,
And my couch a low grass-tomb."""

# Still I Rise - Angelou
manoscritto3 = """You may write me down in history
With your bitter, twisted lies,
You may trod me in the very dirt
But still, like dust, I'll rise.
Does my sassiness upset you?
Why are you beset with gloom?
’Cause I walk like I've got oil wells
Pumping in my living room.
Just like moons and like suns,
With the certainty of tides,
Just like hopes springing high,
Still I'll rise.
Did you want to see me broken?
Bowed head and lowered eyes?
Shoulders falling down like teardrops,
Weakened by my soulful cries?
Does my haughtiness offend you?
Don't you take it awful hard
’Cause I laugh like I've got gold mines
Diggin’ in my own backyard.
You may shoot me with your words,
You may cut me with your eyes,
You may kill me with your hatefulness,
But still, like air, I’ll rise.
Does my sexiness upset you?
Does it come as a surprise
That I dance like I've got diamonds
At the meeting of my thighs?
Out of the huts of history’s shame
I rise
Up from a past that’s rooted in pain
I rise
I'm a black ocean, leaping and wide,
Welling and swelling I bear in the tide.
Leaving behind nights of terror and fear
I rise
Into a daybreak that’s wondrously clear
I rise
Bringing the gifts that my ancestors gave,
I am the dream and the hope of the slave.
I rise
I rise
I rise."""

# Odi et amo - Catullo
manoscritto4 = """Odi et amo. Quare id faciam fortasse requiris.
Nescio, sed fieri sentio, et excrucior."""

# Lista dei manoscritti da includere nel libro
lista_manoscritti = [manoscritto1, manoscritto2, manoscritto3, manoscritto4]

# Creazione del libro tematico di poesie
print("Creazione del libro di poesie...")
libro_poesia = crea_libro(lista_manoscritti)
print("Libro di poesie creato.\n")

# Analisi del libro originale
analisi_libro(libro_poesia)

# Creazione di una nuova versione modificata di un manoscritto
print("Creazione di una nuova versione modificata del quarto manoscritto (aggiunta di una riga finale)...")
nuovo_manoscritto = aggiungi_finale(libro_poesia[3])
print("Nuova versione del manoscritto creata.\n")

# Verifica che il libro originale sia rimasto inalterato
print("Verifica che il libro originale sia inalterato dopo la modifica...")
analisi_libro(libro_poesia)

# Creazione di una copia del libro per inviarla ad altri monasteri
copia_libro = crea_copia_libro(libro_poesia)
# Modifica della copia aggiungendo una nota al primo manoscritto
print("Aggiunta di una nota al primo manoscritto nella copia del libro...")
copia_libro[0].append("nota a margine")
print("Nota aggiunta alla copia del libro.\n")

# Verifica che il libro originale sia rimasto inalterato dopo la modifica della copia
print("Verifica che il libro originale sia inalterato dopo la modifica della copia...")
analisi_libro(libro_poesia)

# Creazione di altre versioni modificate dei manoscritti
print("Creazione di nuove versioni modificate del primo manoscritto...")
nuovo_manoscritto2 = aggiungi_finale(libro_poesia[0])
nuovo_manoscritto3 = rimuovi_inizio(libro_poesia[0])
print("Nuove versioni del manoscritto create.\n")

# Verifica finale del libro originale
print("Analisi finale del libro originale per confermare che è inalterato...")
analisi_libro(libro_poesia)

# Modifica di un manoscritto utilizzando la funzione generale
print("Modifica del quarto manoscritto utilizzando la funzione 'modifica_manoscritto' con operazione 'R'...")
manoscritto_modificato = modifica_manoscritto(libro_poesia[3], "R")

# Stampa del manoscritto modificato
print("Manoscritto modificato:")
for riga in manoscritto_modificato:
    print(riga)

