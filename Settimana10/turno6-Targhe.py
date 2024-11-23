"""
Le targhe delle auto italiane seguono un formato standard, di 7 caratteri ciascuna (2 lettere maiuscole, 3 cifre decimali, 
2 lettere maiuscole). Ad esempio, `"AB123CD"`.
Tuttavia, non tutte le lettere sono ammissibili, per evitare confusione con la forma di alcuni numeri. In paticolare, 
le lettere `'I'`, `'O'` e `'Q'` non sono ammesse. Inoltre, le prime due lettere non possono essere `"EE"`.

Data una lista di stringhe denominata 'targhe', che contiene una serie di codici alfanumerici, effettuare due operazioni:
- costruire una lista di valori booleani, denominato 'valide', della stessa lunghezza di 'targhe', che contenga il valore True per tutte e sole le targhe che rispettano i criteri indicati
- costruire una lista di stringhe, denominata 'targhe_valide', che contiene tutte e sole le targhe valide tra quelle di partenza, nello stesso ordine.

Ad esempio, dato:
```python 
targhe = ['AB123CD', 'EE123CD', 'AB123CE', 'AB123CO', 'AB123CI', 'AB123CQ', 'ab123fg', 'AB123', 'AB888EE']
```
si calcolerà:
```python    
valide = [True, False, True, False, False, False, False, False, True]
targhe_valide = ['AB123CD', 'AB123CE', 'AB123CD', 'AB123CD', 'AB888EE']
```
"""

targhe = [
    "AB123CD",
    "EE123CD",
    "AB123CE",
    "AB123CO",
    "AB123CI",
    "AB123CQ",
    "ab123fg",
    "AB123",
    "AB888EE",
]
