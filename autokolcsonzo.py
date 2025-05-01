import re
from datetime import datetime
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_felvetele(self, auto):
        self.autok.append(auto)

    def rendszam_ellenorzes(self, rendszam):
        minta = r"^[A-Z]{4}-\d{3}$"
        return bool(re.match(minta, rendszam))

    def foglalas(self, rendszam, datum):
        try:
            foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
            jelenlegi_datum = datetime.now()

            if foglalas_datum < jelenlegi_datum:
                return f"Hiba: Nem foglalható múltbéli dátum ({datum})."
        except ValueError:
            return f"Helytelen dátumformátum! Használja: ÉÉÉÉ-HH-NN."

        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                return f"A(z) {rendszam} rendszámú autó már foglalt ezen a napon: {datum}."

        for auto in self.autok:
            if auto.rendszam == rendszam:
                auto.foglalas(datum)
                self.berlesek.append(Berles(auto, datum))
                return f"A(z) {rendszam} rendszámú autó sikeresen lefoglalva erre a napra: {datum}."

        return f"Nincs ilyen autó a rendszerben: {rendszam}"

    def lemondas(self, rendszam, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                self.berlesek = [berles for berles in self.berlesek if not (berles.auto.rendszam == rendszam and berles.datum == datum)]
                return auto.lemondas(datum)
        return f"Nincs ilyen autó a rendszerben: {rendszam}"
