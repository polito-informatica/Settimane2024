# Generare una nuova stringa a partire 
# dalla stringa "Università"
# sostituendo a tutte le "i" nella prima metà
# il carattere "1"

#parola = "Università"
parola = "Uiiiiiiiiiiiniversità"

# usando solo .replace() - sbagliato
s1 = parola.replace("i", "1")
print(s1)

# Usando .replace() con n di occorrenze da sostituire
# come terzo parametro - non è generalizzabile
s2 = parola.replace("i", "1", 1)
print(s2)

# basandoci sulla lunghezza della stringa
lunghezza = len(parola)
print(lunghezza)

meta_lunghezza = lunghezza // 2
prima_meta = parola[:meta_lunghezza]
seconda_meta = parola[meta_lunghezza:]
print(prima_meta)
prima_meta = prima_meta.replace("i","1")
print(prima_meta)

nuova_parola = prima_meta + seconda_meta
print(nuova_parola)