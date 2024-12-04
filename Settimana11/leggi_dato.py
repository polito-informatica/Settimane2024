
def leggi_intero(msg):
    ok = False
    while not ok:
        s = input(msg)
        try:
            dato = int(s)
            ok = True
            return dato
        except ValueError:
            print('Dato errato, re-inseriscilo')

def calcola(x, y):
    risultato = x / y
    return risultato
    
def main():

    ok = False
    while not ok:
        try:
            x = leggi_intero('x = ')
            y = leggi_intero('y = ')
            z = calcola(x, y)
            ok = True
            print(z)
            
        except ZeroDivisionError:
            print("Divisione per zero, devi reinserire i dati da capo")


main()