import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_hae_pelaajat(self):
        self.assertAlmostEqual(len(PlayerReaderStub.get_players(self)), 5)

    def test_hae_pelaajan_nimellä(self):
        pelaaja = self.stats.search("Semenko")

        self.assertEqual(str(pelaaja), "Semenko EDM 4 + 12 = 16")

    def test_hae_väärän_pelaajan_nimellä(self):
        pelaaja = self.stats.search("Henni")

        self.assertEqual(str(pelaaja), "None")
    
    def test_hae_luku_tiimin_pelaajista(self):
        players = self.stats.team("DET")
    
        self.assertEqual(len(players), 1)
    
    def test_top_funktio(self):
        players = self.stats.top(2)

        self.assertEqual(len(players)-1, 2)

        

