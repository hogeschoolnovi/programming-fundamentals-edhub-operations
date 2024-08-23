# ==========================================
# Voorbeeld Opdracht
# Gebruik de not operator om het tegenovergestelde van de boolean waarde True te printen.
# ==========================================

print(not True)     # Het resultaat is: False


# ==========================================
# Opgave 1.
# Gebruik logische operatoren om te controleren of het getal 5 zowel groter is dan 3 als kleiner dan 10.
# Print het resultaat.
# Controleer daarna of 5 groter is dan 10 of gelijk is aan 5.
#
# Verwachte uitkomst is de boolean waarde: True
# ==========================================

print(5 > 3 and 5 < 10)     # Het resultaat is: True


# ==========================================
# Opgave 2.
# Evalueer of het getal 7 zowel groter is dan 5 als kleiner dan 12, en tegelijkertijd niet gelijk is aan 10.
# Print het resultaat.
#
# Verwachte uitkomst: True
# ==========================================

print(7 > 5 and 7 < 12 and not (7 == 10))     # Het resultaat is: True


# ==========================================
# Opgave 3
# Gegeven is x = 5 en y = -5
# Gebruik logische operatoren om te controleren of de variabelen positief zijn en kleiner dan 10. Print het resultaat als boolean waarde.
#
# Verwachte uitkomst voor x is: True
# Verwachte uitkomst voor y is: False
# ==========================================

x = 5
y = -4

print(x > 0 and x < 10)     # Het resultaat is: True
print(y > 0 and y < 10)     # Het resultaat is: False


# ==========================================
# Opgave 5.
# Geef aan wat het resultaat zou zijn van de volgende code:

# A. print(True or 1 / 0)
# B. print(True or False)
# C. print(False and True and True)
# D. print(True or False or False)
# E. print(not True or False or not True)
# ==========================================

# A.
print(True or 1 / 0)     # Het resultaat is: False
# Het resultaat is True. De 'or' operator kijkt of er minimaal een True waarde in de expressie voorkomt. Zodra er een True waarde is, is het resultaat True en wordt de rest van de expressie niet geëvalueerd. Als dat wel zo was zou de expressie een ZeroDivisionError geven op 1 / 0

# B.
print(False or True)     # Het resultaat is: True
# Als er een True waarde voorkomt in een 'or' evaluatie is het resultaat True.

# C.
print(False and True and True)     # Het resultaat is: False
# Een 'and' operator evalueert alleen naar True als beide zijden True zijn.

# D.
print(True or False or False)     # Het resultaat is: True
# Zodra er in een 'or' evaluatie een True waarde voorkomt is het resultaat True.

print(not True or False or not True)     # Het resultaat is: False
# Door de 'not' operator evalueert de True naar een False. Omdat er geen enkele True waarde in de expressie voorkomt is het resultaat False.


# ==========================================
# Opgave 6:
# Evalueer of een nummer even of oneven is.
# Maak een variabele 'nummer' aan met de waarde 42,
# Schrijf de evaluatie die bepaalt of het nummer even of oneven is. Print de string 'Even' als het nummer even is, anders print 'Oneven'.
# Tip: Als het nummer gedeeld door 2 geen restwaarde heeft, dan is het even. Anders is het oneven.
# ==========================================

nummer = 42
even_of_oneven = "Even" if nummer % 2 == 0 else "Oneven"
print(even_of_oneven)     # Het resultaat is: Even


# ==========================================
# Opgave 7:
# Begroeting op Basis van het Uur van de Dag
#
# Stel je hebt een klok die aangeeft dat het 9 uur 's ochtends is (uur = 9).
# Afhankelijk van het tijdstip wil je een passende begroeting gebruiken: "Goedemorgen", "Goedemiddag", of "Goedenavond".
# Met een conditionele expressie kun je besluiten: als het uur minder dan 12 is, zeg "Goedemorgen"; als het minder dan 18 is, zeg "Goedemiddag"; en anders, zeg "Goedenavond".
# Voor 9 uur 's ochtends zou de gekozen begroeting "Goedemorgen" zijn. Tip: je kunt meerdere keren ‘else’ achterelkaar zetten.
#
# Check het resultaat met de print() methode. Veranderde de waarde van 'uur' om te zien of de begroeting verandert.
# ==========================================

uur = 9
begroeting = "Goedemorgen" if uur < 12 else "Goedemiddag" if uur < 18 else "Goedenavond"

print(begroeting)     # Het resultaat is: Goedemorgen


# =========================================
# Opgave 8:
# Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren. Print daarna de som en het product van de getallen.
# De input functie moet vragen 'Voer eerste getal in :' en 'Voer tweede getal in :'
# Zorg ervoor dat de input ook kommagetallen accepteert.
#
# Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# ==========================================

getal_een = float(input('Voer eerste getal in :'))
getal_twee = float(input('Voer tweede getal in :'))

print('De som van', getal_een, 'en', getal_twee, 'is :', getal_een + getal_twee)
