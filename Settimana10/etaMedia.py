# Apri il file "anagrafica.txt" in modalità lettura con codifica UTF-8
infile = open(file="anagrafica.txt", mode="r", encoding="UTF-8")

# Inizializza una variabile per la somma delle età
somma = 0

# Itera attraverso ogni riga del file
for riga in infile:
    # Rimuove il carattere di nuova linea '\n' e divide la riga in parole separate da spazio
    lista_parole = riga.rstrip().split(" ")
    # Prende il terzo elemento della lista (indice 2) e lo converte in intero
    eta = int(lista_parole[2])
    # Aggiunge l'età alla somma totale
    somma = somma + eta
    # Stampa l'età corrente
    print(eta)

# Stampa la somma totale delle età
print(somma)

# Chiude il file
infile.close()