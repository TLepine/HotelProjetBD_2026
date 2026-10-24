import unittest
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

from model import Reservation, Chambre, Usager


import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)

class test_reservation(unittest.TestCase):
    def test_getReservationPartNumero(self):
        with Session(engine) as session:
            stmt = select(Reservation).where(Reservation.id_reservation =='B9BB357B-C7B6-4AAD-9B84-B600606F1064')
            reservation = session.execute(stmt).scalar_one()
            self.assertEqual(reservation.id_reservation, 'B9BB357B-C7B6-4AAD-9B84-B600606F1064')
            self.assertEqual(reservation.prix_jour, 40.5)
            self.assertEqual(reservation.info_reservation, 'Fete anniversaire')
            self.assertEqual(reservation.date_fin_reservation, "22 octobre")
            self.assertEqual(reservation.date_debut_reservation, "12 octobre")
            self.assertEqual(reservation.usager.id_usager, '00D685BF-CE7B-44C0-B204-D7483E6D50A5')
            self.assertEqual(reservation.chambre.id_chambre, '78CAEDED-334E-4AB4-AC78-00CEAFFFF0EC')
            