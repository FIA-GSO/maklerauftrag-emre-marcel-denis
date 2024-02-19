class Raum:
    def __init__(self, laenge, breite, name, raumgroesse):
        self.name = name
        self.laenge = laenge
        self.breite = breite
        self.raumgroesse = laenge * breite

raeume = 0

while True:
    try: 
        raeume = int(input("Hey Makler, Gebe die Anzahl an Räumen an welches das Gebäude hat: "))
        Raum.name = str(input("Wie ist der Name deines Raumes? "))
        Raum.laenge = int(input("Gebe die Länge deines Raumes (in Metern) an: "))
        Raum.breite = int(input("Gebe die Breite deines Raumes (in Metern) an: "))
        break
    except ValueError:
        print("Die Eingabe ist Falsch, bitte erneut eingeben.")

input("einfach nur nen test")

# print("Dein Gebäude hat " + str(raeume) + " Räume und der Name des Raumes lautet: " + Raum.name + " Die länge beträgt: " + str(Raum.laenge) + "m und die Breite beträgt: " + str(Raum.breite) + " Die Raumgröße ist: " {Raum.raumgroesse})
# print("Dein Gebäude hat " + raeume + " Rä)