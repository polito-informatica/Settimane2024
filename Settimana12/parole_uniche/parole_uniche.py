import string

NOME_FILE_POESIA = 'apelle.txt'

univoche = set()
tutte = []

f_in = open(NOME_FILE_POESIA, 'r', encoding='utf-8')

for riga in f_in:
    parole = riga.rstrip('\n').split()

    for parola in parole:
        parola = parola.strip(string.punctuation)

        # print(parola)
        tutte.append(parola)

print(tutte)
univoche = set(tutte)
print(univoche)

# statistiche
for p in sorted(univoche):
    c = tutte.count(p)
    print(f'La parola {p} compare {c} volte')

f_in.close()
