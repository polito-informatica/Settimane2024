"""
Consideriamo una serie di punti nel piano, dei quali sono memorizzate le coordinate (ascissa, ordinata) in due liste di numeri reali, chiamate rispettivamente 'x' e 'y'.

Ad esempio, supponendo di avere 8 punti nel piano, le coordinate potrebbero essere:

```python
x = [-84.71, -17.58, 6.85, 1.34, -91.5, 78.47, -62.66, -6.13]
y = [54.55, -61.9, 78.31, 37.2, -34.29, -77.22, 68.04, 41.15]
```
Si scriva un frammento di codice Python che, partendo dalle liste 'x' e 'y', determini quali sono i due punti più vicini tra loro (considerando la distanza euclidea calcolata con il teorema di Pitagora), ed i due punti più lontani tra loro. Si stampino le coordinate dei punti trovati.
"""

from math import sqrt

x = [-84.71, -17.58, 6.85, 1.34, -91.5, 78.47, -62.66, -6.13]
y = [54.55, -61.9, 78.31, 37.2, -34.29, -77.22, 68.04, 41.15]

all_dist = []

min_dist = 100000.0
max_dist = 0.0

for i1 in range(len(x)):  # indice del primo punto
    for i2 in range(i1+1, len(x)): # indice del secondo punto
        dist = sqrt((x[i2]-x[i1])**2+(y[i2]-y[i1])**2)
        if dist>max_dist:
            max_dist = dist
            indici_max = [i1, i2]
        if dist<min_dist:
            min_dist = dist
            indici_min = [i1, i2]

print('minima', x[indici_min[0]], y[indici_min[0]], '/', x[indici_min[1]], y[indici_min[1]] )
print('massima', x[indici_max[0]], y[indici_max[0]], '/', x[indici_max[1]], y[indici_max[1]] )