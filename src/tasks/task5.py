# TASK 5

# a) Claudia hat 12 Flaschen Limonade für ihre Geburtstagsfeier gekauft. Jede
# Flasche enthält 3/4 Liter Limonade. Sie füllt je 1/5 in die Gläser ihrer Gäste.
# Wie viele Gläser kann Claudia füllen?

# 12 Flaschen * 0.75 Liter * 5 Gläser pro Liter
print(f'Claudia kann {12 * 0.75 * 5} Gläser füllen.')

# b) Leon und Max schwimmen 1000m um die Wette. Leon hat bereits 3/8 und Max 2/5
# der Strecke zurückgelegt. Wie viele müssen Leon und Max jeweils noch schwimmen?
# Wer liegt in Führung?

print(f'Leon muss noch {5/8 * 1000}m zurücklegen. '
      f'Max muss noch {3/5 * 1000}m zurücklegen. '
      f'Damit liegt {"Leon" if 3/8 > 2/5 else "Max"} vorne.')
