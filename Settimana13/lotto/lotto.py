"""

SCELGO LA PRIMA FORMA

estrazioni = [
    {
        "data": "2001/03/10",
        "ruota": "RM",
        "numeri": { 74, 30, 35, 26, 8 }
    },
    {
        "data": "2001/03/10",
        "ruota": "TO",
        "numeri": { 22, 35, 14, 68, 57 }

    },

]

estrazioni = [
    {
        "data": "2001/03/10",
        "estrazioni": [
            {
                "ruota": "RM",
                "numeri": [ 74, 30, 35, 26, 8]
            },
            {
                "ruota": "TO",
                "numeri": [ 22, 35, 14, 68, 57]
            }
        ]
    }
]
"""

import operator


def leggi_estrazioni(nome_file):
    estrazioni = []
    with open(nome_file, "r", encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split()
            numeri = set()
            for n in campi[2:]:
                numeri.add(int(n))
            estrazioni.append( {
                "data": campi[0],
                "ruota": campi[1],
                "numeri": numeri
            })

    return estrazioni


def trova_comuni(estrazioni, ruota1, ruota2):
    """
    la funzione trova tutti i numeri che sono usciti nella stessa data in ruota1 e routa2, e 
    restituisce una lista di tali co-occorrenze, nel formato:
    [ { "numero": 6, "data": "2001/01/27"}, { "numero": 36, "data": "2001/02/10"}, ... ]
    """
    cooccorrenze = []

    for estrazione1 in estrazioni:
        for estrazione2 in estrazioni:
            if (estrazione1["data"]== estrazione2["data"] and 
                estrazione1["ruota"] == ruota1 and
                estrazione2["ruota"] == ruota2 ):
                comuni = estrazione1["numeri"].intersection(estrazione2["numeri"])
                for n in comuni:
                    cooccorrenze.append({"numero": n, "data": estrazione1["data"]})

    return cooccorrenze

def calcola_frequenze(comuni):
    """
    Partendo dalla lista dei numeri comuni, determina le frequenze
    e restituisce un dizionario che contiene, per ogni numero (chiave),
    la sua frequenza di occorrenza (valore)

    { 90: 19, 82: 16, ...}
    """
    frequenze = dict()
    for comune in comuni:
        n = comune["numero"]
        if n in frequenze:
            frequenze[n] = frequenze[n]+1
        else:
            frequenze[n] = 1

        # frequenze[n] = frequenze.get(n, 0)+1
    return frequenze

def main():
    estrazioni = leggi_estrazioni("storico01-oggi.txt")
    # print(estrazioni)

    ruote = sorted({ e["ruota"] for e in estrazioni })
    print(', '.join(ruote))

    ok = False
    while not ok:
        ruota1 = input("Ruota 1: ").upper()
        ruota2 = input("Ruota 2: ").upper()
        if ruota1 in ruote and ruota2 in ruote and ruota1!=ruota2:
            ok = True
        else:
            print('Ripeti...')

    comuni = trova_comuni(estrazioni, ruota1, ruota2)
    
    for comune in comuni:
        print(f"Numero comune {comune['numero']:2d} in data {comune['data']}")

    frequenze = calcola_frequenze(comuni)
    lista_frequenze = list(frequenze.items())
    lista_frequenze.sort(key=operator.itemgetter(1), reverse=True)
    for freq in lista_frequenze:
        print(f"{freq[0]:2d} {freq[1]:3d}")

main()