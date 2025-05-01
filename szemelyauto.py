from auto import Auto

class Szemelyauto(Auto):
    def foglalas(self, datum):
        if datum not in self.foglalt_napok:
            self.foglalt_napok.append(datum)
            return f"{self.rendszam} rendszámú autó sikeresen lefoglalva {datum}-ra."
        return f"{self.rendszam} rendszámú autó már foglalt {datum}-ra."

    def lemondas(self, datum):
        if datum in self.foglalt_napok:
            self.foglalt_napok.remove(datum)
            return f"{self.rendszam} rendszámú autó foglalása lemondva {datum}-ra."
        return f"{self.rendszam} rendszámú autó ezen a napon nem volt foglalva."
