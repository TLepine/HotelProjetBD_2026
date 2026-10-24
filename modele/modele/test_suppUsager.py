import unittest
from model import Usager
from metier.chambreMetier import supprimerUsager, UsagerDTO

class test_creerUsager(unittest.TestCase):
    def test_suppUsager(self):
        
        SuppUsager = supprimerUsager("0993F8D0-FA9D-4F31-BD2C-DB23B519F966")
        self.assertIsNone(SuppUsager)