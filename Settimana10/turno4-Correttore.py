'''
Un correttore ortografico deve verificare, data una parola appena scritta dall'utente, se questa è presente nel dizionario 
oppure se esiste una parola ad essa simile che sia presente nel dizionario.

Il dizionario è memorizzato in una lista di stringhe di nome 'dizionario', che contiene singole parole minuscole prive di spazi.

Esempio:
```python
dizionario = ['casa', 'cane', 'gatto', 'topo', 'mela', 'pera', 
              'uva', 'ciccia', 'cicoria', 'cicogna', 'ciclamino']
```

Si scriva un frammento di codice Python che, partendo dalla lista 'dizionario' e dalla parola 'parola' da correggere, 
verifichi se la parola è presente nel dizionario, e in caso contrario verifichi se esiste una parola simile (ossia che 
differisca per una sola lettera) presente nel dizionario. In tal caso, si stampi la parola corretta.

Ad esempio: la parola 'pera' è indicata come corretta, mentre la parola 'getto' viene corretta in 'gatto'. 
Invece, la parola 'sotto' è indicata come errata ma priva di correzione, perché differisce di 2 lettere da 'gatto'.

'''

dizionario = ['casa', 'cane', 'gatto', 'topo', 'mela', 'pera', 
              'uva', 'ciccia', 'cicoria', 'cicogna', 'ciclamino']

parola = 'getto'

if parola in dizionario:
    print('parola presente')
else:
    for diz in dizionario:
        # mi chiedo se 'diz' è simile a 'parola'
        # ha la stessa lunghezza
        # n-1 lettere uguali ed 1 diversa

        if len(diz)==len(parola):
            # conto le lettere di differenza
            c = 0
            for i in range(len(parola)):
                if parola[i]!=diz[i]:
                    c = c + 1
            if c==1:
                print(f'{parola} è simile a {diz}')

