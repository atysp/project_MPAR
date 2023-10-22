def all_target (targets,l) :
    #return true si toutes les targets sonts dans la liste l
    for target in targets : 
        if target.id not in l :
            return False
    return True

def parcours (S,S0,S1,transitions) : 
    "renvoie True si il n'existe un chemin de S vers un état de S1"
    etats = [S] 
    vus = S0.copy()
    while etats != [] :
        e = etats[0]
        vus.append(e)
        etats = etats [1:]
        for transition in transitions :
            if transition.departure.id == e :
                for t in transition.targets : 
                    if t.id in S1 :
                        return True
                    if t.id not in vus : 
                        etats.append(t.id)
    
    return False
            
def accessibilite (s, transitions, states) : 
    
    S0 = []
    S1 = [s]
    S2 = []
    
    #S0 = états à partir desquels on est sur de pas pouvoir acceder à s. 
    #S1 = états pour lesquels on est sur d'accéder à s
    #S2 = états à partir desquels on ne sait pas
    
    #Initialisation de S0 = ajout des états qui bouclent sur eux même et qui sont différets de s:
    for transition in transitions : 
        if len(transition.targets) == 1 and transition.targets[0].id == transition.departure.id != s :
            S0.append(transition.departure.id)
         
    changement = True #signifie qu'on a soit rajouté qqch dans S1 ou S0     
       
    while changement :
        changement = False
        for transition in transitions : 
            targets = transition.targets
            
            #On rajoute un sommet dans S0 si on a toutes les targets dans S0  et que le sommet n'est pas déja dans S0
            if all_target(targets,S0) and transition.departure.id not in S0: 
                S0.append(transition.departure.id)
                changement = True
                
            #On rajoute un sommet dans S1 si on a toutes les targets dans S1  et que le sommet n'est pas déja dans S1
            if all_target(targets,S1) and transition.departure.id not in S1: 
                S1.append(transition.departure.id)
                changement = True
                
    #S2 = reste des états 
    for x in states : 
        if x.id not in S0 and x.id not in S1 : 
            if  parcours (x.id,S0,S1,transitions) :
                S2.append(x.id)
            else : 
                S0.append(x.id)
    
    print(f"S0 = {S0} ; S1 = {S1} ; S? = {S2}")
    
#Rajouter : choisir l'adversaire pour les processus de décision markovien. --> faire prog accessibilite_mdp ou on choisi un adversaire
#puis on créée une copie des transitions en supprimant les transitions pas possibles avec notre adversaire puis on applique accessibilité.


def suppr(transitions,adversaire,statesid) : 
    l = []
    for t in transitions : 
        i = statesid.index(t.departure.id)
        a = t.action
        
        if str(adversaire[i]) == str(a.id) : 
            l.append(t)
    return l 

def accessibilite_mdp (s, transitions, states,adversaire) : 
    statesid = [state.id for state in states]
    l = suppr(transitions,adversaire,statesid)
    print(adversaire)
    print(l)
    accessibilite(s,l,states)