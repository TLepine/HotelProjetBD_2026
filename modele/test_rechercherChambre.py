import unittest
from model import Chambre, TypeChambre
from metier.chambreMetier import getChambrePartNumero, ChambreDTO

class test_rechercherChambre(unittest.TestCase):
    def test_rechercherChambre(self):
        
        chambreDTONum = getChambrePartNumero(301)
        self.assertEqual(chambreDTONum.numero_chambre, 301)