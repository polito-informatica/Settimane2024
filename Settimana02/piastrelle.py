# Esercizio "Piastrelle"

"""
Bisogna posizionare lungo il muro una fila di piastrelle nere e bianche. 
Per ragioni estetiche l'architetto ha specificato che la prima e l'ultima piastrella devono essere nere. 
Il vostro compito è calcolare il numero di piastrelle necessarie e il vuoto a ciascuna delle due estremità 
della riga, dato lo spazio disponibile e la larghezza di ogni piastrella. 
"""

'''

| NBNBNBNBN |

Dati di partenza:
 - Lunghezza del muro (lun_muro)
 - Lato della piastrella (ipotesi: quadrate) (lato)
 - Due tipi di piastrelle: B e N
Vincoli del problema:
 - Prima e ultima piastrella N
 - Piastrelle B e N sempre alternate
 - Spazio rimanente >=0, se >0 distribuito egualmente sui due lati
Risultati attesi:
 - Numero di piastrelle B
 - Numero di piastrelle N
 - Spazio residuo da ciascun lato

 num_piastrelle = lun_muro / lato
 es. 90 / 20 = 4.5  -> ne metto 4 NO! -> ne metto solo 3
 In generale, se lun_muro>=lato, devo trovare il numero dispari più grande
 che sia <= a lun_muro / lato
 Se invece lun_muro < lato, non esiste soluzione

 100/20 = 5
 110/20 = 5.5
 2000/20 = 100 -> 99
 50/20 = 2.5 -> 2 -> 1
 40/20 = 2.0 -> 2 -> 1
 30/20 = 1.5 -> 1
 20/20 = 1
 10/20 = 0.5 -> (-1)

 Possibile strategia:

 verificare che lun_muro>0 e lato>0
 calcola num_piastrelle = lun_muro / lato
 calcola la parte intera di num_piastrelle
 se è pari, decrementala di 1
 se viene -1, i dati non sono accettabili
 altrimenti, quello è il numero totale di piastrelle
 B = numero // 2
 N = B+1
 spazio = (lun_muro - (N+B)*lato)/2

 Strategia alternativa (senza "se"):
 (assumendo che i dati siano corretti)

 NBNBNBN    =   N BN BN BN
 coppie_BN = (lun_muro-lato) // (2*lato)
 B = coppie_BN
 N = coppie_BN + 1

'''

# lun_muro = 137
# lato = 19.4
lun_muro = float(input("Muro: "))
lato = float(input("Piastrella: "))

coppie = (lun_muro-lato) // (2*lato)
B = coppie
N = coppie + 1
spazio = (lun_muro - (N+B)*lato)/2

print('Su un muro di lunghezza', lun_muro, 'con piastrelle di lato', lato)
print('ci stanno', N, 'piastrelle nere e', B, 'bianche')
print('lasciando lo spazio di ', spazio, 'da entrambi i lati')