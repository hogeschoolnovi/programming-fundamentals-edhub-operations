# ==========================================
# Voorbeeld Opdracht
# Schrijf de notatie van een 10 miljoen. Gebruik de ‘leesbaarheid methode’ van Python.
# print het getal.
# ==========================================

print(10_000_000)  # Het resultaat is: 10000000


# ==========================================
# Opgave 1:
# Welk getal is goed geschreven volgens de ‘leesbaarheid methode’
# print het getal.

#     100_00.000_001
#     1_000.00_001
#     1_000_000.000_1
# ==========================================

print(1_000_000.000_1)  # Het resultaat is: 1000000.0001


# ==========================================
# Opgave 2:
# Hoe schrijf je de volgende getallen uit in de wetenschappelijke notatie van Python?
# print de getallen.

#     -12.000.000
#     0.13 met drie extra nullen (0.00013)
#     64.000.000.000
# ==========================================

# Alle resultaten worden floats
print(-12E6)  # Het resultaat is: -12000000.0
print(0.13E-3)  # Het resultaat is: 0.00013
print(64E9)  # Het resultaat is: 64000000000.0


# ==========================================
# Opgave 3:
# Schrijf 5 miljoen uit. Hoe maak je daar met behulp van de wetenschappelijke notatie 0.05 van?
# ==========================================

# Print 5 miljoen
print(5_000_000)  # Het resultaat is: 5000000
# Maakt van 5 miljoen 0.05 met behulp van de wetenschappelijke notatie
print(5_000_000E-8)  # Het resultaat is: 0.05


# ==========================================
# Opgave 4:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.

# a. 11 * 3
# b. 7.5 – 1.5
# c. 3 + 4.0
# d. 15 / 5
# ==========================================

print(11 * 3)     # Het resultaat is: 33
print(7.5 - 1.5)  # Het resultaat is: 6.0
print(3 + 4.0)    # Het resultaat is: 7.0
print(15 / 5)     # Het resultaat is: 3.0


# ==========================================
# Opgave 5:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.
# a. 18 // 4
# b. 15.5 // 4
# c. 10 % 4
# d. 9 % 4.5
# ==========================================

print(18 // 4)    # Het resultaat is: 4       (int)
print(15.5 // 4)  # Het resultaat is: 3.0     (float)
print(10 % 4)     # Het resultaat is: 2       (int)
print(9 % 4.5)    # Het resultaat is: 0.0     (float)


# ==========================================
# Opgave 6:
# Hieronder staan een aantal expressies. Schrijf voor jezelf in een comment wat de volgorde is en reken het antwoord uit. Check dan met een print statement of je hetzelfde antwoord krijgt

#  A   8 + 2 * 3
#  B   (8 + 2) * 3
#  C   2 ** 3 ** 2
#  D   (2 ** 3) ** 2
#  E   100 - 5 ** 2 / 5 * 2
# ==========================================


# De volgorde van operaties in Python volgt de standaard wiskundige regels, vaak samengevat als PEMDAS:

# Parentheses (haakjes): ()
# Exponents (machtsverheffingen): **
# Multiplication (vermenigvuldiging) en Division (deling): *, /, //, %
# Addition (optelling) en Subtraction (aftrekking): +, -

# A. Eerst wordt 2 * 3 uitgevoerd en daarna 8 + 6  ->  Het resultaat is: 14
# B. Eerst wordt 8 + 2 uitgevoerd en daarna * 3  -> Het resultaat is: 30
# C. Eerst wordt 3 ** 2 uitgevoerd en daarna 2 ** 9  ->  Het resultaat is: 512
# D. Eerst wordt 2 ** 3 uitgevoerd en daarna ** 2  -> Het resultaat is: 64
# E. Eerst wordt 5 ** 2 uitgevoerd en daarna / 5 en dan * 3 en dan 100 - 15  -> Het resultaat is: 85


# ==========================================
# Opgave 7:
# Zet de volgende tekst om naar een Python string. Let op speciale tekens en spaties.
# Tip: Herhalende woorden kun je met een operator vaker printen
# Check het resultaat met een print statement

# A: Dit is de vorm van een dak / \
# B: ‘quotes’ ‘quotes’ ‘quotes’ ‘quotes’ spamspamspam
# C: Python’s syntax is “eenvoudig”
# ==========================================

print("Dit is de vorm van een dak / \\")  # Het resultaat is: Dit is de vorm van een dak / \
print(3 * 'quotes ', 3 * 'spam')  # Het resultaat is: quotes quotes quotes spamspamspam
print("Python's syntax is \"eenvoudig\"")  # Het resultaat is: Python's syntax is "eenvoudig"
