from auto import Auto

class Teherauto(Auto):
    def foglalas(self, datum):
        if datum not in self.foglalt_napok:
            self.foglalt_napok.append(datum)
            return f"{self.rendszam} rendszámú teherautó sikeresen lefoglalva {datum}-ra."
        return f"{self.rendszam} rendszámú teherautó már foglalt {datum}-ra."

    def lemondas(self, datum):
        if datum in self.foglalt_napok:
            self.foglalt_napok.remove(datum)
            return f"{self.rendszam} rendszámú teherautó foglalása lemondva {datum}-ra."
        return f"{self.rendszam} rendszámú teherautó ezen a napon nem volt foglalva."
