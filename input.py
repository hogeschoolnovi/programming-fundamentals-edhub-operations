# ==========================================
# Voorbeeld Opdracht
# Voer je naam in met de input() methode en print daarna je naam in de console.
# ==========================================

naam = input('Voer je naam in: ')  # voorbeeld invoer: Bart
print('Je naam is: ', naam)  # Het resultaat is: Je naam is: Bart



# ==========================================
# Opgave 1:
# Gegeven is het woord 'Python'. Schrijf een programma dat de gebruiker vraagt om input. Als de gebruiker het woord 'Python' invoert, print dan de boolean True, anders print False.
# ==========================================


woord = 'Python'
invoer = input('Voer een woord in: ')  # voorbeeld invoer: Python

print(invoer == woord)  # Het resultaat is: True (elke andere invoer geeft False)



# ==========================================
# Opgave 2:
# Schrijf een programma dat de gebruiker vraagt om een getal. Voer daarna nog een getal in en print de som van de twee getallen.

# Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# ==========================================

getal_een = float(input('Voer eerste getal in :'))
getal_twee = float(input('Voer tweede getal in :'))
print('De som van', getal_een, 'en', getal_twee, 'is :', getal_een + getal_twee)  # Het resultaat is: De som van 2.0 en 3.0 is : 5.0

# Let op: Standaard is de input() functie een string, ook als je getallen invoert. Hier kan je het beste 'float' voor de input zetten. Dan zal Python ook kommagetallen accepteren. Als je 'int' gebruikt, accepteert de input() functie alleen gehele getallen.

