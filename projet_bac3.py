import abc
from abc import abstractmethod

class Personnes(abc.ABC):
        def __init__(self,nom,post_nom,prenom,age):
            super().__init__()

            self.nom_p=nom
            self.post_nom_p=post_nom
            self.prenom_p=prenom
            self.age_p=age
            
        @abstractmethod
        def signer(self):
            pass

class Enseignant(Personnes):
        def __init__(self, nom, post_nom, prenom, age):
            super().__init__(nom, post_nom, prenom, age)
        

        def enseigner (self):
            print(f"{self.nom_p} il enseigne le cours de ")
        def signer(self):
             pass
         
class Sec_fac(Personnes):
        def __init__(self, nom, post_nom, prenom, age):
            super().__init__(nom, post_nom, prenom, age)

        def aligner (self):  
            print(f"le {self.nom_p} peut aligner un ou plusieur cours")

        def signer(self):
            pass
 
class Cp(Personnes):
        def __init__(self, nom, post_nom, prenom, age):
            super().__init__(nom, post_nom, prenom, age)

        def remplir (self):
             print(f"le {self.nom_p} peut remplire une ou plusieurs fiches  ")

        def signer(self):
            pass
              
class Fiche():
        def __init__(self,volume_horair,Fac,promo,DPT,cp, enseignant):

            self.volu_f=volume_horair
            #self.nom_f=nom
            self.Fac=Fac
            self.promo=promo
            self.DPT=DPT
            self.cp=cp
            self.ens= enseignant


class Cours():
        def __init__(self,intutiler,nombre_heur):
            self.intutiler_c=intutiler
            self.nombre_heur_c=nombre_heur
        def programmaer (self):
            print(f"le cours de {self.intutiler_c} peut etre programmer une est une seul fois c'est un cours de {self.nombre_heur_c}heur")

class promotion():
     def __init__(self,nom):
          self.nom_p=nom
          
     
class Faculte():
     def __init__(self,nom):
          self.nom_f=nom
        
     
class Departement():
     def __init__(self,nom):
          self.nom_d=nom
        
fac=Faculte("sc_info")

Depart=Departement("g_l")
pro=promotion("bac3")
cp1=Cp("franck","jfjf","vi",67)
cour=Cours("poo",45)
ensei=Enseignant("kyembe","samba","sinai",43)
fich1= Fiche(cour.nombre_heur_c,fac.nom_f,pro.nom_p,Depart.nom_d,cp1.nom_p,ensei.prenom_p)
print(f"le cp :{fich1.cp}")
print(f"le departement :{fich1.DPT}")
print(f"la faculté: {fich1.Fac}")
print(f"la promotion: {fich1.promo}")
print(f"volume horaire : {fich1.volu_f}")
print(f"l'enseignant : {fich1.ens}")

ense1=Enseignant("samba","kyembe","sinai",34)
ense1.enseigner()

sec2=Sec_fac("secreteur de faculté","kasongo","ruth",34)
sec2.aligner()

cp3=Cp("chef de promotion","nsenga","emma",20)
cp3.remplir()

cour4=Cours("info",48)
cour4.programmaer() 