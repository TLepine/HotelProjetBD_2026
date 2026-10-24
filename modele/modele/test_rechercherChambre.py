import unittest
from model import Chambre, TypeChambre
from metier.chambreMetier import getChambreParNumero, ChambreDTO

class test_rechercherChambre(unittest.TestCase):
    def test_rechercherChambre(self):
        
        chambreDTONum = getChambreParNumero(300)
        self.assertEqual(chambreDTONum.numero_chambre, 300)