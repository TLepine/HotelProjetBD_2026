import unittest
from metier.chambreMetier import creerTypeChambre,TypeChambreDTO
from model import TypeChambre


class test_creerTypeChambre(unittest.TestCase):
    def test_creerNouveauTypeChambre(self):
        typeChambreDTO=TypeChambreDTO(
                    TypeChambre(
                        nom_type="penthouse2",
                        prix_plafond=1000.0,
                        prix_plancher=700.0,
                        description_chambre= "test"
                    )                       
                )
        typeChambreCree= creerTypeChambre(typeChambreDTO)
        self.assertEqual(typeChambreCree.nom_type, "penthouse2")
        self.assertEqual(typeChambreCree.prix_plafond,1000.0)
        self.assertEqual(typeChambreCree.prix_plancher,700.0)