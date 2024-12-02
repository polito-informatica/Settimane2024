from csv import reader

f = open('voti.csv', 'r', encoding='utf-8')

csv_reader = reader(f)

for campi in csv_reader:
    print(campi)

f.close()