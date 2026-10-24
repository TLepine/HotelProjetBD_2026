import unittest
from model import Chambre, TypeChambre, Reservation, Usager
from metier.chambreMetier import creerReservation, ReservationDTO

class test_crerrReservation(unittest.TestCase):
    def test_creerReservation(self):
        reservationDTO = ReservationDTO(
                Reservation(
                        date_fin_reservation = "30 octobre",
                        date_debut_reservation = "12 octobre",
                        prix_jour = 40.5,
                        info_reservation= "test suppression2",
                        chambre =  Chambre( numero_chambre = 185, type_chambre=TypeChambre(id_type_chambre="1D97FBBB-53C7-4284-919C-0DD84095B512", nom_type="simple")),    
                        usager =  Usager(id_usager= "00D685BF-CE7B-44C0-B204-D7483E6D50A5", nom="Sainte-Marie", prenom="Paul", adresse= "144 rue Julien" ))
        )
        reservationDTOCree = creerReservation(reservationDTO)
        self.assertEqual(reservationDTOCree.date_fin_reservation, '30 octobre')