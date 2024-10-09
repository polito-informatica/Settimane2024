# nel palazzo il piano 13 "si salta"
# l'utente dice a che piano vuole andare 
# l'ascensore deve dire di quanti piani salirà effettivamente

piano = int(input("A che piano vuoi andare? "))

# se il piano è maggiore di 13 allora deve salire 
# di un numero di piani pari a piano - 1
# altrimenti, deve salire
# di un numero di piani pari a piano

# gestione anomalia
isValid = piano == 13 or piano == 17

if piano == isValid:
    print(f"Piano non valido")
# gestione casi validi
else: 
    
    if piano > 17:    
        piano_effettivo = piano - 2
    elif piano > 13:
        piano_effettivo = piano - 1
    else:
        piano_effettivo = piano
    
    print(f"Salirò di {piano_effettivo} piani")





