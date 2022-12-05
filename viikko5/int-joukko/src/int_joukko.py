class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = 5 if not isinstance(kapasiteetti, int) or kapasiteetti < 0 else kapasiteetti
        self.kasvatuskoko = 5 if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0 else kasvatuskoko
        self.luvut = [None] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.luvut

    def lisaa(self, n):
        if self.kuuluu(n): return False

        self.luvut[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        self.luvut = self.luvut + [None] * self.kasvatuskoko if self.alkioiden_lkm == len(self.luvut) else self.luvut
        return True

    def poista(self, n):
        if not self.kuuluu(n): return False

        self.luvut.remove(n)
        self.luvut.append(None)
        self.alkioiden_lkm -= 1
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [luku for luku in self.luvut if luku is not None]

    def _muodosta_luvuista_joukko(self, luvut):
        for luku in luvut:
            self.lisaa(luku)

    @staticmethod
    def yhdiste(joukko1, joukko2):
        yhdiste = IntJoukko()
        yhdiste._muodosta_luvuista_joukko(joukko1.to_int_list() + joukko2.to_int_list())
        return yhdiste

    @staticmethod
    def leikkaus(joukko1, joukko2):
        leikkaus = IntJoukko()

        for luku in joukko1.to_int_list():
            if joukko2.kuuluu(luku):
                leikkaus.lisaa(luku)

        return leikkaus

    @staticmethod
    def erotus(joukko1, joukko2):
        erotus = IntJoukko()
        erotus._muodosta_luvuista_joukko(joukko1.to_int_list())

        for luku in joukko2.to_int_list():
            erotus.poista(luku)

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"

        mjono = "{"
        for luku in list(filter(lambda alkio : alkio is not None, self.luvut)):
            mjono += f"{luku}, "
        return mjono[:-2] + "}"
