
# Apri il file "datiNumerici.txt" in modalità lettura con codifica UTF-8
infile = open("datiNumerici.txt", "r", encoding="UTF-8")

# Legge un carattere dal file
# un_carattere = infile.read(1)
# print(un_carattere)

# Legge i successivi tre caratteri dal file
# un_carattere = infile.read(3)
# print(un_carattere)

# Legge una riga dal file e rimuove il carattere di nuova linea '\n' alla fine
# una_riga = infile.readline().rstrip()
# print(una_riga)

# Legge tutte le righe rimanenti dal file e le memorizza in una lista
# tutte_le_righe = infile.readlines()
# print(tutte_le_righe)

# Inizializza una variabile per la somma
somma = 0

# Utilizzando il for
# Itera attraverso ogni riga nel file
#for line in infile:
#    # Rimuove il carattere di nuova linea '\n' alla fine e converte la linea in un intero
#    n = int(line.rstrip())
    # Aggiunge il numero alla somma totale
#    somma = somma + n

# Utilizzando il while
# Legge la prima riga del file
line = infile.readline()

# Itera attraverso ciascuna riga utilizzando readline()
while line!="":
    # Rimuove il carattere di nuova linea '\n' alla fine e converte la riga in un intero
    n = int(line.rstrip())
    # Aggiunge il numero alla somma totale
    somma += n
    # Legge la linea successiva
    line = infile.readline()

# Stampa la somma totale dei numeri nel file
print(somma)


# Chiude il file
infile.close()