import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
import random

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_henkilolla(self):
        viitenumero = random.randint(1,99)

        self.viitegeneraattori_mock.uusi.return_value = viitenumero

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value ,"12345", "33333-44455", 5)
    
    def test_ostetaan_kaksi_eri_tuotetta(self):

        viitenumero = random.randint(1,99)

        self.viitegeneraattori_mock.uusi.return_value = viitenumero

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "kahvi", 12)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value  ,"12345", "33333-44455", 17)
    
    def test_ostetaan_kaksi_samaa_tuotetta(self):

        viitenumero = random.randint(1,99)

        self.viitegeneraattori_mock.uusi.return_value = viitenumero

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "kahvi", 12)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value ,"12345", "33333-44455", 10)

    def test_ostetaan_kaksi_samaa_tuotetta_ja_varastossa_ei_tarpeeksi(self):
        
        viitenumero = random.randint(1,99)

        self.viitegeneraattori_mock.uusi.return_value = viitenumero


        def hae_uusi_saldo(tuote_id, vähennetty_määrä):
            if tuote_id == 1:
                return 10 - vähennetty_määrä

            elif tuote_id == 2:
                return 1 - vähennetty_määrä

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return hae_uusi_saldo(tuote_id,0)
            
            elif tuote_id == 2:
                return hae_uusi_saldo(tuote_id,0)

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                hae_uusi_saldo(tuote_id, 1)
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                hae_uusi_saldo(tuote_id, 1)
                return Tuote(2, "kahvi", 12)
            

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()

        for _ in range(1):
            if varasto_saldo(2) > 0:
                kauppa.lisaa_koriin(2)

        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi.return_value ,"12345", "33333-44455", 12)
    
    