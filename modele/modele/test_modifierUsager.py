import unittest
from metier.chambreMetier import modifierUsager,UsagerDTO
from model import Chambre,TypeChambre, Usager
from sqlalchemy import create_engine,update,select
import logging
from sqlalchemy.orm import Session
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
class test_modifierUsager(unittest.TestCase):
    def test_modifierUsager(self):
        with Session(engine) as session:
                usager_existe=session.execute(select(Usager)).scalars().first()
                self.assertIsNotNone(usager_existe)
                

                usagerAModif=UsagerDTO(
                     Usager(
                        id_usager="00D685BF-CE7B-44C0-B204-D7483E6D50A5",
                        nom="Sainte-Marie",
                        prenom="Paul",
                        adresse="144 rue Julien",
                        mobile="111 111 1111",
                        mot_de_passe= "54321"
                    
                         )
                )
                usager_modif=modifierUsager(usagerAModif)
                self.assertEqual(usager_modif.nom,"Sainte-Marie")
                self.assertEqual(usager_modif.prenom, "Paul")
                self.assertEqual(usager_modif.motDePasse, "54321")  