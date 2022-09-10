# TASK 4

# 1. Definiere eine Variable mit allen Monaten eines Kalendarjahres. Verwende als
# Schlüssel die Monatsabkürzungen (drei Buchstaben) und als Wert die Monate.

months = {
    'jan': 'Januar',
    'feb': 'Februar',
    'mar': 'März',
    'apr': 'April',
    'mai': 'Mai',
    'jun': 'Juni',
    'jul': 'Juli',
    'aug': 'August',
    'okt': 'Oktober',
    'sep': 'September',
    'nov': 'November',
    'dez': 'Dezember',
}

print(f'months.keys(): \n{months.keys()}\n\n'
      f'months.values(): \n{months.values()}\n\n'
      f'months.items(): \n{months.items()}\n\n'
      f'months.get("sep"): \n{months.get("sep")}\n\n')
