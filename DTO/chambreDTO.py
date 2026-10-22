from typing import Optional
from pydantic import BaseModel, Field, model_validator
from model import TypeChambre, Chambre, Usager
from uuid import UUID

# Data transfer Object: pydantic BaseModel pour intégration facile avec Fast API
# Facilite aussi grandement la sérialization et la validation des donnés contenues


class TypeChambreDTO(BaseModel):
    id_type_chambre : Optional[UUID] = None
    nom_type: str = Field(max_length=6)  #changer pour le bon max lenght
    prix_plafond: Optional[float] = None
    prix_plancher: float
    description_chambre: Optional[str] = None


    @model_validator(mode='after')
    def verifier_prix_par_type(self):
         if (self.nom_type == 'simple' and self.prix_plancher > 250) :
              raise ValueError("Un simple ne peut pas louer plus de 250 par nuit")
         return self    





    def __init__(self, typeChambre: TypeChambre =None):
        super().__init__(id_type_chambre = typeChambre.id_type_chambre,
                         nom_type = typeChambre.nom_type,
                         prix_plafond = typeChambre.prix_plafond,   
                         prix_plancher = typeChambre.prix_plancher,
                         description_chambre = typeChambre.description_chambre
                         )

class ChambreDTO(BaseModel):
    idChambre : Optional[UUID] = None
    numero_chambre: int = Field(le=999, ge=0, custom_error="Le numéro doit être entre 0 et 999")
    disponible_reservation : bool = Field(default=True)
    autre_informations: Optional[str] = Field(None, max_length=200, custom_error="200 caractères maximum pour les autres informations")
    type_chambre: TypeChambreDTO



    def __init__(self, chambre: Chambre =None):
            super().__init__(idChambre = chambre.id_chambre,
                             numero_chambre = chambre.numero_chambre,
                             disponible_reservation = chambre.disponible_reservation,
                             autre_informations = chambre.autre_informations,
                             type_chambre = TypeChambreDTO(chambre.type_chambre) 
                             )

class UsagerDTO(BaseModel):
     idUsager : Optional[UUID] = None
     motDePasse : Optional[str] = Field(None, max_length=50, custom_error="50 caractères maximum pour le mot de passe")
     nom : str = Field( max_length=50, custom_error="50 caractères maximum pour le nom et non vide")
     prenom : str = Field( max_length=50, custom_error="50 caractères maximum pour le prenom et non vide")
     adresse : str = Field( max_length=100, custom_error="100 caractères maximum pour l'adresse et non vide")
     mobile : Optional[str] = Field(None, max_length=50, custom_error="50 caractères maximum pour le numéro de mobile")


     def __init__(self, usager: Usager =None):
                 super().__init__(idUsager= usager.id_usager,
                                  motDePasse = usager.mot_de_passe,
                                  nom = usager.nom,
                                  prenom = usager.prenom,
                                  adresse = usager.adresse,
                                  mobile = usager.mobile
                                  )