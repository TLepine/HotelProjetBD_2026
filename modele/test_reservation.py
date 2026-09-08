import unittest
from datetime import datetime, date, time

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

from model import Reservation, Chambre, Usager


import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
#engine = create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=SQL Server', use_setinputsizes=False)
class test_reservation(unittest.TestCase):
    def test_getReservationPartNumero(self):
        with Session(engine) as session:
            stmt = select(Reservation).where(Reservation.id_reservation =='59D55C2C-6FFA-4EDC-A50F-F3F0C7A1CEA6')
            reservation = session.execute(stmt).scalar_one()
            self.assertEqual(reservation.id_reservation, '59D55C2C-6FFA-4EDC-A50F-F3F0C7A1CEA6')
            self.assertEqual(reservation.prix_jour, 40.0)
            self.assertEqual(reservation.info_reservation, 'no info')
            self.assertEqual(reservation.date_fin_reservation, datetime(2026, 2, 2, 0, 0, 0))
            self.assertEqual(reservation.date_debut_reservation, datetime(2026, 2, 1, 0, 0, 0))
            self.assertEqual(reservation.usager.id_usager, '0A3352CC-77BF-47F5-8FB2-60AB681ED745')
            self.assertEqual(reservation.chambre.id_chambre, 'BEE896DE-B3F5-4988-85A1-002733C3CEB5')
            