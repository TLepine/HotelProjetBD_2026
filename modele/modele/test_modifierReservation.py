import unittest
from metier.chambreMetier import modifierReservation,ChambreDTO, ReservationDTO
from model import Chambre,TypeChambre, Reservation, Usager
from sqlalchemy import create_engine,update,select
import logging
from sqlalchemy.orm import Session
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
class test_modifierChambre(unittest.TestCase):
    def test_modifierUneChambre(self):
        with Session(engine) as session:
                reservation_existe=session.execute(select(Reservation)).scalars().first()
                self.assertIsNotNone(reservation_existe)
                
                chambreDTO=ChambreDTO(
                     (Chambre(id_chambre="23BE72DD-8C79-4007-84C2-026687DAB3AC",
                               numero_chambre=94,
                               disponible_reservation=True,
                                type_chambre=(TypeChambre(id_type_chambre="15854D43-4688-4226-A330-D36184B0F78E",
                                nom_type='triple',prix_plancher=333.3))
                                         )),
                )
                usagerDTO=(Usager(id_usager="00D685BF-CE7B-44C0-B204-D7483E6D50A5",
                                                                nom="Sainte-Marie",
                                                                prenom="Paul",
                                                                adresse="144 rue Julien",
                                                                mobile="111 111 1111",
                                                                mot_de_passe= "54321"    ))

                


                reservationAModif=ReservationDTO(
                     Reservation(
                        id_reservation="71119CE6-E7D5-449A-96E2-61CD0443AD00",
                        date_fin_reservation="28",
                        date_debut_reservation="10",
                        prix_jour= 100.0,
                        info_reservation="Test",          
                        chambre=chambreDTO,
                        usager=usagerDTO
                        )
                )
                reservation_modif=modifierReservation(reservationAModif)
                self.assertEqual(reservation_modif.date_fin_reservation,"28")
                self.assertEqual(reservation_modif.date_debut_reservation,"10")
                  