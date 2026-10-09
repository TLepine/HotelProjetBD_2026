import uuid

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.chambreDTO import ChambreDTO,TypeChambreDTO
from modele.chambre import Chambre, TypeChambre

engine= create_engine('mssql+pyodbc://CL5-WIN11-KOMAR\\SQLEXPRESS01/Hotel?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes',use_setinputsizes=False)
def creerChambre(chambre:ChambreDTO):
    #TODO ajouter des validations(lorsqu'on cree une chambre )

    with Session(engine) as session:
        stmt= select(TypeChambre).where(TypeChambre.nom_type==chambre.type_chambre.nom_type)
        result=session.execute(stmt)
        for typeChambre in result.scalars():
            nouvelleChambre = Chambre(
                numero_chambre =chambre.numero_chambre,
                disponible_reservation=chambre.disponible_reservation,
                autre_informations=chambre.autre_informations,
                id_chambre = uuid.uuid4(),
                type_chambre= typeChambre
            )
        session.add(nouvelleChambre)
        session.commit()
        return chambre
def getChambreParNumero(no_chambre: int):
    #TODO: Ajouter des validations(no_chambre ne doit pas etre null)
    with Session(engine) as session:
        stmt= select(Chambre).where(Chambre.numero_chambre== no_chambre)
        result = session.execute(stmt)  
        
        

def modifierChambre(chambre:ChambreDTO):
    with Session(engine)as session:
        stmt =select(Chambre).where(Chambre.id_chambre==chambre.id_chambre)
        
        chambreAModifier=session.execute(stmt).scalars().one()
        tychambre = session.execute(select(TypeChambre).where(TypeChambre.id_type_chambre
                == chambre.type_chambre.id_type_chambre)).scalar_one()
        if tychambre is None:
            raise ValueError(
                "Type de chambre introuvable : "
                f"{chambre.type_chambre.id_type_chambre}"
            )
        chambreAModifier.disponible_reservation=chambre.disponible_reservation
        chambreAModifier.autre_informations=chambre.autre_informations
        chambreAModifier.numero_chambre=chambre.numero_chambre
        chambreAModifier.type_chambre=tychambre
        session.commit()
        if chambreAModifier is None:
                    raise ValueError("Chambre introuvable")
        return chambre
def creerTypeChambre(typeChambre: TypeChambreDTO):
        with Session(engine) as session:
            stmt= select(TypeChambre).where(TypeChambre.id_type_chambre==typeChambre.id_type_chambre)
            result=session.execute(stmt)
            for idTypeChambre in result.scalars():
                    newTypeChambre= TypeChambre (
                        
                        nom_type = typeChambre.nom_type,
                        prix_plafond= typeChambre.prix_plafond,
                        prix_plancher= typeChambre.prix_plancher,
                        id_type_chambre= typeChambre.idTypeChambre,
                        description_chambre=typeChambre.description_chambre
                    )
                    session.add(newTypeChambre)
                    session.commit()       
            return typeChambre