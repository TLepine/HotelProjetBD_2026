import unittest
from model import Chambre
from metier.chambreMetier import supprimerChambre, ChambreDTO

class test_suppChambre(unittest.TestCase):
    def test_suppChambre(self):
        
        SuppChambre = supprimerChambre("CBE63E9D-DE76-4FDA-A326-E46E1120D200")
        self.assertIsNone(SuppChambre)