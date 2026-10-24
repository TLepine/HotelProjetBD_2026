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
                    stmt= select(Usager).where(Usager.prenom=='Paul')
                    usager=session.execute(stmt).scalar_one()
                    self.assertEqual(usager.prenom,'Paul')
                    self.assertEqual(usager.nom,'Sainte-Marie')
                    self.assertEqual(usager.adresse,'144 rue Julien')
                    self.assertEqual(usager.mobile,'111 111 1111')
                    self.assertEqual(usager.mot_de_passe,'54321')
                    self.assertEqual(usager.id_usager,'00D685BF-CE7B-44C0-B204-D7483E6D50A5')