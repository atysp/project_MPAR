from importations import *

def transi_depart (s,a,transitions) : 
    """Donne les états accessibles depuis s avec l'action a ainsi que leur proba associée."""
    etats = []
    probas = []
    for transition in transitions :
        if transition.departure.id == s.id and transition.action.id == a.id : 
           etats = transition.targets
           weights = transition.weights 
           somme = np.sum(transition.weights)
           probas = list (np.array(weights)/somme)
    #print(etats,probas)
    return(etats,probas)

def iteration_valeur (eps,gamma, states, actions, transitions) : 
    
    statesid = [state.id for state in states]
    statesgain = [state.gain for state in states]
    
    n = len (states)
    Vn = np.array([0] * n) #nombre états
    vn1 = np.array( [float(states[k].gain) for k in range(n)]) 
    #Calcul de Vn+1-Vn jusqu'a ce que ca converge
    while ( (np.max(abs(Vn-vn1)) ) >= eps ): 
        copy = vn1
        for k in range(n) : 
            possible = []
            s = states[k]
            
            r = float(s.gain)
            for a in actions :
                (etats,proba) = transi_depart(s,a,transitions)
                somme = 0 
                for j in range ( len(etats) ) :
                    somme += proba[j] * Vn[statesid.index(etats[j].id)] 
                possible.append( r + gamma * somme )
            vn1[k] = max (possible)
        Vn = copy
        
    #Choix de l'adversaire 
    adversaire = []  
    for k in range(n) : 
            possible = []
            s = states[k]
            r = 0
            act = ''
            sc = 0
            for a in actions :
                (etats,proba) = transi_depart(s,a,transitions)
                somme = 0 
                for j in range ( len(etats) ) :
                    r += float(statesgain[statesid.index(etats[j].id)])
                    somme += proba[j] * Vn[statesid.index(etats[j].id)] 
                if len(etats) != 0 and sc < r/len(etats) + gamma * somme  :
                    sc = r/len(etats) + gamma * somme 
                    act = a 
                
            adversaire.append(act)
     
    print(Vn, adversaire)        
    return (adversaire,Vn)