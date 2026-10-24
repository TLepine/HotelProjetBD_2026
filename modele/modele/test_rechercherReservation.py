import unittest
from model import Chambre, TypeChambre, Usager, Reservation
from metier.chambreMetier import rechercherReservation, ReservationDTO
import uuid

class test_rechercherReservation(unittest.TestCase):
    def test_rechercherReservation(self):
        
        ReservationDTOid = rechercherReservation("71119CE6-E7D5-449A-96E2-61CD0443AD00")
        self.assertEqual(ReservationDTOid.id_reservation, uuid.UUID("71119CE6-E7D5-449A-96E2-61CD0443AD00"))