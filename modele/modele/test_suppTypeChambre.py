import unittest
from model import TypeChambre
from metier.chambreMetier import supprimerTypeChambre, TypeChambreDTO

class test_creerUsager(unittest.TestCase):
    def test_suppTypeUsager(self):
        
        SuppTypeChambre = supprimerTypeChambre("CBE63E9D-DE76-4FDA-A326-E46E1120D200")
        self.assertIsNone(SuppTypeChambre)