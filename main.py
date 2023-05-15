import datetime
class Auto:

    def __init__(self, marka, modelis, gads, cena):
        self.marka = marka
        self.modelis = modelis
        self.gads = gads
        self.cena = cena

    def informacija(self):
        print(f"Marka: {self.marka}\n"
              f"Modelis: {self.modelis}"
              f"Gads: {self.gads}")

    def vecums(self):
        now = datetime.datetime.now()
        if self.gads > now.year:
            print("Nakotnē")
        else:
            print(now.year - self.gads)
        return now.year - self.gads

    def vertiba(self):
        if self.vecums():
            cenas_zaudesana = self.cena * (0.05 * self.vecums())
            print(self.cena - cenas_zaudesana)
        else:
            print(100)
