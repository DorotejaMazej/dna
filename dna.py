f = open('dna.txt', 'r')


characteristics = {"blackh": "CCAGCAATCGC",
                   "brownh": "GCCAGTGCCG",
                   "blondeh": "TTAGCTATCGC",
                   "square": "GCCACGG",
                   "round": "ACCACAA",
                   "oval": "AGGCCTCA",
                   "blue": "TTGTGGTGGC",
                   "green": "GGGAGGTGGC",
                   "brown": "AAGTAGTGAC",
                   "female": "TGAAGGACCTTC",
                   "male": "TGCAGGAACTTC",
                   "white": "AAAACCTCA",
                   "black": "CGACTACAG",
                   "asian": "CGCGGGCCG"}

eva = ['female', 'white', 'blondeh', 'oval', 'blue']
larisa = ['female', 'white', 'brownh', 'brown', 'oval']
matej = ['male', 'white', 'blackh', 'blue', 'oval']
miha = ['male', 'white', 'brownh', 'green', 'square']

list = []

values = characteristics.values()

for line in f:
        s = line
s = str(s)

for value, key in characteristics.items():
    if key in s:
        list.append(value)

if list == matej:
    print("Kradel je Matej.")
elif list == larisa:
    print("Kradla je Larisa.")
elif list == eva:
    print("Kradla je Eva.")
else:
    print("Kradel je Miha.")
