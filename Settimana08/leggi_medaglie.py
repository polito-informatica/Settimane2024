# legge da tastiera i dati del medagliere

NAZIONI = 4
MEDAGLIE = 3

# counts = []

# for riga in range(NAZIONI):
#     nazione = []
#     counts.append(nazione)
#     # leggo le medaglie di una nazione
#     for col in range(MEDAGLIE):
#         m = int(input(f'Numero di medaglie ({riga},{col}): '))
#         nazione.append(m)

# print(counts)

# facciamo un medagliere di tutti 0, 
# poi lo riempiamo con i valori effettivi

counts = []
riga_vuota = [0] * MEDAGLIE
for riga in range(NAZIONI):
    counts.append(list(riga_vuota))

for riga in range(NAZIONI):
    for col in range(MEDAGLIE):
        m = int(input(f'Numero di medaglie ({riga},{col}): '))
        counts[riga][col] = m

print(counts)