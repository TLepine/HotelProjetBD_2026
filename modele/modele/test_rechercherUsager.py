import unittest
from model import Chambre, TypeChambre, Usager
from metier.chambreMetier import rechercherUsager, UsagerDTO

class test_rechercherUsager(unittest.TestCase):
    def test_rechercherUsager(self):
        
        UsagerDTONom = rechercherUsager("Simard")
        self.assertEqual(UsagerDTONom.nom, "Simard")