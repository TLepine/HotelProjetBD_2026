import unittest
from metier.chambreMetier import modifierChambre,ChambreDTO
from modele.chambre import Chambre,TypeChambre
from sqlalchemy import create_engine,update,select
import logging
from sqlalchemy.orm import Session
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
engine= create_engine('mssql+pyodbc://CL5-WIN11-KOMAR\\SQLEXPRESS01/Hotel?driver=ODBC+Driver+17+for+SQL+Server',use_setinputsizes=False)
class test_modifierChambre(unittest.TestCase):
    def test_modifierUneChambre(self):
        with Session(engine) as session:
                chambre_existe=session.execute(select(Chambre)).scalars().first()
                self.assertIsNotNone(chambre_existe)
                id_chambre=chambre_existe.id_chambre
                id_type_chambre = (chambre_existe.type_chambre.id_type_chambre)

                chambreAModif=ChambreDTO(
                     Chambre(
                        id_chambre=id_chambre,
                        numero_chambre=501,
                        disponible_reservation=False,
                        autre_informations= "Chambre nouvelle modifiée",
                        type_chambre=(TypeChambre(id_type_chambre=id_type_chambre, nom_type='double',prix_plancher=80.0))
                            )
                )
                chambre_modif=modifierChambre(chambreAModif)
                self.assertEqual(chambre_modif.numero_chambre,501)
                self.assertEqual(chambre_modif.disponible_reservation,False)
                self.assertEqual(chambre_modif.autre_informations,"Chambre nouvelle modifiée")              

     