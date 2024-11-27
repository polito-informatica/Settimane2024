"""
Una famiglia nobile vuole assolutamente dare un doppio nome al proprio figlio, e per farlo vuole combinare i nomi dei propri avi, in modo però che il nome complessivo non risulti troppo lungo.

I nomi degli avi sono contenuti in una lista di stringhe di nome 'avi', come ad esempio:

```python
avi = ['Giovanni', 'Maria', 'Luigi', 'Anna', 'Paolo', 'Giulia', 'Carlo', 'Rosa']
```

I possibili nomi devono essere creati combinando tra di loro due nomi degli avi, in tutti i modi possibili, con le seguenti regole:
- il nome complessivo deve avere una lunghezza massima di 10 caratteri
- la vocale finale del primo nome deve essere cancellata
- se, dopo avere cancellato la vocale, il nome terminasse con due consonanti, la seconda consonante deve essere cancellata

Ad esempio, si potranno ottenere i seguenti nomi: Giovananna, Paolcarlo, Anrosa, Mariluigi, Ananna, ecc.

Si scriva un frammento di codice Python che, partendo dalla lista 'avi', calcoli la lista di tutti i possibili nomi che rispettano le regole sopra indicate, rispettando il corretto uso delle maiuscole e minuscole.
"""

avi = ["Giovanni", "Maria", "Luigi", "Anna", "Paolo", "Giulia", "Carlo", "Rosa"]

VOCALI = 'aeiou'

# considero tutte le coppie di nomi possibili
for primo in avi:
    for secondo in avi:
        primo = primo.lower()
        secondo = secondo.lower()

        if primo[-1] in VOCALI:
            primo = primo[:-1]
        
        if len(primo)>=2 and primo[-1] not in VOCALI and primo[-2] not in VOCALI:
            primo = primo[:-1]

        nome = primo+secondo
        nome = nome[0].upper() + nome[1:]

        if len(nome)<=10:
            print(nome)