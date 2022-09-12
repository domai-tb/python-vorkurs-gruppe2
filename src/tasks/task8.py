# TASK 8

# Überführe die DNA-Sequenz "ATGACGGATCAGCCGCAAGCGGGG" in die korrekte Petitkette

# 8.1 Transkription:
#       - "Umschreiben" der DNS zu mRNA aka. Messenger-RNA
#       - Definiere Intron -> ATG
#       - Intron wird aus DNA-Sequenz 'gelöscht', weil es nicht codierte Abschnitte
#         der DNA innerhalb eines Gens

dnaSeq = 'ATGACGGATCAGCCGCAAGCGGGG'
intron = 'ATG'

# Intron wird gelöscht
if intron in dnaSeq:
    dnaSeq = dnaSeq.replace(intron, '')

# Erstelle mRNA aus DNA
mrna = ''
for base in dnaSeq:
    if base == "A":
        mrna += "U"
    elif base == "T":
        mrna += "A"
    elif base == "C":
        mrna += "G"
    elif base == "G":
        mrna += "C"

# 8.2 Translation:
#   - bilde jeweils drei Basen auf ein Petit ab
#   - konkatiniere Petite zu Petitkette

tripletts = []
for i in range(0, len(mrna), 3):
    tripletts.append(mrna[i:i+3])  # mrna[0:3], mrna[3:6], mrna[6:9] usw.

petitkette = ''

# Codesonne als if-else Verzweigung
for triplett in tripletts:
    if triplett == "GGG" or triplett == "GGA" or triplett == "GGC" or triplett == "GGU":
        petitkette += "Gly-"
    elif triplett == "GAG" or triplett == "GAA":
        petitkette += "Glu-"
    elif triplett == "GAC" or triplett == "GAU":
        petitkette += "Asp-"
    elif triplett == "GCG" or triplett == "GCC" or triplett == "GCA" or triplett == "GCU":
        petitkette += "Ala-"
    elif triplett == "GUG" or triplett == "GUA" or triplett == "GUC" or triplett == "GUU":
        petitkette += "Val-"
    elif triplett == "AGG" or triplett == "AGA":
        petitkette += "Arg-"
    elif triplett == "AGC" or triplett == "AGU":
        petitkette += "Ser-"
    elif triplett == "AAG" or triplett == "AAA":
        petitkette += "Lys-"
    elif triplett == "AAC" or triplett == "AAU":
        petitkette += "Asn-"
    elif triplett == "ACG" or triplett == "ACC" or triplett == "ACA" or triplett == "ACU":
        petitkette += "Thr-"
    elif triplett == "AUG":
        petitkette += "Met-"
    elif triplett == "AUA" or triplett == "AUC" or triplett == "AUU":
        petitkette += "lle-"
    elif triplett == "UUU" or triplett == "UUC":
        petitkette += "Phe-"
    elif triplett == "UUA" or triplett == "UUG":
        petitkette += "Leu-"
    elif triplett == "UCU" or triplett == "UCA" or triplett == "UCC" or triplett == "UCG":
        petitkette += "Ser-"
    elif triplett == "UAU" or triplett == "UAC":
        petitkette += "Tyr-"
    elif triplett == "UGU" or triplett == "UGC":
        petitkette += "Cys-"
    elif triplett == "AUG":
        petitkette += "Trp-"
    elif triplett == "CUU" or triplett == "CUC" or triplett == "CUA" or triplett == "CUG":
        petitkette += "Leu-"
    elif triplett == "CCU" or triplett == "CCC" or triplett == "CCG" or triplett == "CCA":
        petitkette += "Pro-"
    elif triplett == "CAU" or triplett == "CAC":
        petitkette += "His-"
    elif triplett == "CAA" or triplett == "CAG":
        petitkette += "Gln-"
    elif triplett == "CGU" or triplett == "CGC" or triplett == "CGG" or triplett == "CGA":
        petitkette += "Arg-"

print(petitkette[:-1])
