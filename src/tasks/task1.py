# TASK 1

# Ein Glücksrad mit 11 gleichgroßen Feldern (nummeriert mit $1,...,11$) wird 
# einmal gedreht, wobei die Zufallsvariable $X$ die Nummer des erzielten Feldes 
# angibt. Ermitteln Sie den Erwartungswert und die Varianz von $X$.

# Summe aus allen i für i aus [1,11] geteielt durch 11
erwartungswert = sum([i for i in range(1, 12)]) / 11
print(f'Der Erwartungswert beträgt: {erwartungswert}')

# Summe aus allen (i - erwartungswert)² für i aus [1,11] geteielt durch 10
varianz = sum([(i - erwartungswert)**2 for i in range(1, 12)]) / (11 - 1)
print(f'Die Varianz beträgt: {varianz}')