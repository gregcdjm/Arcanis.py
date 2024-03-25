# 3) Voici la class "SuperPlayer" elle récupère les informations transmises au préalable et effectue 
# les instructions correspondantes à l'ordre précédent.
class SuperPlayer:
        def __init__(self, pseudo): # <--- dépôt des informations du joueur
            self.pseudo = pseudo
            self.health = 10                    # <--- création et stockage des carastérisitques 
            self.attack = 2                     # du joueur selon les informations du dépot.

            # Petit message de bienvenue pour s'assurer sue le joueur est bien enregistré.
            print("Bienvenue au joueur "+self.pseudo+" vous avez ",str(self.health),"point de vie et {} "
                  "points d'attack" .format(self.attack))
            
    # Il est possible d'inclure des méthodes permettant d'intérargir avec notre base de données ci-dessus 
    # On peut identifier 3 grands types de méthodes :
    # a) Les "guetteurs" ou "assesseurs" qui permettent de récupérer des informations :

        def get_pseudo(self):     # <--- Permet de récupérer(return) le pseudo de l'objet renseigné.
            return self.pseudo
        def get_health(self):     # <--- Permet de récupérer(return) le nombre de point de vie de l'objet.
            return self.health    
        def get_attack(self):     # <--- Permet de récupérer(return) le nombre de point d'attaque de l'objet.
            return self.attack
    
    # b) Les "setteurs" ou "mutateurs" qui permettent de changer/modifier les valeurs

        def damage(self, damage):   # Si on met player1.damage(5) la base de données effectura une modification 
            self.health -= damage   # propre à la méthode "damage" et de son argument (5) c'est à dire
                                    # -5 sur le "Health" de "player1".

    # c) Les autres méthodes permettent d'interagir entre les méthodes

        def attack_player(self, target_player): # Si on met player1.attack_player(player2) player2 subira 
            target_player.damage(self.attack)   # les dégâts de player1

    # RENDEZ VOUS sur la fonction "new_player" du fichier "Les objets.py" L139

