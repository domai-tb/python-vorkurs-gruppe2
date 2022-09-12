# TASK 6

# 1. Jemand möchte sich eines der vier oben abgebildeten Tablet-Modelle kaufen.
# Schreibe ein Programm, dass den Käufer nach einem Maximalpreis fragt, den er
# höchstens für das Tablet zahlen will.
#
# Das Programm soll nun alle Tablets mit ihren Eigenschaften ausgeben, deren
# Preis kleiner oder gleich dem Maximalpreis ist.

tabletModels = [
    {
        'name': 'Galaxy Tab A',
        'marke': 'Samsung',
        'display': 'TFT',
        'fqz': 60,
        'größe': 10.1,
        'preis': 210,
    },
    {
        'name': 'Galaxy Tab S7+',
        'marke': 'Samsung',
        'display': 'OLED',
        'fqz': 120,
        'größe': 12.4,
        'preis': 955,
    },
    {
        'name': 'iPad Air',
        'marke': 'Apple',
        'display': 'RETINA',
        'fqz': 60,
        'größe': 10.5,
        'preis': 500,
    },
    {
        'name': 'Mad Pad pro',
        'marke': 'Huawei',
        'display': 'AMOLED',
        'fqz': 60,
        'größe': 10.8,
        'preis': 510,
    },
]

maxPreis = int(input('Was ist der maximale Preis, den Sie ausgeben wollen? '))
for tablet in tabletModels:
    if tablet['preis'] > maxPreis:
        continue
    for key in tablet.keys():
        print(f'{key}: {tablet.get(key)}', end=', ')
    print()

# 2. Schreibe ein Programm, das dem Anwender fünf einfache Rechenaufgaben stellt.
# Überprüfe die Eingabe. Wenn das Ergebnis richtig ist, erhält der Anwender einen
# Punkt. Gib nach dem Ende der Aufgaben eine Bewertung aus.

randomNumber0 = 42
randomNumber1 = 21
points = 0

test0 = int(input(f'Was ergibt {randomNumber0} + {randomNumber1}? '))
test1 = int(input(f'Was ergibt {randomNumber0} - {randomNumber1}? '))
test2 = int(input(f'Was ergibt {randomNumber0} * {randomNumber1}? '))
test3 = int(input(f'Was ergibt {randomNumber0} : {randomNumber1}? '))
test4 = input(f'Was ergibt {randomNumber1} : 0? ')

if test0 == randomNumber0+randomNumber1:
    points += 1
if test1 == randomNumber0-randomNumber1:
    points += 1
if test2 == randomNumber0*randomNumber1:
    points += 1
if test3 == randomNumber0/randomNumber1:
    points += 1
if test4 == 'nl':
    points += 1

match points:
    case 0:
        print(f'[{points} Pkt.] Dringend Nachhilfe benötigt!')
    case 1 | 2:
        print(f'[{points} Pkt.] Viele Fehler: weitere Übung erforderlich!')
    case 3 | 4:
        print(f'[{points} Pkt.] Gute Leistung!')
