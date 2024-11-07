"""
Gestire la lista d'attesa per un locale.
Le persone in lista sono identificate con il proprio nome, e non ci sono omonimi. 
Il programma prende in input un'operazione che inserisce l'utente, 
la quale in questo caso è la persona che gestisce gli ingressi all'evento. 
Le operazioni da gestire sono le seguenti (i nomi delle persone sono a titolo esemplificativo):

P mina -> restituisci la Posizione di mina (se non è presente, segnalalo)
A pippo -> Aggiungi in coda pippo (se è già presente, segnalalo)
R gina -> Rimuovi dalla coda gina (se non è presente, segnalalo)
I john -> Inserisci in testa john (se è già presente, segnalalo)

Dopo ogni iterazione, il programma restituisce in output la lista d'attesa nel suo stato corrente, con il formato:

1 john
2 gale
3 iram
4 melany
5 pippo

Il programma termina quano viene inserita in input la stringa vuota ("").

"""

listaDAttesa = ["pippo", "gina", "andrea", "ginevra", "willy", "greta", "jo"]

operazione = input("Inserisci un'operazione: ")

while operazione != "":
    
    operazione_spezzettata = operazione.split()
    operazione = operazione_spezzettata
    #print("Hai inserito", operazione)
    azione = operazione[0].upper()
    persona = operazione[1].lower()

    if azione == "P":

        if persona in listaDAttesa:
            posizione = listaDAttesa.index(persona)
            print(f"{persona} si trova in posizione {posizione+1}")
            
            """
            # versione che gestisce i duplicati
            indici_occorrenze=[]
            i = 0
            for p in listaDAttesa:
                if p == persona:
                    indici_occorrenze.append(i)
                i = i + 1
            print(f"Le occorrenze di {persona} si trovano alle posizioni {indici_occorrenze}")
            """
        else:
            print(f"Non posso trovare la posizione di {persona} perché non è in lista.")

    elif azione == "A":

        if persona not in listaDAttesa:
            listaDAttesa.append(persona)
        else:
            print(f"Non posso aggiungere {persona} perché è già in lista.")

        """
        # versione che gestisce 5 duplicati

        if listaDAttesa.count(persona) < 5:
            listaDAttesa.append(persona)
        else:
            print(f"Non posso aggiungere {persona} perché ce ne sono già 5 in lista.")
        """  

    elif azione == "R":
        if persona in listaDAttesa:
            listaDAttesa.remove(persona)
            #listaDAttesa.pop(listaDAttesa.index(persona))
        else:
            print(f"Non posso rimuovere {persona} perché non è in lista.")

    elif azione == "I":

        if persona not in listaDAttesa:
            listaDAttesa.insert(0, persona)
        else:
            print(f"Non posso aggiungere {persona} in testa perché è già in lista.")

        """
        # versione che gestisce 5 duplicati

        if listaDAttesa.count(persona) < 5:
            listaDAttesa.append(persona)
        else:
            print(f"Non posso aggiungere {persona} in testa perché ce ne sono già 5 in lista.")
      
        """      

    else:
        print("Inserire azione corretta: P, A, I, R")
    
    for i, p in enumerate(listaDAttesa):
        print(i+1, p)
        
    operazione = input("Inserisci un'operazione: ")