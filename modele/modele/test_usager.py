import unittest
from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session
from model import Usager
import logging



logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
class test_usager(unittest.TestCase):
    def test_getUsagerParNom(self):
        with Session(engine) as session:
                    stmt= select(Usager).where(Usager.prenom=='steve')
                    usager=session.execute(stmt).scalar_one()
                    self.assertEqual(usager.prenom,'steve')
                    self.assertEqual(usager.nom,'rejean')
                    self.assertEqual(usager.adresse,'111 rue nord')
                    self.assertEqual(usager.mobile,'12345')
                    self.assertEqual(usager.mot_de_passe,'abcd')
                    self.assertEqual(usager.id_usager,'0993F8D0-FA9D-4F31-BD2C-DB23B519F966')