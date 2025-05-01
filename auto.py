from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.foglalt_napok = []

    @abstractmethod
    def foglalas(self, datum):
        pass

    @abstractmethod
    def lemondas(self, datum):
        pass