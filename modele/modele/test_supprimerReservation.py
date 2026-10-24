import unittest
from model import Reservation
from metier.chambreMetier import supprimerReservation, ReservationDTO

class test_suppReservation(unittest.TestCase):
    def test_suppReservation(self):
        
        SuppReservation = supprimerReservation("F5780E89-09B1-4385-97FF-1CBF4B2F4784")
        self.assertIsNone(SuppReservation)