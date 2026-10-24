import unittest
from model import Reservation
from metier.chambreMetier import supprimerReservation, ReservationDTO

class test_suppReservation(unittest.TestCase):
    def test_suppReservation(self):
        
        SuppReservation = supprimerReservation("59D55C2C-6FFA-4EDC-A50F-F3F0C7A1CEA6")
        self.assertIsNone(SuppReservation)