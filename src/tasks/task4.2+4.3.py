# TASK 4

# 2. Stelle dir vor, du schreibst ein Programm für die Verwaltung der Bestände eines
# Buchhändlers. Zu jedem Buch sollen der Titel, der Autor, eine Artikelnummer und
# der Preis gespeichert werden. Schreibe drei Programme, die jeweils eine Liste,
# ein Dictionary bsw. ein Tupel verwenden. Jedes Programm soll die Werte für drei
# Bücher abspeichern und die Daten anschließend auf dem Bildschirm ausgeben.

# Die Ausgabe soll dabei nicht als komplette Liste erfolgen, sondern jeder Wert
# soll in einer eigenen Zeile stehen. Nach jedem Buch soll eine Leerzeile folgen.
# Dazu dient das Zeichen \n.

# ------------ Dictionaries ----------------------------------------------------

books = [
    {
        'Titel': 'Distributed Systems',
        'Autor': 'Marten van Steen, Andrew S. Tanenbaum',
        'Artikelnummer': 0,
        'Preis': 19.95,
    },
    {
        'Titel': 'Modern Operating Systems, 4th Edition',
        'Autor': 'Andrew S. Tanenbaum',
        'Artikelnummer': 1,
        'Preis': 34.12,
    },
    {
        'Titel': 'Academic English for Computer Science',
        'Autor': 'Noni Rizopoulou',
        'Artikelnummer': 2,
        'Preis': 23.42,
    },
]

# Alternative 1: Naive Methode, aber mit Formatierung
for book in books:
    for key in book.keys():
        if key == 'Preis':
            print(f'{key}: {book.get(key)}€', end=' | ')
            continue
        print(f'{key}: {book.get(key)}', end=' | ')
    print()  # print('\n')

# Alternative 2: Pointer auf eine Liste (keine Formatierung)
print(*books, sep='\n', end='\n\n')

# Alternative 3: Inline Loops (keine Formatierung)
print(*[[f'{book.get(key)}' for key in book.keys()] for book in books], end="\n\n")

# ---------------- Tupel -------------------------------------------------------

books = {
    'buch0': ('Distributed Systems', 'Marten van Steen, Andrew S. Tanenbaum', 0, 19.95),
    'buch1': ('Modern Operating Systems, 4th Edition', 'Andrew S. Tanenbaum', 1, 34.12),
    'buch2': ('Academic English for Computer Science', 'Noni Rizopoulou', 2, 23.42),
}

for book in books.items():
    for attribut in book[1]:
        if attribut == book[-1]:
            print(f'{attribut}€', end=' | ')
            continue
        print(attribut, end=' | ')
    print()  # print('\n')

# Alternativ:
for book in books.items():
    print(f'Titel: {book[1][0]} | Author: {book[1][1]} | '
          f'Artikelnummer: {book[1][2]} | Preis: {book[1][3]}€')

# ---------------- Lists -------------------------------------------------------

books = [
    ['Distributed Systems', 'Marten van Steen, Andrew S. Tanenbaum', 0, 19.95],
    ['Modern Operating Systems, 4th Edition', 'Andrew S. Tanenbaum', 1, 34.12],
    ['Academic English for Computer Science', 'Noni Rizopoulou', 2, 23.42],
]

# Tupel ist eine read-only Liste -> Code für die Ausgabe ist identisch
for book in books:
    for attribut in book:
        if attribut == book[-1]:
            print(f'{attribut}€', end=' | ')
            continue
        print(attribut, end=' | ')
    print()  # print('\n')
