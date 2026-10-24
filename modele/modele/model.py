from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column

class Base(DeclarativeBase):
        pass


class Chambre(Base):
        __tablename__ = "chambre"

        numero_chambre: Mapped[int]
        disponible_reservation: Mapped[bool]
        autre_informations: Mapped[str]
        id_chambre: Mapped[str] = mapped_column(primary_key=True)

        fk_type_chambre: Mapped[str] = mapped_column(ForeignKey("type_chambre.id_type_chambre"))


        type_chambre: Mapped['TypeChambre'] = relationship()
        reservations: Mapped[List["Reservation"]] = relationship(back_populates="chambre")

class TypeChambre(Base):
        __tablename__ = "type_chambre"

        nom_type: Mapped[str]
        prix_plafond: Mapped[float]
        prix_plancher: Mapped[float]
        description_chambre: Mapped[str]
        id_type_chambre: Mapped[str] = mapped_column(primary_key=True)

        chambres: Mapped[List["Chambre"]] = relationship(back_populates="type_chambre")


class Usager(Base):
        __tablename__ ="usager" 

        prenom: Mapped[str]
        nom: Mapped[str]
        adresse: Mapped[str]
        mobile: Mapped[str]
        mot_de_passe: Mapped[str]
        id_usager: Mapped[str] = mapped_column(primary_key=True)

        reservations: Mapped[List["Reservation"]] = relationship(back_populates="usager")


        

class Reservation(Base):
        __tablename__ ="reservation" 
        
        date_fin_reservation: Mapped[str]
        date_debut_reservation: Mapped[str]
        prix_jour: Mapped[float]
        info_reservation: Mapped[str]
        id_reservation:  Mapped[str] = mapped_column(primary_key=True)

        fk_id_usager: Mapped[str] = mapped_column(ForeignKey("usager.id_usager"))
        fk_id_chambre: Mapped[str] = mapped_column(ForeignKey("chambre.id_chambre"))


        chambre: Mapped['Chambre'] = relationship()
        usager: Mapped['Usager'] = relationship()
       


#TODO : La classe Usager avec une relation de 1 à N vers la classe réservation.
#TODO : La classe Reservation avec une relation de 1 à 1 vers la classe Usager et une relation de 1 à 1 vers la classe Chambre. 
#TODO: Ajouter une relation de 1 à N dans la classe Chambre vers la classe Reservation