# TASK 0

# Gegebene Infos: ohne Zurücklegen
cnt_red = 2  # zwei rote Kugeln
cnt_yellow = 3  # drei gelbe Kugeln
cnt_both = cnt_red + cnt_yellow

# b.1) r1: Wahrscheinlichkeit dafür, dass die erste Kugel rot ist
p_r1 = cnt_red / cnt_both  # p_r1 = 2/5
print(
    f'Die erste Kugel ist mit einer Wahrscheinlichkeit von p = {p_r1} eine rote Kugel.')

# b.2) g2: Wahrscheinlichkeit dafür, dass die zweite Kugel gelb ist
# Es muss unterschieden werden, ob beim ersten Versuch gelb oder rot gezogen wurde
# p_g2 = 2/5 * 3/4 + 3/5 * 2/4
p_g2 = cnt_red/cnt_both * cnt_yellow/(cnt_both-1) + cnt_yellow/cnt_both * (cnt_yellow-1)/(cnt_both-1)
print(f'Die zweite Kigel ist mit einer Wahrscheinlichekeit von p = {p_g2} eine gelbe Kugel.')

# c) Definition: P(A|B) = P(A ∩ B) / P(B)
p_both = cnt_red/cnt_both * (cnt_yellow-1)/(cnt_both-1) # p_both = 2/5 * 3/4

p_g2r1 = p_both / p_r1
print(f'P(G2|R1) lautet: {p_g2r1}')

p_r1g2 = p_both / p_g2
print(f'P(R1|G2) lautet: {p_r1g2}')
