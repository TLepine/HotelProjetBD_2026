import unittest
from metier.chambreMetier import creerTypeChambre,TypeChambreDTO
from modele.chambre import TypeChambre
import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
class test_creerTypeChambre(unittest.TestCase):
    def test_creerNouveauTypeChambre(self):
        typeChambreDTO=TypeChambreDTO(
                    TypeChambre(
                        nom_type="penthouse",
                        prix_plafond=1000.0,
                        prix_plancher=700.0
                    )                       
                )
        typeChambreCree= creerTypeChambre(typeChambreDTO)
        assert typeChambreCree.nom_type== "penthouse"
        assert typeChambreCree.prix_plafond==1000.0
        assert typeChambreCree.prix_plancher==700.0