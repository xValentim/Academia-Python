import csv
with open('data.csv', 'r') as data:
    arquivo = csv.DictReader(data)
    for row in arquivo:
        print(row['assunto'])