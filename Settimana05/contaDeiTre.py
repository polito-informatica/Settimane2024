# prendere in input dall'utente dei numeri
# e contare le occorrenze del numero 3
# e uscire se viene inserito "*"

isValid = True
conta_tre = 0 
numero = input("Inserire un numero: ")

#if numero == "*":
#    isValid = False

#isValid = not (numero == "*")

isValid = numero != "*" 

if not isValid:
    print("Non entro nel ciclo!")

while isValid:
    print(f"Hai inserito {numero}")
    
    # conta tutti i numeri 3 inseriti dall'utente
    #if int(numero) == 3: 
    #    conta_tre = conta_tre + 1

    # conta come singola occorrenza tutti i numeri che contengono almeno un 3
    #if "3" in numero:
    #    conta_tre = conta_tre + 1
    
    # conta tutti i caratteri "3" all'interno di ciascun numero inserito dall'utente
    for cifra in numero: # itero sulla stringa che rappresenta il numero per valutare una cifra alla volta
        if int(cifra) == 3: 
            conta_tre = conta_tre + 1
    
    #conta_tre = conta_tre + numero.count("3")
    numero = input("Inserire un numero: ")

    isValid = numero != "*" 

    if not isValid:
        print("Interruzione ciclo!")

print (f"Ho incontrato {conta_tre} numeri tre")