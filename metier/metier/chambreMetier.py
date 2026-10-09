from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.exc import SQLAlchemyError
from DTO.chambreDTO import ChambreDTO, TypeChambreDTO
from model import Chambre, TypeChambre
import uuid


engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)



def creerChambre(chambre: ChambreDTO):
    
    with Session(engine) as session:

        stmt_num = select(Chambre).where(Chambre.numero_chambre == chambre.numero_chambre)
        if session.execute(stmt_num).scalars().first() is not None:
            raise ValueError( f"le numéro de la chambre {chambre.numero_chambre} est dans la BD.")
        
        stmt = select (TypeChambre).where(TypeChambre.nom_type == chambre.type_chambre.nom_type)
        result=session.execute(stmt)

       

        for typeChambre in result.scalars():
            nouvelleChambre = Chambre (
                numero_chambre=chambre.numero_chambre,
                disponible_reservation=chambre.disponible_reservation,
                autre_informations = chambre.autre_informations,
                id_chambre = uuid.uuid4(),
                type_chambre = typeChambre
            )
            session.add(nouvelleChambre)
            session.commit()

        return chambre



    
def creerTypeChambre (typeChambre: TypeChambreDTO):

    with Session(engine) as session:
        nouveauTypeChambre = TypeChambre(
            nom_type = typeChambre.nom_type,
            prix_plancher = typeChambre.prix_plancher
        )
        session.add(nouveauTypeChambre)
        session.commit()
        return typeChambre

#TODO: Ajouter des validations au besoin. Ex no_chambre ne doit pas être null. 
    #TODO: Ajouter gestion des erreurs. On va voir un exemple au prochain cours

def getChambreParNumero(no_chambre: int):

    if no_chambre <0:
       raise ValueError("Pas de nombre négatif pour le numéro de chambre")
    if no_chambre >999:
           raise ValueError("Pas de nombre au dessus de 999 pour le numéro de chambre")


    try: 
        with Session(engine) as session:

            stmt_num = select(Chambre).where(Chambre.numero_chambre == no_chambre)
            if session.execute(stmt_num).scalars().first() is None:
                raise ValueError( "Aucune chambre avec ce numéro")
            
            stmt = select(Chambre).where(Chambre.numero_chambre == no_chambre)
            result = session.execute(stmt)

            for chambre in result.scalars():
                return ChambreDTO(chambre)
    except SQLAlchemyError as e:
        raise ValueError(f"Une erreur est survenue avec la BD : {e}")
        


def modifierChambre(chambre: ChambreDTO):
    #voir si  ca existe deja
    #gestion des erreurs
    with Session(engine) as session:

        stmt_num = select(Chambre).where(Chambre.numero_chambre == chambre.numero_chambre)
        if session.execute(stmt_num).scalars().first() is None:
             raise ValueError( f"La chambre n'existe pas")


        stmt = select(Chambre).where(Chambre.id_chambre == chambre.idChambre)
        chambreAModifier= session.execute(stmt).scalars().one()
        

        chambreAModifier.disponible_reservation = chambre.disponible_reservation
        chambreAModifier.autre_informations = chambre.autre_informations
        chambreAModifier.numero_chambre = chambre.numero_chambre
        #setter les autres champs
        session.commit()
        