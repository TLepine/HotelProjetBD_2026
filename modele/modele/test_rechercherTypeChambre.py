import unittest
from model import Chambre, TypeChambre
from metier.chambreMetier import rechercherTypeChambre, ChambreDTO

class test_rechercherTypeChambre(unittest.TestCase):
    def test_rechercherChambre(self):
        
        TypechambreDTONom = rechercherTypeChambre("triple")
        self.assertEqual(TypechambreDTONom.nom_type, "triple")