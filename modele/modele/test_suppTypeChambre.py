import unittest
from model import TypeChambre
from metier.chambreMetier import supprimerTypeChambre, TypeChambreDTO

class test_creerUsager(unittest.TestCase):
    def test_suppTypeUsager(self):
        
        SuppTypeChambre = supprimerTypeChambre("1D97FBBB-53C7-4284-919C-0DD84095B513")
        self.assertIsNone(SuppTypeChambre)