import unittest
from model import Chambre, TypeChambre
from metier.chambreMetier import creerChambre, ChambreDTO

class test_crerrChambre(unittest.TestCase):
    def test_creerChambre(self):
        chambreDTO = ChambreDTO(
                Chambre(
                        numero_chambre = 501,
                        disponible_reservation = True,
                        type_chambre = 
                            TypeChambre(
                                    nom_type = 'simple',
                                    prix_plancher = 59.0
                            )
                )
        )
        chambreDTOCree = creerChambre(chambreDTO)
        self.assertEqual(chambreDTOCree.numero_chambre, 501)