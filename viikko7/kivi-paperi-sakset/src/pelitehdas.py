from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Pelitehdas:
    @staticmethod
    def luo(peli):
        vaihtoehdot = {"a": KPSPelaajaVsPelaaja, "b": KPSTekoaly, "c": KPSParempiTekoaly}
        return vaihtoehdot[peli]()
