COUNTRIES = 8
MEDALS = 3

counts = [
    [ 0, 3, 0 ],
    [ 0, 0, 1 ],
    [ 0, 0, 1 ],
    [ 1, 0, 0 ],
    [ 0, 0, 1 ],
    [ 3, 1, 1 ],
    [ 0, 1, 0 ],
    [ 1, 0, 1 ]
    ]

print(counts)

print(counts[5])

oro_russia = counts[5][0]
print(oro_russia)

for riga in range(len(counts)):
    # print(counts[riga])
    for col in range(len(counts[riga])):
        print(f'{counts[riga][col]:6d}', end='')
    print()

for nazione in counts:
    for medaglie in nazione:
        print(f'{medaglie:6d}', end='')
    print()

print('il numero totale di medaglie per ogni nazione')
# somma per righe
for nazione in counts:
    print(sum(nazione))

print('il numero di medaglie per ciascun tipo')
for tipo in range(3):
    med = 0
    for nazione in counts:
        med = med + nazione[tipo]
    print(med)

for tipo in range(3):
    med = 0
    for riga in range(len(counts)):
        med = med + counts[riga][tipo]
    print(med)

