"""
Operazioni con le liste
"""

# lista di stringhe

tartarughe = ["Leonardo", "Donatello", "Raffaello", "Michelangelo"]
alleati_tartarughe = ["Splinter", "April", "Casey"]

print(len(tartarughe))
print(tartarughe[1])


# lista di numeri interi

# punteggi di Pecco Bagnaia nei motoGP del 2024 - Fonte: https://www.insella.it/motogp/classifica-piloti

punti = [31, 6, 13, 25, 16, 25, 37, 37, 32, 16, 37, 1, 29, 12, 28, 37, 22, 32, 25, 0]

for pt in punti:
    print('*' * pt)

for i in range(len(punti)):
    print(i+1, '#' * punti[i])


# ESERCIZI DI RISCALDAMENTO

# Leggere da tastiera l'elenco dei voti conseguiti da uno studente (valori interi tra 18 e 31, termina inserimento con *).
# Memorizzare i dati in una lista.

'''
voti = []
v = input('Voto: ')
while v != '*':
    voto = int(v)
    # metti il voto in una lista di voti[]
    voti.append(voto)
    v = input('Voto: ')

print(voti)
'''

voti = [20, 18, 24, 29, 18, 30, 31, 27, 19, 30]


# Verificare se lo studente ha preso almeno un voto pari a 18. 

trovato18 = False
for voto in voti:
    if voto == 18:
        trovato18 = True

if trovato18:
    print("Trovato almeno un 18")
else:
    print("Nessun 18")

if 18 in voti:
    print("Trovato almeno un 18")
else:
    print("Nessun 18")

# Verificare se ha preso un 30 o 30 e lode.

if (30 in voti) or (31 in voti):
    print("Trovato almeno un 30 o 30 e lode")
else:
    print("Nessun 20 né 30 e lode")

# Verificare se il numero di 18 è minore o maggiore del numero di 30 / 30 lode.

conta18 = 0 
for voto in voti:
    if voto==18:
        conta18 += 1

conta30 = 0 
for voto in voti:
    if voto == 30 or voto==31:
        conta30 += 1


conta18 = 0 
conta30 = 0 
for voto in voti:
    if voto==18:
        conta18 += 1
    if voto == 30 or voto==31:
        conta30 += 1
        

if conta18 < conta30:
    print('Hai più 30/30L che 18')
elif conta18 > conta30:
    print('Hai più 18 che 30/30L')
else:
    print('Hai lo stesso numero di 18 e di 30/30L')

conta18 = voti.count(18)
conta30 = voti.count(30)+voti.count(31)

# Costruire dei voti "migliorati", sommando 1 punto a tutti i voti >= 24,
# e 2 punti a tutti i voti >=18

print(voti)

voti_fake = list(voti)
# voti_fake = voti #  NOOOO, crea un alias e non una copia

for i in range(len(voti_fake)):
    voti_fake[i] = voti_fake[i]+1

print("migliorati", voti_fake)
print("originali", voti)


voti_fake2 = []   # voti_fake2 = list()
for voto in voti:
    voti_fake2.append(voto+1)


voti_fake3 = [voti]  # NOO, crea una nuova lista con 1 solo elemento che è un alias alla lista precedente

# Riguardo ai punteggi di Bagnaia, calcolare la somma e la media delle gare

somma_punti = 0
for punto in punti:
    somma_punti = somma_punti + punto

somma_punti = sum(punti)
media_punti = sum(punti) / len(punti)

print(f'Il punteggio totale vale {somma_punti} e media vale {media_punti}')

# Ripetere i calcoli considerando solo i punteggi maggiori o uguali a 20.

somma20 = 0
conta20 = 0
for punto in punti:
    if punto>=20:
        somma20 = somma20 + punto
        conta20 = conta20 + 1

print(f'Il punteggio delle gare con più di 20 punti vale {somma20} e media vale {somma20/conta20:.2f}')


# Cancellare dalla lista tutti gli elementi con punteggio minore di 20

print(punti)

# i=0
# while i<len(punti):
#     punto = punti[i]
#     if punto<20:
#         punti.pop(i)
#         continue

#     i = i + 1

# i = len(punti)-1
# while i>=0:
#     if punti[i]<20:
#         punti.pop(i)
#     i = i - 1

# for i in range(len(punti)-1, -1, -1): # indici 19, 18, 17, .... 2, 1, 0
#     if punti[i]<20:
#         punti.pop(i)


punti_nuovi = []
for punto in punti:
    if punto>=20:
        punti_nuovi.append(punto)
punti = punti_nuovi

punti_nuovi = [ p for p in punti if p>=20  ]
# list comprehension

voti_nuovi = [ voto+1 for voto in voti if voto<24 ]

print(punti)


# Visualizzare in ordine alfabetico tutti i personaggi delle TMNT

# costriusco una lista che contenga SIA le tartarughe SIA gli alleati
# -> concatenazione di liste

personaggi = tartarughe + alleati_tartarughe

# personaggi = [ tartarughe, alleati_tartarughe ]   NOO

print(personaggi)
personaggi.sort()
print(personaggi)

# tartarughe.append(alleati_tartarughe) NO
tartarughe.extend(alleati_tartarughe)

print(tartarughe)