# visualizza un riquadro di numeri 0 di larghezza
# n e altezza m

"""
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
"""

N = 4
M = 4

for i in range(1, N+1):
    #print("Indice for esterno", i)
    for j in range(1, M+1):
        #print(f'Esterno: {i}; Interno {j}')
        print("0 ", end="")
    print()


