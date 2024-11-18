"""
Si consideri il seguente algoritmo (tratto dal problema matematico della "congettura di Collatz"):

Si prenda un intero positivo n.
Se n = 1, l'algoritmo termina.
Se n è pari, si divida per due; altrimenti si moltiplichi per 3 e si aggiunga 1.
Ad esempio, per n=12 l'algoritmo genera la sequenza 12, 6, 3, 10, 5, 16, 8, 4, 2, 1, che ha lunghezza 10.

Si scriva un frammento di codice Python che, partendo da tutti i valori di n compresi tra 1 e 100,
per ciascuno di essi calcoli la lunghezza della sequenza generata dall'algoritmo di Collatz,
e costruisca una lista 'lunghezze' che contenga tali lunghezze.

"""
