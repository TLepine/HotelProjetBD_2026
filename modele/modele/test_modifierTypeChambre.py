import unittest
from metier.chambreMetier import modifierTypeChambre,TypeChambreDTO
from model import Chambre,TypeChambre
from sqlalchemy import create_engine,update,select
import logging
from sqlalchemy.orm import Session
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
class test_modifierTypeChambre(unittest.TestCase):
    def test_modifierTypeChambre(self):
        with Session(engine) as session:
                type_chambre_existe=session.execute(select(TypeChambre)).scalars().first()
                self.assertIsNotNone(type_chambre_existe)
                

                typechambreAModif=TypeChambreDTO(
                     TypeChambre(
                        id_type_chambre="15854D43-4688-4226-A330-D36184B0F78E",
                        nom_type="triple",
                        prix_plancher=333.3,
                        prix_plafond=444.4,
                        description_chambre="Chambre triple, avant triuple v2"
                    
                         )
                )
                type_chambre_modif=modifierTypeChambre(typechambreAModif)
                self.assertEqual(type_chambre_modif.nom_type,"triple")
                self.assertEqual(type_chambre_modif.prix_plancher, 333.3)
                self.assertEqual(type_chambre_modif.prix_plafond, 444.4)  