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
            Raum.name = str(input("\nWie ist der Name deines Raumes? "))
            Raum.laenge = int(input("Gebe die Länge deines Raumes (in Metern) an: "))
            Raum.breite = int(input("Gebe die Breite deines Raumes (in Metern) an: "))
            Raum.groesse = Raum.laenge * Raum.breite

            alle_raeume.append(Raum)
        except ValueError:
            print("Die Eingabe ist Falsch, bitte erneut eingeben.")

    return alle_raeume


def raum_ausgeben(raeume, num):
    print(f"Dein Gebäude hat {num}")

    for i in range(num):
        print(f"""\n
        Der Name des Raumes lautet: {raeume[i].name}
        Die länge beträgt: {raeume[i].laenge}
        und die Breite beträgt: {raeume[i].breite}.
        Die Raumgröße ist: {raeume[i].groesse}
        """)

# print("Dein Gebäude hat " + raeume + " Rä)

if __name__ == '__main__':
    raeume = int(input("Hey Makler, Gebe die Anzahl an Räumen an welches das Gebäude hat: "))
    alle_raeume = raum_abfrage(raeume)
    print(alle_raeume[0].name)
    raum_ausgeben(alle_raeume, raeume)
