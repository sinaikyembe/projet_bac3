class ErreurDeSaisie(Exception):
    pass

class ErrurDeCalcul(Exception):
    pass
class Division:
    @classmethod
    def saisie_nombre(cls):
        try:
            nombre= int(input("Entrez un nombre"))

            if nombre<0:
                raise ErreurDeSaisie("le nombre doit etre positif")
            return nombre
        except ValueError:
            raise ErreurDeSaisie("vous devez entrez un nombre entier ")
    @classmethod    
    def deiviser(cls,nbr1,nbr2):
        try:
            resultat= nbr1/nbr2
            #if resultat == float(resultat):
             #   raise ErreurDeSaisie("Erreur division par zero")
            return resultat
        except ZeroDivisionError:
            raise ErrurDeCalcul("Division par zero")
     
# fonction de saisie


    

try:
        nombre1=Division.saisie_nombre()
        nombre2= Division.saisie_nombre()
        resultat= Division.deiviser(nombre1,nombre2)
        print("le resultat de la division est :", resultat)
except(ErreurDeSaisie,ErrurDeCalcul) as e:
        print(" une erreur est survenue",e)
