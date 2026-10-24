import unittest
from model import Usager
from metier.chambreMetier import creerUsager, UsagerDTO

class test_creerUsager(unittest.TestCase):
    def test_creerUsager(self):
        usagerDTO = UsagerDTO(
                Usager(
                        nom = "Ste-Marie2",
                        prenom = "Paul2",
                        adresse = "148 rue Albert",
                        mobile = "418-845-2424",
                        mot_de_passe = "12345",
                        
                )
        )
        usagerDTOCreer = creerUsager(usagerDTO)
        self.assertEqual(usagerDTOCreer.nom, "Ste-Marie2")