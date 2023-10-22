from random_walk import random_walk_without_comment

def etat_final(n,states,actions,transitions) :
    """ But de etatfinal : renvoie l'etat final au bout d'un parcours aléatoire de longueur n"""
    
    #Marche aléatoire
    start_state = states[0]
    end_state = random_walk_without_comment(transitions, start_state)
    for i in range(1,n):
        start_state = end_state
        end_state = random_walk_without_comment(transitions, start_state)
    return (end_state.id)



