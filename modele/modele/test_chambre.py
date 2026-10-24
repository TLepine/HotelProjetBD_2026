import unittest

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

from model import Chambre, TypeChambre


import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
#engine = create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=SQL Server', use_setinputsizes=False)
class test_chambre(unittest.TestCase):
    def test_getChambrePartNumero(self):
        with Session(engine) as session:
            stmt = select(Chambre).where(Chambre.numero_chambre ==136)
            chambre = session.execute(stmt).scalar_one()
            self.assertEqual(chambre.numero_chambre, 136)
            self.assertIsNone(chambre.autre_informations)
            self.assertTrue(chambre.disponible_reservation)
            self.assertEqual(chambre.id_chambre, 'F6BEBF8A-2AC6-4810-8CAF-008FAA63E238')
            self.assertEqual(chambre.type_chambre.nom_type, 'simple')
            self.assertEqual(chambre.type_chambre.prix_plancher, 59.0)
            self.assertEqual(chambre.type_chambre.prix_plafond, 99.0)
            self.assertEqual(chambre.type_chambre.description_chambre, 'Chambre avec lit simple')
            self.assertIsNotNone(chambre.type_chambre)
            self.assertEqual(chambre.type_chambre.id_type_chambre, '1D97FBBB-53C7-4284-919C-0DD84095B512')



          
        
          
           
