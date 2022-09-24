# TASK 9

# Erstelle eine Passwort-Abfrage, bei der das Passwort nur aus Ziffern besteht.
# Bei drei Fehleingaben erscheint die Botschaft("three times wrong"). Wenn der
# Nutzer Zeichenketten eingibt, zählt dies nicht als Fehlversuch. Wenn der Nutzer
# das Passwort richtig eingibt, erscheint die Botschaft "nice!".

password = 4242
maxWrong = 3
cntWrong = 0

while cntWrong != maxWrong:
    try:
        userCode = int(input('Bitte geben Sie ihr Passwort ein! '))
        if userCode == password:
            print('nice!')
            break
        else:
            cntWrong += 1
            if cntWrong == maxWrong:
                print(f'{maxWrong} times wrong!')

    except ValueError:
        print(f'Deine Eingabe entspricht nicht den Passwort-Richtlinien!')
