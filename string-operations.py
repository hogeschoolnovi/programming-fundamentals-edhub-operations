# ==========================================
# Voorbeeld Opdracht
# Gegeven is de string ‘Python’ en het getal 3.
# Maak met deze variabelen de volgende string: ‘Python Python Python’ Gebruik een operator.
# ==========================================

woord = 'Python '
aantal_keer = 3

print(woord * aantal_keer)  # Het resultaat is: Python Python Python


# ==========================================
# Opgave 1:
# Maak de volgende zin in Python: Bello is 4 jaar. Dit is 28 jaar in mensenjaren.
# Je hebt de volgende variabelen: leeftijd_hond = 4 en naar_mensen_jaren = 7
# Maak een variabele aan genaamd 'mensen_jaren’. Ken daar de waarde aan toe van leeftijd_hond maal naar_mensen_jaren.
# Schrijf nu de zin met de print() methode.
# ==========================================

bello_hondenjaren = 4
naar_mensen_jaren = 7
bello_mensenjaren = bello_hondenjaren * naar_mensen_jaren

print('Bello is ', bello_hondenjaren, 'jaar. Dit is', bello_mensenjaren, 'jaar in mensenjaren')



# ==========================================
# Opgave 2:
# Wat zijn de datatypes van de gegeven variabelen?
# Bedenk het antwoord vooraf en check het met de print() methode die het type van de variabele print.
# ==========================================

variabele_een = '5'
variabele_twee = 1 / 1
variabele_drie = 'Python' * 3

print(type(variabele_een))      # Het resultaat is: <class 'str'>
print(type(variabele_twee))     # Het resultaat is: <class 'float'>
print(type(variabele_drie))     # Het resultaat is: <class 'str'>



# ==========================================
# Opgave 3:
# Niet alle variabele namen zijn toegestaan in Python. Sommige namen zijn gereserveerd voor Python zelf (keywords).
# Welke van de volgende variabele namen kun je gebruiken zonder dat je een foutmelding krijgt? Bedenk het antwoord vooraf en check het door de variabelen aan te maken.

# a.     And = ‘something’
# b.     while = ‘something’
# c.     Break = ‘something’
# d.     none = ‘something’
# ==========================================


# And = 'something'
# Valide syntax. 'and' met een kleine letter is wel een keyword (vergelijkingsoperator), maar 'And' met een hoofdletter niet

# while = 'something'
# Foutmelding. Dit keyword is gereserveerd voor de while loop

# Break = 'something'
# Valide syntax: 'break' met een kleine letter is een keyword om uit een loop te komen, maar 'Break' met een hoofdletter niet

# none = 'something'
# Valide syntax: 'None' met een hoofdletter is een keyword (geeft een lege waarde aan), maar 'none' met een kleine letter niet


# LET OP: Hoewel deze variabele namen technisch gezien kunnen worden gebruikt, is het niet aan te raden om dit te doen. Het kan verwarrend zijn voor andere programmeurs die je code lezen.



# ==========================================
# Opgave 4:
# Schrijf een goede variabele naam voor:

# a.     Het totale aantal van een product (bananen)
# b.     De minimale toegestane lengte voor een attractie in een pretpark
# c.     Het grootste getal in een rij met getallen

# Denk ook aan de schrijf conventies voor variabele namen.
# ==========================================

# a. totaal_aantal_bananen
# b. min_lengte_voor_attractie
# c. grootste_getal_uit_rij


# LET OP: Wees specifiek en beschrijvend in je variabele namen. De benaming mag best wat langer zijn als dit de duidelijkheid van je code ten goede komt.


# ==========================================
# Opgave 5:
# Maak onderstaande opgaven
# Maak van het getal 3.14 een 3. Je mag alleen de typecast functie gebruiken
# ==========================================

getal = 3.14

print(int(getal))  # Het resultaat is: 3


# ==========================================
# Opgave 6:
# Gegeven zijn mijn_variabele = 5 en print(mijn_variabele * 3)
# Zorg ervoor dat de uitkomst van de print() methode ‘555’ is zonder dat je een andere getalswaarde toekent aan mijn_variabele.
# De gegeven code mag je niet aanpassen, maar je mag wel extra code toevoegen.
# ==========================================

mijn_variabele = 5
# Door te typecasten naar een string wordt er twee keer een vijf achter elkaar geprint in plaats van dat er twee getallen worden vermenigvuldigd
mijn_variabele = str(mijn_variabele)

print(mijn_variabele * 3)  # Het resultaat is: 555



# ==========================================
# Opgave 7:
# Welke van de gegeven print() statements zullen een foutmelding veroorzaken? Bedenkt het antwoord vooraf en check het door de code uit te voeren.
# ==========================================

# print(int('1490.99'))
# Foutmelding (alleen als in de string een heel getal staat kan deze worden omgezet naar int)

# print(float(12))
# Geen foutmelding (Python zet de waarde om in een float 12.0)

# print(int('1plus1'))
# Foutmelding (de string bevat een woord. Dat kan niet worden omgezet naar een getal)

# print(str(25E10))
# Geen foutmelding (25E10 betreft wetenschappelijke notatie. Dit wordt een 25 met 10 nullen en kan als zodanig in een string worden omgezet). Wat opvalt is dat Python eerst de wetenschappelijke notatie omzet naar een float en vervolgens naar een string. Het resultaat is dus '250000000000.0' in plaats van '25E10'.
