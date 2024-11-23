"""
Lo studio di una funzione ha determinato una serie di 'zeri' di una funzione, ossia le ascisse in cui la funzione si azzera. Tali ascisse sono memorizzate in una lista 'zeri' di numeri reali. Gli zeri sono riportati in un ordine qualsiasi. Ad esempio:

```python
zeri = [-84.71, -17.58, 6.85, 1.34, -91.5, 78.47, -62.66, -6.13]
```

Per ciascuno di tali zeri (tranne il minimo ed il massimo), è possibile identificare lo zero che sta immediatamente alla sua sinistra, e lo zero che sta immediatamente alla sua destra, sulla retta dei numeri.
Ad esempio, 1.34 è preceduto da -6.13 e seguito da 6.85, mentre -17.58 è preceduto da -62.66 e seguito da -6.13.

Si stampi, per ciascuno degli zeri iniziali (tranne il minimo ed il massimo) la coppia di zeri che sono immediatamente adiacenti

Nel caso di esempio, si stampi (non è importante l'ordine in cui vengono stampati):

```
-84.71 si trova tra -91.5 e -62.66
-62.66 si trova tra -84.71 e -17.58
-17.58 si trova tra -62.66 e -6.13
-6.13 si trova tra -17.58 e 1.34
1.34 si trova tra -6.13 e 6.85
6.85 si trova tra 1.34 e 78.47
```
"""

zeri = [-84.71, -17.58, 6.85, 1.34, -91.5, 78.47, -62.66, -6.13]
