import csv

with open("C:\\Users\\sortfile.csv", 'r') as fopen:
    rows = csv.reader(fopen)
    csvf = list(rows)

x = 0
array = []

while True:
    lines = []
    try:
        for i in csvf:
            lines.append(i[x])
        array.append(lines)
        x +=1
    except IndexError:
        break
