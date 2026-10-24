import unittest
from model import Chambre
from metier.chambreMetier import supprimerChambre, ChambreDTO

class test_suppChambre(unittest.TestCase):
    def test_suppChambre(self):
        
        SuppChambre = supprimerChambre("9D8D72EF-9132-4C97-A6A7-3CE5AA95D8DE")
        self.assertIsNone(SuppChambre)