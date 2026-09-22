import unittest
from sqlalchemy import create_engine,select,insert
from sqlalchemy.orm import Session
from modele.chambre import Usager
import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
engine= create_engine('mssql+pyodbc://CL5-WIN11-KOMAR\\SQLEXPRESS01/Hotel?driver=ODBC+Driver+17+for+SQL+Server',use_setinputsizes=False)
class test_usager(unittest.TestCase):
    def test_getUsagerParNom(self):
        with Session(engine) as session:
                    stmt= select(Usager).where(Usager.prenom=='Clara')
                    usager=session.execute(stmt).scalar_one()
                    self.assertEqual(usager.prenom,'Clara')
                    self.assertEqual(usager.nom,'Bottom')
                    self.assertEqual(usager.adresse,'600 Pennsylvania Avenue NW in Washington, D.C')
                    self.assertEqual(usager.mobile,'111-222-3335')
                    self.assertEqual(usager.mot_de_passe,'abcd123')
                    self.assertEqual(usager.id_usager,'B40E5226-A10B-4B94-9312-7771A938B88D')