# Esercizio

## Testo del problema

Quali sono i nomi più frequenti in quest’aula?

## Analisi

- QUANTI nomi devo restituire?
es: i 10 più frequenti, o meno di 10 se non ci sono almeno 10 nomi diversi
in caso di pari-merito nella classifica delle frequenze, mi
fermo comunque a 10 scegliendone alcuni arbitrariamente

- Maria Grazia ... 
I nomi composti... es. li tratto come nomi unici

analizziamo i nomi degli studenti iscritti al corso
(che possono o non possono essere in quest'aula)

- vogliamo visualizzare i nomi, con a fianco la relativa frequenza
e visualizzarli in ordine decrescente di frequenza
a parità di frequenza, scelgo un ordine qualsiasi

PINCO 10
PALLINO 8
SEMPRONIO 8


## Strategia

VISTI = nessuno
Prendi le righe del file una per una
    per ciascuna riga, estrai il NOME (in terzo campo, considerando i campi separati da virgola)
    ho già visto questo nome? (NOME è presente in VISTO?)
        se no, aggiungi a VISTI il NOME, con frequenza 1
        se sì, incrementa di 1 la frequenza associata a NOME

Ordina i VISTI per freuquenza decrescente
    ???

Visualizza i primi 10 di VISTI