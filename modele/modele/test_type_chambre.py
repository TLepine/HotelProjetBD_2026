import unittest

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

from model import  TypeChambre


import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
#engine = create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=SQL Server', use_setinputsizes=False)
class test_type_chambre(unittest.TestCase):
    def test_getTypeChambrePartNumero(self):
        with Session(engine) as session:
            stmt = select(TypeChambre).where(TypeChambre.id_type_chambre =='1D97FBBB-53C7-4284-919C-0DD84095B512')
            tchambre = session.execute(stmt).scalar_one()
            self.assertEqual(tchambre.id_type_chambre, '1D97FBBB-53C7-4284-919C-0DD84095B512')
            self.assertEqual(tchambre.nom_type, 'simple')
            self.assertEqual(tchambre.prix_plancher, 59.0)
            self.assertEqual(tchambre.prix_plafond, 99.0)
            self.assertEqual(tchambre.description_chambre, 'Chambre avec lit simple')