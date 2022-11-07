import unittest
from statistics import Statistics
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_pelaajat_ovat_oikein(self):
        players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
        for index, player in enumerate(self.statistics._players):
            self.assertEqual(str(player), str(players[index]))

    def test_pelaaja_loytyy_kun_nimi_on_oikein(self):
        player = self.statistics.search("Kurri")

        self.assertEqual(str(player), str(Player("Kurri", "EDM", 37, 53)))

    def test_pelaaja_loytyy_kun_nimi_tasmaa_osittain(self):
        player = self.statistics.search("Kur")

        self.assertEqual(str(player), str(Player("Kurri", "EDM", 37, 53)))

    def test_search_palauttaa_None_kun_pelaajaa_ei_ole(self):
        player = self.statistics.search("Aho")

        self.assertEqual(player, None)

    def test_team_palauttaa_oikeat_pelaajat_kun_tiimi_on_olemassa(self):
        players = self.statistics.team("EDM")

        correct_players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]

        for i in range(len(players)):
            self.assertEqual(str(players[i]), str(correct_players[i]))

    def test_team_palauttaa_tyhjan_listan_kun_tiimia_ei_ole(self):
        players = self.statistics.team("BUF")

        self.assertEqual(players, [])

    def test_top_palauttaa_parhaan_pelaajan_parametrilla_nolla(self):
        players = self.statistics.top(0)

        self.assertEqual(str(players[0]), str(Player("Gretzky", "EDM", 35, 89)))

    def test_top_palauttaa_kolme_parasta_pelaajaa_parametrilla_kaksi(self):
        players = self.statistics.top(2)

        best_players = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]

        for i in range(len(players)):
            self.assertEqual(str(players[i]), str(best_players[i]))

    def test_top_palauttaa_tyhjan_listan_negatiivisella_parametrilla(self):
        players = self.statistics.top(-5)

        self.assertEqual(players, [])

    def test_top_palauttaa_eniten_maaleja_tehneen_pelaajan(self):
        players = self.statistics.top(0, SortBy.GOALS)

        self.assertEqual(str(players[0]), str(Player("Lemieux", "PIT", 45, 54)))

    def test_top_palauttaa_eniten_syottoja_tehneen_pelaajan(self):
        players = self.statistics.top(0, SortBy.ASSISTS)

        self.assertEqual(str(players[0]), str(Player("Gretzky", "EDM", 35, 89)))

    def test_top_palauttaa_samat_arvot_ilman_toista_parametria(self):
        self.assertEqual(self.statistics.top(2, SortBy.POINTS), self.statistics.top(2))