from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
import uuid
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from DTO.chambreDTO import ChambreDTO, TypeChambreDTO
from model import Chambre, TypeChambre

engine =create_engine('mssql+pyodbc://localhost\\MSSQLSERVER2/Hotel?driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)

#TODO: Générer un uuid et l'assigner à la chambre, si vous n'utilisez pas un auto-increment.
    #TODO: Ajouter des validations au besoin. Ex: Lorsque l'on créé une chambre, s'il n'y a pas de numéro de chambre # ou si le numéro de chambre existe déjà, on Raise un ValueError.
    #TODO: Ajouter gestion des erreurs. On va voir un exemple au prochain cours.

def creerChambre(chambre: ChambreDTO):
    
    with Session(engine) as session:
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
#TODO: Générer un uuid et l'assigner à la chambre, si vous n'utilisez pas un auto-increment. #TODO: Ajouter des validations au besoin.
#TODO: Ajouter gestion des erreurs. On va voir un exemple au prochain cours.
    with Session(engine) as session:
        nouveauTypeChambre = TypeChambre(
            nom_type = typeChambre.nom_type,
            prix_plancher = typeChambre.prix_plancher
        )
        session.add(nouveauTypeChambre)
        session.commit()
        return typeChambre

def getChambreParNumero(no_chambre: int):
    with Session(engine) as session:
        stmt = select(Chambre).where(Chambre.numero_chambre == no_chambre)
        result = session.execute(stmt)

        for chambre in result.scalars():
            return Chambre(chambre)
        
#TODO: Ajouter des validations au besoin. Ex no_chambre ne doit pas être null. 
#TODO: Ajouter gestion des erreurs. On va voir un exemple au prochain cours

def modifierChambre(chambre: ChambreDTO):
    with Session(engine) as session:
        stmt = select(Chambre).where(Chambre.id_chambre == chambre.idChambre)
        chambreAModifier= session.execute(stmt).scalars().one()
        chambreAModifier = session.execute(stmt).scalars().one()

        chambreAModifier.disponible_reservation = chambre.disponible_reservation
        chambreAModifier.autre_informations = chambre.autre_informations
        chambreAModifier.numero_chambre = chambre.numero_chambre

        session.commit()
        return chambre