# TASK 10

# Bestimmen Sie, welche der folgenden Zahlen natürliche, ganze, rationale, reelle
# oder komplexe Zahlen sind. (Geben Sie jeweils alle zutreffenden Bezeichnungen an.)

from email.policy import default
from math import pi, sqrt
from typing import Any


def numClassificator(n: Any) -> None:
    '''Klassifiziert eine Zahl in dessen Zahlenbereich.

    Args:
        n: Beliebige Zahl
    '''
    match n:
        case complex():
            print(f'{n} ist eine komplexe Zahl.')
        case int():
            print(f'{n} ist eine {"natürliche Zahl" if n >= 0 else "ganze Zahl"}.')
        case float():
            print(f'{n} ist möglicherweise eine rationale Zahl.')
        case _:
            print(f'"{n}" ist vom Typ {type(n)} und keine Zahl.')


testNumbers = [3, -3, -(8//2), 4/10, pi, 2j, sqrt(2) / 7, 12, 'Vorkurs Gruppe 2']
for num in testNumbers:
    numClassificator(num)
