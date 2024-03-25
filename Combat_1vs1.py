from playermodel import SuperPlayer
from ClasseModel import Guerrier

list_players = []

#//////////////////////////////// DEBUT DE LA PRESENTAION /////////////////////////////

# Un objet est un élément qui peut représenter un concept ou même un idée, si on prend le cas jeux vidéo 
# par exemple on pourrait identifer à l'intérieur de ce dernier plusieurs objets, commen un certain
# joueur disposant d'un nombre de points de vie, points d'attaque, ou alors d'une arme qui possède une
# durabilité. C'est la version supérieure d'une liste capable d'ajouter des caratéristiques à chaque nouvel
# élément et de les faire interagir entre elles. Voici un petit programme qui enregistre des joueurs 
# ayant un pseudo, des points d'attaque et des points de vie pour les faire combattre chacun leur tour.

#                           ---------- 0) -----------
# Veuillez suivre la visiste guidée ci dessous avec les numéros de 0 à 9. Le numéro 1 commence dans
# la fonction main juste ci-dessous L19.

def main(): 
    #                       ---------- 1) ----------
    # Tout d'abord nous créons des joueurs, qui seront enregistrés dans une base de données.
    # Rendez-vous dans la fonction new_player ci-dessous L127.  
    print("Bienvenue sur Arcanis ! ") 
    new_player()
    #                       ---------- 5) -----------
    # Puis nous les faisons combatre, après verification de leurs enregistrements dans la data base.
    combat()
    print("Aurevoir et à bientôt sur Arcanis")
    # RENDEZ VOUS dans la fonction "combat"L70.

#                           ---------- 7) ---------
# La fonction va demander les pseudos qui doivent se combattre, puis rechercher une correspondance dans la
# liste "list_players" pour retourner leur index.
def create_or_check_if_user_is_alive():
    i = len(list_players)  
    while(i > 0):
        if i == len(list_players):
        # On demande le pseudo d'un combattant.
            player1 = input(" ")
        # On vérifie si il correspond à l'index i.
        if player1 == SuperPlayer.get_pseudo(list_players[i - 1]):
            # Si oui on vérifie s'il est vivant et apte.
            if SuperPlayer.get_health(list_players[i - 1]) <= 0:
                # S'il est inapte, on écrit un message, puis on réinitialise la boucle au début.
                print("Ce personnage est mort !")
                i = len(list_players)
                continue
            # S'il est apte on ferme la fonction en renvoyant l'index correspondant.
            print("Combattant prêt pour le combat !")
            return i-1
        # S'il n'y a pas de correspondance on demande à l'utilisateur de recommencer ou enregistrer un 
        # nouveau joueur.
        if i == 1:
            print("Ce nom n'est pas enregistré comme un joueur veuillez l'enregistrer ou réessayer.")                
            while(1):
                log_or_sign = input("Taper : sign-in (pour enregistrer un nouveau joueur)" 
                                    "or log-in (pour rentrer un combattant dans l'arène)")
                # Si l'utilisateur choisit d'enregistrer un nouveau joueur, le programme le redirige
                # dans la fonction new_player
                if log_or_sign == "sign-in":
                    print("-----Redirection au bureau des inscriptions -----")
                    new_player()
                elif log_or_sign == "log-in":
                # S'il choisit d'enregister un combattant on le redirige au début de la fonction en quittant
                # cette boucle et en rénitialisant i.
                     print("-----Redirection à l'arène -----")
                     break  # <--- On quitte la boucle
            i = len(list_players) # <--- On rénitialise i.
            continue # <--- On revient au début de la boucle.
        i -= 1 # L'incrémantation de i.
        # RENDEZ VOUS au 8) dans la fonction combat.L95

#                               ---------- 6) ----------
# Voici la fonction combat :
def combat():
    # Premièrement on demande si le joueur veut organiser un combat.
    ask_combat = input("Voulez-vous organiser un combat 1vs1 ? ")
    # Si oui on continue ci-dessous avec un message assurrant la prise en compte de la réponse du joueur.
    if ask_combat == "oui":
        print("Ouverture de l'arène.... ")
    # Puis le programme va chercher l'index des combattants de la liste "list_players".
        print("Entrez le pseudo du premier combattant : ")
        index_player1 = create_or_check_if_user_is_alive()
        while(1):
            print("Entrez le pseudo du Deuxièmme combattant : ")
            index_player2 = create_or_check_if_user_is_alive()
            if index_player1 == index_player2: # <--- Vérification que les combattants sont différents.
                print("Le combatant {} est déjà  enregistré, recommencer "
                      .format(SuperPlayer.get_pseudo(list_players[index_player2])))
            else:
                break
    else:
    # Si non le programme s'arrête.
        print("Pas de combat au revoir")
        return
    
    # RENDEZ VOUS dans la fonction create_or_check_if_user_is_alive.L28
    
    #                           ---------- 8) -----------
    # Une fois la présentation faite place au combat.
    while(1):
        # Le joueur 1 attaque le joueur 2 une fois.
        print(str(SuperPlayer.get_pseudo(list_players[index_player1]))+" attaque "+
              str(SuperPlayer.get_pseudo(list_players[index_player2])))
        
        SuperPlayer.attack_player(list_players[index_player1], list_players[index_player2])

        print(str(SuperPlayer.get_pseudo(list_players[index_player2]))+
              " "+str(SuperPlayer.get_health(list_players[index_player2]))+" point de vie restant ")
        
        # On verifie si le joueur 2 est vivant.

        if SuperPlayer.get_health(list_players[index_player2]) <= 0:
            # Si non on affiche un message de victoire en indiquant les points de vie restant du gagnant.
            print(str(SuperPlayer.get_pseudo(list_players[index_player1]))+" win, pv restant :"
               , str(SuperPlayer.get_health(list_players[index_player1])))
            # Puis on ferme le combat en fermant la boucle avec "break".
            break
        # Ici le joueur 2 riposte.
        print(str(SuperPlayer.get_pseudo(list_players[index_player2]))+" attaque "+
              str(SuperPlayer.get_pseudo(list_players[index_player1])))
        
        SuperPlayer.attack_player(list_players[index_player2], list_players[index_player1])
        
        print(str(SuperPlayer.get_pseudo(list_players[index_player1]))+
              " "+str(SuperPlayer.get_health(list_players[index_player1]))+" point de vie restant ")
        # On verifie si le joueur 1 est vivant.
        if SuperPlayer.get_health(list_players[index_player1]) <= 0:
            # Si non on affiche un message de victoire en indiquant les points de vie restant du gagnant.
            print(SuperPlayer.get_pseudo(list_players[index_player2])+" win, pv restant :"
                   , SuperPlayer.get_health(list_players[index_player2]))
            # Puis on ferme le combat en fermant la boucle avec ce "break".
            break
    # Une fois le combat terminé, on demande si l'utilisateur veut faire un autre combat.
    ask_combat = input("Organiser un autre combat ? ")
    if ask_combat == "oui":
        # Si oui on rappelle la fonction combat.
        combat()    
    # Si non on affiche la fermeture de l'arène, puis c'est ici que la fonction et le programme s'arrête.
    print("Fermeture de l'arène ")
    # RENDEZ VOUS à la fin du Fichier L 156.

        
def new_player():
    #                           ---------- 2) ----------
    # C'est à partir d'ici que les informations sur les joueurs sont insérées dans le programme.
    while(1):
        newplayer = input("Voulez-vous enregistrer un nouveau joueur ? ")
        if newplayer == "oui" or newplayer == "OUI" or newplayer == "Oui":
            newplayer_name = input("Entrez son pseudo : ")
            newplayer_class = input("Choisir sa classe : A--> Guerrier /"+ 
                                     "B--> Voleur / C--> Mage / Défault paysan : ")
    # Une fois toutes les informations propres au joueur collectées, nous créons le joueur grâce 
    # à la classe SuperPlayer (Défault) ou avec les sub-class Guerrier etc...
    # Nous créons ici une liste qui gardera en mémoire les références des différents objets enregistrés.
            
            if newplayer_class=="A" or newplayer_class=="a":
                list_players.append(Guerrier(newplayer_name))
            else:
                list_players.append(SuperPlayer(newplayer_name))
        # RENDEZ VOUS dans le fichier "playermodel.py" L1.
    #                           ---------- 4) ----------            
    # Quand les inscriptions sont finies, le programme affiche les pseudos des joueurs enregistrés
    # grâce à "list_players".
        else:
            if len(list_players) == 0:
                print("Aurevoir et à bientôt sur Arcanis")
                exit()
            dispplay_list_players(len(list_players))        
            break
    # RENDEZ VOUS dans la fonction "main"L23.

def dispplay_list_players(i):
    print("La liste des joueurs sont : ")
    while(i > 0):
        print(SuperPlayer.get_pseudo(list_players[i - 1]))
        i -= 1 

            
if __name__ == '__main__':
    main()

    #                           ---------- 9) ----------
    # Voici un aperçu de mes compétences dans le chapitre "Les objets" du Langage Python.
    # Temps d'écriture de ce programme + les commentaires = 4 à 5 heures.
    # Auteur : Grégoire Coudrin fait le 05/11/2023 14h00.
    #  # ////////////////////////// FIN DE LA PRESENTATION //////////////////////////////////