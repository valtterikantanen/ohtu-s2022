from tuomari import Tuomari


class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto()

        self._tulosta_tietokoneen_siirto(tokan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()

            self._tulosta_tietokoneen_siirto(tokan_siirto)
            self._aseta_tekoalyn_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)
    
    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]

    def _tulosta_tietokoneen_siirto(self, tietokoneen_siirto):
        print(f"Tietokone valitsi: {tietokoneen_siirto}")

    def _aseta_tekoalyn_siirto(self, tekoaly, ekan_siirto):
        pass
