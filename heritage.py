class Personne:

    def __init__(self,p_nom_personne,p_post_nom_personne,p_prenom_personne,p_age_personne):
        self.nom_personne=p_nom_personne
        self.post_nom=p_post_nom_personne
        self.prenom=p_prenom_personne
        self.age=p_age_personne

    def sePresenter(self):
        print(f"bonjour je m'appel {self.nom_personne} {self.post_nom} {self.prenom} j'ai {self.age} ans")

p1=Personne("kyembe","samba","sinai",34)
p1.sePresenter() 

class Animal(Personne):
    def __init__(self,p_nom_personne,p_post_nom_personne,p_prenom_personne,p_age_personne,nbre_pat):
        super().__init__(p_nom_personne,p_post_nom_personne,p_prenom_personne,p_age_personne)
        self.pat=nbre_pat

p2= Animal("kyembe","samba","sinai",31,4)
p2.sePresenter() 




