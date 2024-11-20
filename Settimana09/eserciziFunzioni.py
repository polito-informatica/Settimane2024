def calcolo_cubo(n):
    # Questa funzione calcola il cubo di un numero
    return n ** 3 

def accorcia_lato(lato):
    # Questa funzione diminuisce il valore di 'lato' di 1
    lato = lato - 1
    return lato

def stampa_due_numeri(a, b, c):
    # Questa funzione stampa i valori di 'a' e 'c', ignorando 'b'
    print(a, c)

def stampa_parole(*args):
    # Questa funzione accetta un numero variabile di argomenti e li stampa
    for arg in args:
        print(arg)

def analisi_tipo(var):
    # Questa funzione controlla il tipo di 'var' e restituisce un valore basato sul tipo
    if type(var) == str:
        print(var, "è una stringa")
        return var + "1"
    elif type(var) == int:
        print(var, "è un int")
        return var + 1
    else:
        print(var, "ha un tipo non gestito")
        return None
    
def aggiungi_elemento(lista):
    lista.append(4)
    print(f"Lista all'interno della funzione: {lista}")
  

# Uso delle funzioni

# Esempio 1: Uso di calcolo_cubo(n)
numero = 3
print(f"Calcoliamo il cubo di {numero}")
cubo = calcolo_cubo(numero)
print(f"Il cubo di {numero} è {cubo}\n")

# Esempio 2: Uso di accorcia_lato(lato)
lato_originale = 5
print(f"Lato originale: {lato_originale}")
lato_accorciato = accorcia_lato(lato_originale)
print(f"Lato accorciato: {lato_accorciato}")
print(f"Lato originale dopo la funzione: {lato_originale}\n")

# Esempio 3: Uso di stampa_due_numeri(a, b, c)
print("Chiamata a stampa_due_numeri(1, 2, 3):")
stampa_due_numeri(1, 2, 3)
print()

# Esempio 4: Uso di stampa_parole(*args)
print("Chiamata a stampa_parole('Ciao', 'a', 'tutti'):")
stampa_parole('Ciao', 'a', 'tutti')
print()

# Esempio 5: Uso di analisi_tipo(var)
print("Chiamata a analisi_tipo con una stringa:")
risultato_stringa = analisi_tipo("test")
print(f"Risultato: {risultato_stringa}\n")

print("Chiamata a analisi_tipo con un intero:")
risultato_intero = analisi_tipo(10)
print(f"Risultato: {risultato_intero}\n")

print("Chiamata a analisi_tipo con un float:")
risultato_float = analisi_tipo(3.14)
print(f"Risultato: {risultato_float}\n")

# Esempio 6: oggetti mutabili (come le liste)
mia_lista = [1, 2, 3]
print(f"Lista originale: {mia_lista}")
aggiungi_elemento(mia_lista)
print(f"Lista dopo la funzione: {mia_lista}")