# TASK 2

# 1. Speichere den oberen DNA-Strang (ATGACGGATCAGCCGCAAGCGG) in einer Variable dna_sequence
dna_sequence = 'ATGACGGATCAGCCGCAAGCGG'

# 2. Gib die Variable mit dem Funktionsausruf print() aus.
print(f'02.: dna_sequence \t\t\t=\t {dna_sequence}')

# 3. Gib den vierten Baustein der dna_sequence aus.
print(f'03.: dna_sequence[3] \t\t\t=\t {dna_sequence[3]}')

# 4. Gib die DNA-Bausteine zwischen Position 4 und 8 aus.
print(f'04.: dna_sequence[3:7] \t\t\t=\t {dna_sequence[3:9]}')

# 5. Besteht die dna_sequence wirklich nur aus Großbuchstaben? Bitte überprüfe es.
print(f'05.: dna_sequence.isupper() \t\t=\t {dna_sequence.isupper()}')

# 6. Aus wie vielen Bausteinen besteht die dna_sequence
print(f'06.: len(dna_sequence) \t\t\t=\t {len(dna_sequence)}')

# 7. Wie häufig kommen die einzelnen DNA-Basen "A", "C", "G" und "T" vor?
print((f'07.: dna_sequence.count("A") \t\t=\t {dna_sequence.count("A")}\n'
       f'     dna_sequence.count("C") \t\t=\t {dna_sequence.count("C")}\n'
       f'     dna_sequence.count("G") \t\t=\t {dna_sequence.count("G")}\n'
       f'     dna_sequence.count("T") \t\t=\t {dna_sequence.count("T")}'))

# 8. Wie häufig kommt das Muster "GG" vor ?
print(f'08.: dna_sequence.count("GG") \t\t=\t {dna_sequence.count("GG")}')

# 9. An welcher Stelle taucht das Muster "GG" zum ersten mal auf?
print(f'09.: dna_sequence.index("GG", 1) \t=\t {dna_sequence.index("GG", 1)}')

# 10. Ersetze alle DNA Bausteine "C" mit "A". Speicher die Veränderung in einer neuen Variable.
dna_seq_modified = dna_sequence.replace("C", "A")
print(f'10.: dna_sequence.replace("C", "A") \t=\t {dna_seq_modified}')

# 11. Gebe für die obere dna_sequence den invertierten 5-3 Strang aus
inverted_repeat = dna_sequence[::-1]                    # invertiere String

# ersezte Basenpaare -> nicht Teil der Aufgabenstellung, aber verdeutlicht Methodenaufrufe
inverted_repeat = inverted_repeat.replace('A', 't') \
                                 .replace('T', 'a') \
                                 .replace('G', 'c') \
                                 .replace('C', 'g') \
                                 .upper()               
print(f'11.: inverted_repeat \t\t\t=\t {inverted_repeat}')

# 12. Erzeuge zwei neue Variablen dna_seq2 und dna_seq3. Jede Variable verfügt
# genau die Hälfte der DNA-Bausteine von dna_sequence. dna_seq2 soll die erste
# Hälfte der DNA-Bausteine von dna_sequence darstellen. dna_seq3 soll die zweite
# Hälfte der DNA-Bausteine von dna_sequence darstellen.
dna_seq2 = dna_sequence[:len(dna_sequence)//2]
dna_seq3 = dna_sequence[len(dna_sequence)//2:]
print((f'12.: dna_seq2 \t\t\t\t=\t {dna_seq2}\n'
       f'     dna_seq3 \t\t\t\t=\t {dna_seq3}'))
