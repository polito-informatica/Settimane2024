"""
Si consideri il gioco "Tetris Piatto e Compatto", in cui è necessario di collocare dei pezzi (composti da 1 a 4 quadretti, sempre disposti in orizzontale) su una tabella composta da 10 colonne ed un numero illimitato di righe.
Un nuovo pezzo si può posizionare solamente in forma orizzontale, e deve appoggiarsi completamente sulla base della tabella, oppure sopra dei pezzi già esistenti. Non è quindi permesso formare dei "buchi" con l'arrivo di nuovi pezzi. Se non è possibile disporre un pezzo senza formare un buco, il gioco termina.

La situazione della tabella di gioco può quindi essere riassunta da una lista di 10 numeri interi, che rappresentano l'altezza dei quadretti già posizionati in ciascuna colonna. Ad esempio, la lista:
```python
altezze = [ 0, 1, 0, 2, 0, 3, 3, 2, 2, 0 ]
```
rappresenta questa tabella di gioco:
```
        . . . . . . . . . .
        . . . . . X X . . .
        . . . X . X X X X .
        . X . X . X X X X .
        ___________________
        1 2 3 4 5 6 7 8 9 10
```
Se arrivasse un pezzo di lunghezza 1, può essere piazzato in qualsiasi colonna. Se arrivasse un pezzo di lunghezza 2, 
potrà essere piazzato solo sulle colonne 6-7 oppure sulle colonne 8-9. Se arrivasse un pezzo di lunghezza 3, non 
potrebbe essere piazzato senza formare un buco, e quindi la partita terminerebbe.

Si scriva un frammento di codice Python che, data una situazione di partenza rappresentata dalla matrice 'altezze', e data la lunghezza del pezzo in arrivo (tra 1 e 4), indicata dalla variabile 'pezzo', determini:
- se è possibile collocare il pezzo senza formare buchi
- in caso affermativo, scelga dove collocarlo ed aggiorni la lista 'altezze' con la nuova situazione di gioco.
"""

altezze = [0, 1, 0, 2, 0, 3, 3, 2, 2, 0]
pezzo = 2

# trovare se ci sono 'pezzo' celle consecutive di 'altezze' il cui valore sia uguale
# cerchiamo sequenze partendo da diversi indici 'ip' di partenza.

for ip in range(len(altezze)-(pezzo-1)):
    # la sequenza di celle dall'indice ip all'indice (ip+pezzo-1) ha tutti valori uguali?
    uguali = True
    for s in range(1, pezzo):
        if altezze[ip] != altezze[ip+s]:
            uguali = False

    # scorciatoia
    # if altezze[ip:ip+pezzo] == [ altezze[ip] ] * pezzo:

    # la variabile 'uguali' mi dice se il pezzo si può mettere
    if uguali:
        print(f'pezzo in posizione {ip}')
        for s in range(0, pezzo):
            altezze[ip+s] = altezze[ip+s]+1
        break # esce dal ciclo 'for ip'
    
print(altezze)

