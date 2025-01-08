import operator


def leggi_esami(nome_file):
    esami = []
    with open(nome_file, "r") as f:
        for riga in f:
            campi = riga.strip().split(",")

            # converte una data dal formato gg/mm/aaaa al formato aaaa/mm/gg
            campi[1] = "/".join(campi[1].split("/")[::-1])

            esami.append(campi)
    return esami


def leggi_cfu(nome_file):
    cfu = {}
    with open(nome_file, "r") as f:
        for riga in f:
            campi = riga.strip().split(",")
            cfu[campi[0]] = {
                "crediti": int(campi[1]),
                "obbligatorio": bool(int(campi[2])),
            }
    return cfu


def main():
    esami = leggi_esami("esami.log")

    cfu = leggi_cfu("cfu.dati")

    ## ordina la lista degli esami per data crescente
    esami.sort(key=operator.itemgetter(1))

    studenti = dict()
    # studenti['s000001'] = i suoi esami --> solo l'ultima ripetzione, senza A e R
    # esami come lista [codice, voto]
    # esami come dizionario, chiave=codice, valore = lista di voti (lista di [data,voto])

    for esame in esami:
        matricola = esame[0]
        codice = esame[2]
        voto = esame[3]

        if voto != "A" and voto != "R":
            if matricola not in studenti:
                studenti[matricola] = dict()

            studenti[matricola][codice] = voto

    # print(studenti)
    for matricola in studenti:
        tot_crediti = 0
        tot_crediti_obbligatori = 0
        media = 0.0

        print(f"media di {matricola}")
        for codice in studenti[matricola]:
            crediti = cfu[codice]["crediti"]
            obbligatorio = cfu[codice]["obbligatorio"]
            voto = studenti[matricola][codice]
            if voto == "30L":
                voto = 33
            else:
                voto = int(voto)
            # print(codice, crediti, obbligatorio, studenti[matricola][codice])
            tot_crediti = tot_crediti + crediti
            if obbligatorio:
                tot_crediti_obbligatori = tot_crediti_obbligatori + crediti
            media = media + voto * crediti
        media = media / tot_crediti
        print(
            f"CFU totali {tot_crediti}, CFU obbligatori {tot_crediti_obbligatori}, media {media}"
        )
        if tot_crediti >= 30 and tot_crediti_obbligatori >= 10:
            print("Ammissibile")
        else:
            print("Non ammissibile")


main()
