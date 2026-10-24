from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.exc import SQLAlchemyError
from DTO.chambreDTO import ChambreDTO, TypeChambreDTO, UsagerDTO, ReservationDTO
from model import Chambre, TypeChambre, Usager, Reservation
import uuid
from pydantic import  model_validator

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
    
def creerReservation(reservation: ReservationDTO):
    
    with Session(engine) as session:

        stmt_num = select(Reservation).where(Reservation.id_reservation == reservation.id_reservation)
        if session.execute(stmt_num).scalars().first() is not None:
            raise ValueError( f"l'id' de la reservation {reservation.id_reservation} est dans la BD.")
        
        stmt = select (Chambre).where(Chambre.numero_chambre == reservation.chambre.numero_chambre)
        result=session.execute(stmt).scalars().first()

        stmtUsager = select (Usager).where(Usager.id_usager == reservation.usager.idUsager)
        resultUsager=session.execute(stmtUsager).scalars().first()

       
        nouvelleReservation = Reservation (
            date_fin_reservation=reservation.date_fin_reservation,
            date_debut_reservation=reservation.date_debut_reservation,
            prix_jour = reservation.prix_jour,
            info_reservation= reservation.info_reservation,
            id_reservation = uuid.uuid4(),
            chambre = result,
            usager = resultUsager
            )
        
        session.add(nouvelleReservation)
        session.commit()

        return reservation



    
def creerTypeChambre(typeChambre: TypeChambreDTO):
        with Session(engine) as session:    
            newTypeChambre= TypeChambre (   
                            nom_type = typeChambre.nom_type,
                            prix_plafond= typeChambre.prix_plafond,
                            prix_plancher= typeChambre.prix_plancher,
                            id_type_chambre= uuid.uuid4(),
                            description_chambre=typeChambre.description_chambre
                        )
        session.add(newTypeChambre)
        session.commit()       
        return typeChambre


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
        

def rechercherTypeChambre(nom_type: str):
    
    try: 
            with Session(engine) as session:
    
                stmttype = select(TypeChambre).where(TypeChambre.nom_type == nom_type)
                if session.execute(stmttype).scalars().first() is None:
                    raise ValueError( "Aucun type de chambre avec ce nom")
                
                stmt = select(TypeChambre).where(TypeChambre.nom_type == nom_type)
                result = session.execute(stmt)
    
                for typechambre in result.scalars():
                    return TypeChambreDTO(typechambre)
    except SQLAlchemyError as e:
            raise ValueError(f"Une erreur est survenue avec la BD : {e}")

def rechercherUsager(nom: str):
    
    try: 
            with Session(engine) as session:
    
                stmtnom = select(Usager).where(Usager.nom == nom)
                if session.execute(stmtnom).scalars().first() is None:
                    raise ValueError( "Aucun usager avec ce nom")
                
                stmt = select(Usager).where(Usager.nom == nom)
                result = session.execute(stmt)
    
                for usager in result.scalars():
                    return UsagerDTO(usager)
    except SQLAlchemyError as e:
            raise ValueError(f"Une erreur est survenue avec la BD : {e}")
     

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

def modifierReservation(reservation:ReservationDTO):
    with Session(engine)as session:
        stmt =select(Reservation).where(Reservation.id_reservation==reservation.id_reservation)
        
        reservationAModifier=session.execute(stmt).scalars().one()
        usager = session.get(Usager, reservation.usager.idUsager)
        chambre = session.get(Chambre, reservation.chambre.id_chambre)
        
        reservationAModifier.date_fin_reservation=reservation.date_fin_reservation
        reservationAModifier.date_debut_reservation=reservation.date_debut_reservation
        reservationAModifier.prix_jour=reservation.prix_jour
        reservationAModifier.info_reservation=reservation.info_reservation
        reservationAModifier.usager=usager
        reservationAModifier.chambre=chambre


        session.commit()
        if reservationAModifier is None:
                    raise ValueError("Reservation introuvable")
        return reservation

def modifierTypeChambre(typechambre:TypeChambreDTO):
    with Session(engine)as session:
        stmt =select(TypeChambre).where(TypeChambre.id_type_chambre==typechambre.id_type_chambre)
        
        typechambreAModifier=session.execute(stmt).scalars().one()
        tychambre = session.execute(select(TypeChambre).where(TypeChambre.id_type_chambre == typechambre.id_type_chambre)).scalar_one()
        if tychambre is None:
            raise ValueError(
                "Type de chambre introuvable : "
                f"{typechambre.id_type_chambre}"
            )
        typechambreAModifier.nom_type=typechambre.nom_type
        typechambreAModifier.prix_plancher=typechambre.prix_plancher
        typechambreAModifier.prix_plafond=typechambre.prix_plafond
        typechambreAModifier.description_chambre=typechambre.description_chambre
        
        session.commit()
        if typechambreAModifier is None:
                    raise ValueError("Type de chambre introuvable")
        return typechambre

def modifierUsager(usager:UsagerDTO):
    with Session(engine)as session:
        stmt =select(Usager).where(Usager.id_usager==usager.idUsager)
        
        usagereAModifier=session.execute(stmt).scalars().one()
        usagerChan = session.execute(select(Usager).where(Usager.id_usager == usager.idUsager)).scalar_one()
        if usagerChan is None:
            raise ValueError(
                "Usager introuvable : "
                f"{usager.idUsager}"
            )
        usagereAModifier.nom=usager.nom
        usagereAModifier.prenom=usager.prenom
        usagereAModifier.adresse=usager.adresse
        usagereAModifier.mobile=usager.mobile
        usagereAModifier.mot_de_passe=usager.motDePasse
        
        
        session.commit()
        if usagereAModifier is None:
                    raise ValueError("Usager introuvable")
        return usager


def creerUsager (usager: UsagerDTO):

    with Session(engine) as session:
        nouveauUsager = Usager(
            nom = usager.nom,
            prenom = usager.prenom,
            adresse = usager.adresse,
            mobile = usager.mobile,
            mot_de_passe = usager.motDePasse,
            id_usager = uuid.uuid4(),
          
        )
        session.add(nouveauUsager)
        session.commit()
        return usager

def supprimerUsager(id_usager: str):

    with Session(engine) as session:
        
        suppUsager = session.get(Usager, id_usager)
        if suppUsager:
            session.delete(suppUsager)
            session.commit()


def supprimerChambre(id_chambre: str):

    with Session(engine) as session:
        
        suppChambre = session.get(Chambre, id_chambre)
        if suppChambre:
            session.delete(suppChambre)
            session.commit()

def supprimerTypeChambre(id_type_chambre: str):

    with Session(engine) as session:
        
        suppTypeChambre = session.get(TypeChambre, id_type_chambre)
        if suppTypeChambre:
            session.delete(suppTypeChambre)
            session.commit()

def supprimerReservation(id_reservation: str):

    with Session(engine) as session:
        
        suppReservation = session.get(Reservation, id_reservation)
        if suppReservation:
            session.delete(suppReservation)
            session.commit()

           
            
        