class Raum:

    def __init__(self, name):
        """Initialisiert einen Raum-Objekt."""
        self.name = name
        self.raeume = []
        self.teilraeume = []
        self.groesse = 0

    def add_raum(self, laenge, breite):
        """Fügt dem Gebäude einen Raum mit gegebenen Maßen hinzu und aktualisiert die Gesamtgröße."""
        self.raeume.append((laenge, breite))
        self.groesse += laenge * breite

    def add_teilraum(self, laenge, breite):
        """Fügt ggfs dem Raum einen Teilraum mit gegebenen Maßen hinzu und aktualisiert die Gesamtgröße."""
        self.teilraeume.append((laenge, breite))
        self.groesse += laenge * breite


def raum_abfrage(num):
    """Fragt den Benutzer nach Details für eine gegebene Anzahl von Räumen und erstellt diese."""
    alle_raeume = []
    aktueller_raum = 1
    for i in range(num):
        try:
            name = input(f"\nWie ist der Name des {aktueller_raum}. Raumes? ")
            aktueller_raum += 1
            raum = Raum(name)
            teilraum_abfrage = input("Hat dieser Raum Teilräume (Ja/Nein)\n")
            if teilraum_abfrage.lower() == "ja":
                teilraeume_num = int(input(f"Wie viele Teilräume hat der Raum '{name}'? "))
                for _ in range(teilraeume_num):
                    laenge = float(input("Gebe die Länge eines Teilraums (in Metern) an: "))
                    breite = float(input("Gebe die Breite eines Teilraums (in Metern) an: "))
                    raum.add_teilraum(laenge, breite)
            else:
                laenge = float(input("Gebe die Länge des Raumes (in Metern) an: "))
                breite = float(input("Gebe die Breite des Raumes (in Metern) an: "))
                raum.add_raum(laenge, breite)

            alle_raeume.append(raum)
        except ValueError:
            print("Die Eingabe ist falsch, bitte erneut eingeben.")

    return alle_raeume


def raum_ausgeben(alle_raeume):
    """Gibt Informationen über alle Räume und die Gesamtfläche aus."""
    gesamtflaeche = sum(raum.groesse for raum in alle_raeume)
    print(f"Dein Gebäude hat insgesamt {len(alle_raeume)} Räume und eine Gesamtfläche von {gesamtflaeche}m².")

    for raum in alle_raeume:
        print(f"""
        Raum: {raum.name}
        Anzahl der Teilräume: {len(raum.teilraeume)}
        Gesamtfläche: {raum.groesse}m²
        """)


if __name__ == '__main__':
    raeume = int(input("Wie viele Räume hat das Gebäude?: "))
    alle_raeume = raum_abfrage(raeume)
    raum_ausgeben(alle_raeume)
