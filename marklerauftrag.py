class Raum:
    def __init__(self, laenge, breite, name, raumgroesse):
        self.name = name
        self.laenge = laenge
        self.breite = breite
        self.raumgroesse = laenge * breite

def raum_abfrage(num):
    alle_raeume = []
    for i in range(num):
        try: 
            Raum.name = str(input("Wie ist der Name deines Raumes? "))
            Raum.laenge = int(input("Gebe die Länge deines Raumes (in Metern) an: "))
            Raum.breite = int(input("Gebe die Breite deines Raumes (in Metern) an: "))
            Raum.raumgroesse = Raum.laenge * Raum.breite

            alle_raeume.append(Raum)
        except ValueError:
            print("Die Eingabe ist Falsch, bitte erneut eingeben.")

    return alle_raeume


def raum_ausgeben(alle_raeume, num):
    for i in range(num):
        print(alle_raeume[num])


# print("Dein Gebäude hat " + str(raeume) + " Räume und der Name des Raumes lautet: " + Raum.name + " Die länge beträgt: " + str(Raum.laenge) + "m und die Breite beträgt: " + str(Raum.breite) + " Die Raumgröße ist: " {Raum.raumgroesse})
# print("Dein Gebäude hat " + raeume + " Rä)

if __name__ == '__main__':
    raeume = int(input("Hey Makler, Gebe die Anzahl an Räumen an welches das Gebäude hat: "))
    alle_raeume = raum_abfrage(raeume)
    raum_ausgeben(alle_raeume, raeume)
