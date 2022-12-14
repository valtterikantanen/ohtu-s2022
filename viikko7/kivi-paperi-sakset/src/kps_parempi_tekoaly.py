from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self):
        return self.tekoaly.anna_siirto()

    def _aseta_tekoalyn_siirto(self, ekan_siirto):
        self.tekoaly.aseta_siirto(ekan_siirto)
