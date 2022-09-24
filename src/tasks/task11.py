# TAKS 11

# Erstelle eine Funktion, die dir errechnet wie viele Münzen du für eine Bestimmte
# Eingabe von Cents erhältst.

def calcNumCoins(cents: int) -> int:
    """Calculate number of coins by given cents.

    Args:
        cents (int): Number of cents given.

    Returns:
        int: Lowest number of coins by given cents. 
    """
    # Anzahl der Münzen
    numCoins = 0

    # Wenn weniger als 0 Cent eingeben wurden
    if cents <= 0:
        return numCoins

    # Mögliche Münzen von 2€ zu 1ct (Absteigende Reihenfolge!)
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    # Prüfe für jede Münze wie oft sie den gegebenen Cent-Betrag darstellen kann
    for coin in coins:
        numCoins += cents//coin     # Anzahl der Münzen
        cents %= coin               # Restbetrag

        # Keine Cents mehr übrig
        if cents == 0:
            break

    return numCoins


# User darf eine Zahl eingeben
ct = int(input('Wie viele Cent hast du? '))
print(f'Anzahl der Münzen: {calcNumCoins(ct)}')
