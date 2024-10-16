# calcolare il saldo finale dopo 10 anni
# l'interesse è del 5%
"""

saldo = int(input("Inserire saldo iniziale: "))
INTERESSE = 0.05
i = 0
while i < 10:
    saldo = saldo + saldo * INTERESSE

    print(i+1, saldo)
    i = i + 1
"""

saldo = int(input("Inserire saldo iniziale: "))
INTERESSE = 0.05
i = 0

while saldo < 20000:
    
    saldo = saldo + saldo * INTERESSE
    print(i, saldo)
    
    i = i + 1
