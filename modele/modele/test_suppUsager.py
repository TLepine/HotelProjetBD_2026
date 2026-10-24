import unittest
from model import Usager
from metier.chambreMetier import supprimerUsager, UsagerDTO

class test_creerUsager(unittest.TestCase):
    def test_suppUsager(self):
        
        SuppUsager = supprimerUsager("0A3352CC-77BF-47F5-8FB2-60AB681ED745")
        self.assertIsNone(SuppUsager)