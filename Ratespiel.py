import random

zufallszahl = random.randint(1,100)
ratezahl = 0
while ratezahl != zufallszahl:
    ratezahl = input("Rate die Zahl:")
    if ratezahl > zufallszahl:
        print ratezahl,"ist zu groß."
print "Glückwunsch,",zufallszahl,"ist die richtige Zahl!"
