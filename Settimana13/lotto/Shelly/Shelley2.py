
# SHE SELLS SEA SHELLS BY THE SEA SHORE
# (Esame proposto il 20/02/2024)
# Miss Shelley ha deciso di vendere la sua collezione di conchiglie marine sulla riva del mare. Ogni conchiglia ha un prezzo e ha deciso di tentare potenziali acquirenti con offerte. Ad esempio, chiunque compri due conchiglie Abalone riceverà una conchiglia Drupe in regalo.

# Il file prices.dat contiene l'elenco delle conchiglie e il loro prezzo unitario. Il file è composto da più righe, il formato di ogni riga è conchiglia: prezzo. Il nome della conchiglia non contiene spazi. Il prezzo è in euro e può contenere centesimi di euro.
# Il file offers.dat contiene le offerte. Il file è composto da più righe, il formato di ogni riga è conchiglia1 conchiglia2 ... conchigliaN: conchiglia. Ogni riga specifica le conchiglie che devono essere acquistate per ricevere quella in regalo. Ad esempio, se chiunque compri due conchiglie Abalone riceve una conchiglia Drupe in regalo, il file conterrà la riga Abalone Abalone: Drupe. Nota: né le conchiglie che hanno generato un regalo né quelle ricevute possono generare ulteriori regali.
# Il file cart.dat contiene l'elenco delle conchiglie che il cliente desidera acquistare. Il file è composto da più righe, ogni riga contiene il nome di una conchiglia.

# Scrivi un programma che calcola il prezzo finale del carrello, senza considerare le conchiglie che il cliente potrebbe ricevere gratuitamente.
# Il programma dovrebbe visualizzare una riga per ogni offerta corrispondente nel formato Acquistando conchiglia1, conchiglia2, ..., conchigliaN; hai ricevuto conchigliaX in regalo, e il prezzo finale nel formato: Prezzo finale: x.yy EUR

# Ad esempio, con i file di input forniti, se il carrello contiene 6 conchiglie Nautilus, il prezzo finale è solo di 14,95 EUR (cioè 2,99 x 5), perché 1 conchiglia Nautilus è in regalo se un cliente ne acquista 4 ("paghi 4 e ne ottieni 5": Nautilus_Shell Nautilus_Shell Nautilus_Shell Nautilus_Shell: Nautilus_Shell).

# Esempio
# File prices.dat
# Abalone: 19.99
# Melo_Melo: 4.99
# Murex: 2.5
# Nautilus_Shell: 2.99
# Oyster_Shell: .5
# Sand_Dollar: 2.5
# Small_Strombus_Gigas: 2500
# Venus_Comb: 75
# File offers.dat
# Abalone Abalone: Drupe
# Conus_Gloriamaris: Cowrie
# Nautilus_Shell Nautilus_Shell Nautilus_Shell Nautilus_Shell: Nautilus_Shell
# Murex Murex Murex: Oyster_Shell
# File cart.dat
# Nautilus_Shell
# Nautilus_Shell
# Nautilus_Shell
# Abalone
# Drupe
# Abalone
# Nautilus_Shell
# Nautilus_Shell
# Nautilus_Shell
# Output del programma
# Acquistando Abalone, Abalone; hai ricevuto Drupe in regalo
# Acquistando Nautilus_Shell, Nautilus_Shell, Nautilus_Shell, Nautilus_Shell; hai ricevuto Nautilus_Shell in regalo
# Prezzo finale: 58.91 EUR
################################################################################################################################
################################################################################################################################
# Carico i dati
# per ogni offerta controllo se è applicabile (cioè se le conchiglie richieste per applicare l'offerta sono nel carrello).
# Inotre devo sapere se c'è il regalo dentro al carrello, perché se sì, il suo prezzo non va considerato nel conto.
# Inoltre serve un contenitore d'appoggio per tenere in considerazione le conchiglie del carrello che sono già state coinvolte in un'offerta
# Attention to: applico le offerte una per volta ed in ordine.
#               Cosa succede se un'offerta è applicabile più volte?
#               Cosa succede se un'offerta mischia diversi tipi di conchiglie?
#              
# Further request: Quali visualizzazioni sono richieste, dove e con che formati?
# Possibili dubbi:  Cosa dice di fare il testo quando il cliente potrebbe avere una conchiglia in regalo, ma non la ha nel carrello? (quindi non può essere stornato il suo prezzo)
#                   Non lo dice, dice solo: ' Scrivi un programma che calcola il prezzo finale del carrello, senza considerare le conchiglie che il cliente potrebbe ricevere gratuitamente.'
################################################################################################################################
################################################################################################################################
from collections import Counter
# Salviamo i prezzi delle conchiglie come dizionario, poiché non sono dati ordinati.
# La key sarà il nome della conchiglia, il value sarà il prezzo (attenzione è un float)
def load_prices(file_path):
    """Salva i prezzi dal file prices.txt."""
    prices = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            shell, price = line.strip().split(': ')
            prices[shell] = float(price)
    return prices

# Salviamo le conchiglie presenti nel carrello come come dizionario, poiché non sono dati ordinati e ci fa comodo avere informazione sugli elementi presenti nel carrello e la loro frequenza.
# La key sarà il nome della conchiglia, il value sarà il numero di volte in cui appare nel carrello.
# Alternativa: creare una lista di stringhe e calcolare occorrenze qui o successivamente.
# Alternativa: from collections import Counter \n Counter(lista) restitusce un dizionario con elementi come chiavi e occorrenze come value

def load_cart(file_path):
    """Salva il carrello dal file cart.txt."""
    cart = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line=line.strip().strip('\n')
            if line in cart:
                cart[line]+=1
            else:
                cart[line]=1
    return cart


def isapplicable(conditions_c, cart, free_shell):
    """Controlla se l'offerta è applicabile al carrello"""
    # è applicabile? Se l'offerta prevede un numero superiore di conchiglie di quel tipo maggiore di quello presente nel carrello, allora non è applicabile
    flag=True

    for key in conditions_c:
        if key in cart:
            if conditions_c[key]>cart[key]: # Se la condizione prevede più 'conchiglia key' di quelle nel carrello
                flag=False
        else:
            flag=False
    if flag: # Solo se le condizioni dell'offerta sono rispettate
        if not(free_shell in cart):
            flag= False
            print(f"Acquistando {', '.join(conditions)}; avresti diritto a {free_shell} in regalo, ma non la hai nel carrello!")
    
    return flag

def calculate_total(cart, prices):
    """Calcola il prezzo totale del carrello come prezzo conchiglia* occorrenza nel carrello."""
    total = 0
    for shell in cart:
        total += prices[shell]*cart[shell]
    return total

#MAIN

# Carica i file e restituisce i dati in strutture dizionario
prices = load_prices('prices.txt')
    #offers = load_offers('offers.dat')
cart = load_cart('cart.txt')
cart_temp=dict(cart) # Carrello di appoggio per rimuovere gli items già interessati da un'offerta

with open('offers.txt', 'r',encoding='utf-8') as f: #  Carica le offerte una per volta segnando in una stringa di dimensione sconosciuta le condizioni dell'offerta e il regalo corrispondente a parte
    for line in f:
        conditions, free_shell = line.strip().split(': ')
        conditions= conditions.split()
        conditions_c=Counter(conditions)
    # Ci sono gli elementi dell'offerta nel carrello? Attenzione l'offerta si potrebbe verificare più di una volta
        flag=True
        while flag:
            flag = isapplicable(conditions_c,cart_temp, free_shell)
            # Se sì, tolgo il gift corrispondente dal carrello, aggiorno il carrello d'appoggoo e printo
            if  flag:
                    cart[free_shell]-=1 # in cart tengo solo gli oggetti da pagare effettivamente
                    cart_temp[free_shell]-=1
                    for key in conditions_c:
                        cart_temp[key]-=conditions_c[key]
                    print(f"Acquistando {', '.join(conditions)}; hai ricevuto {free_shell} in regalo")
    
#
# Calcola il prezzo finale
total_price = calculate_total(cart, prices)
print(f"Prezzo finale: {total_price:.2f} EUR")


