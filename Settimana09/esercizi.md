# Esercizio Numeri - 7

Codifica Modulo e Segno

010011+011101

0    10011 
0    11101
     -----
   1 10000 la somma dei moduli è una somma tra numeri in binario puro
            quindi l'overflow è indicato dall'eventuale riporto

   Overflow perché il modulo del risultato non è rappresentabile su 5 bit

Risultato: 010000 (overflow)


011101+110111  =>   +11101 + -10111

L'operazione da fare è la sottrazione dei moduli

   11101 -
   10111
   -----
   00110 ok non ho avuto overflow

Risultato: 000110

# VARIANTE

Codifica Complemento a 2
010011+011101

  010011+
  011101
  ------
  110000   => overflow perché la somma di 2 positivi non può essere negativa

011101+110111

  011101+
  110111
  ------
1 010100   -> ok, nessun overflow. Somma un positivo con un negativo, risultato positivo ok

Risultato: 010100

# Esercizio Numeri - 10

base 8  - base 2

007   00 000 111
7            111

7         11 111 111   -->  00 000 111
13        00 001 011
          ----------
          00 001 010

          00 001 010
11        00 001 001
          ----------
          00 010 011  -> in base 8: 023


111 è in CA2 su 3 bit --> vale -1
scrivilo su 6 bit
111111

# Esercizio Numeri - 48

A = 1AF e B = 8F02, calcola A-B

facciamo le operazioni su 16 bit: 01AF - 8F02

  0000 0001 1010 1111  -
  1000 1111 0000 0010 =
  -------------------
  0111 0010 1010 1101    ==>  no overflow : (+) - (-) = (+)

in base 16 è 72AD
in base 10 te lo calcoli

# Esercizio Numeri - 20

AF04, 8711

1010 1111 0000 0100   è il maggiore
1000 0111 0001 0001
-------------------
0011 0110 0001 0101  ==> OVERFLOW la somma di due negativi non può essere positivo

3615

# Esercizio Numeri - 17

Rappresentazione in virgola mobile separa in segno S, la mantissa M e l'esponente E
dedicando un certo numero di bit ciascuna. Lo standard ci dice quanti bit e come 
sono codificate queste parti.

valore =    S  * M  * (2 ^ E)
E può essere positivo o negativo, ed indica di quanti "posti" occorre spostare la virgola.

Vantaggio: è possibile con un numero fisso di bit rappresentare numeri "molto grandi" o "molto piccoli", mantenendo un certo numero di cifre decimali significative, che dipendono
da quanti bit dedico a M.

# Esercizio Architetture - 2

Bus seriale trasferisce 1 bit solo per volta (DBUS = 1 bit)
    USB universal serial bus
    HDMI
    meno costoso
    più semplice
    cablaggi "magri"
    talvolta ad alta velocità

Bus parallelo trasferisce una "parola" di N bit per volta (DBUS = N bit)
    bus interni
    più veloci
    più costosi
    complessi a livello di cablaggio
    limitata la lunghezza massima

# Esercizio Architetture - 51

RAM = 64 GB
Cache = 4 GB
Memoria parallelismo 128 bit
ABUS ?

   MEM = 2^ABUS * DBUS

DBUS = dimensione cella = 128 bit

MEM (RAM) = 64 GB

64 G B = 2^ABUS * 128 b
2ˆ6 2ˆ30 2ˆ3 b = 2^ABUS * 2ˆ7 b
2^39 = 2^ABUS * 2^7

ABUS = 39 - 7 = 32 bit (minimo)

# Esercizio Architetture - 55

ABUS = 10 bit 

Celle di memoria = 2ˆ10 = 1024 celle

Cella = 2 byte

Quantitià di memoria = numero di celle * dimensione della cella = 1024 * 2 B = 2048 B = 2 kB

# Esercizio Numeri - 37

convertire in CA2 su 6 bit

    +60
    -60
    +70
non si può perché il CA2 su 6 bit rappresenta numeri tra -2ˆ5 e +2ˆ5-1 cioè -32 e + 31.

Se invece fossero 8 bit

60 = 32 + 16 + 8 + 4    =    00111100

-60: complemneto il +60

inverto i bit  11000011
sommo 1        00000001
               --------
               11000100  => -60

+70 = 64+4+2  =  01000110

# Esercizio Python - 1

SI parla di alias quando due VARIABILI diverse fanno riferimento allo stesso VALORE.
QUindi gli stessi dati sono raggiungibili in modi diversi.
Il problema è che modificando il contenuto di una variabile, risulta modificato anche l'altro contenuto
Oppure un problema è che si può "rompere" il collegameto se ri-assego una delle due variabili