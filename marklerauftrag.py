class Raum:
    def __init__(self, laenge, breite, name, raumgroesse):
        self.name = name
        self.laenge = laenge
        self.breite = breite
        self.groesse = laenge * breite


def raum_abfrage(num):
    alle_raeume = []
    for i in range(num):
        try: 
            name = str(input("\nWie ist der Name deines Raumes? "))
            laenge = int(input("Gebe die Länge deines Raumes (in Metern) an: "))
            breite = int(input("Gebe die Breite deines Raumes (in Metern) an: "))
            groesse = laenge * breite

            raum = (name, laenge, breite, groesse)
            alle_raeume.append(raum)
        except ValueError:
            print("Die Eingabe ist Falsch, bitte erneut eingeben.")

    return alle_raeume


def raum_ausgeben(raeume, num):
    print(f"Dein Gebäude hat {num}")

    for i in range(num):
        raum = raeume[i]
        print(f"""\n
        Der Name des Raumes lautet: {raum[0]}
        Die länge beträgt: {raum[1]}
        und die Breite beträgt: {raum[2]}.
        Die Raumgröße ist: {raum[3]}
        """)

# print("Dein Gebäude hat " + raeume + " Rä)

if __name__ == '__main__':
    raeume = int(input("Hey Makler, Gebe die Anzahl an Räumen an welches das Gebäude hat: "))
    alle_raeume = raum_abfrage(raeume)
    raum_ausgeben(alle_raeume, raeume)
