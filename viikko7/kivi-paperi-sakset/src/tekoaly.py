class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        self._siirto += 1
        self._siirto %= 3

        siirrot = {0: "k", 1: "p", 2: "s"}

        return siirrot[self._siirto]
