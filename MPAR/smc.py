from importations import m
from etat_final import etat_final

def smc_quantitatif (S,n,eps,delt,  states, actions, transitions) : 
    """ But de smc_quantitatif : on donne un etat terminal S, une longueur n , une precision epsilon(eps), un taux d'erreur delta(delt) 
    et on renvoie l'estimation que le modèle satisfasse S en n tours ou moins"""
    
    compt = 0
    N = (m.log(2)-m.log(delt)) / (4*eps**2)
    
    for k in range (m.ceil(N)) : 
        state = etat_final(n,states,actions,transitions)
        if S == state : 
            compt += 1 
    print(compt/N)

def smc_qualitatif (alpha,beta,theta,n,S, states, actions, transitions) : 
    """ But de smc qualitatif : On donne un etat S, une longueur n, deux bornes alpha/beta et une valeur theta 
et on renvoie si la probabilité que l'algo atteigne S en n coups ou moins est inférieure à theta"""

    precision = 0.01 #epsilon
    gamma0 = theta - precision
    gamma1  = theta + precision
    LA = m.log10((1-beta)/alpha)
    LB = m.log10(beta/(1-alpha))
    print(LB,LA)
    Vrem = m.log10((1-gamma1) / (1- gamma0)  )
    Vadd = m.log10 (gamma1/gamma0) # On fait le programme sous forme logarithmique : moins de calculs 
    max = 1000000000 #on fixe un nombre max de simulations au bout du quel on peut se dire que c'est faux -> en réalité on attend a l'infini
    Rm = 0
    mgood = 0
    for k in range (1,50000) :
        state = etat_final(n,states,actions,transitions)
        if state == S:
            Rm += Vadd
            mgood += 1 
        else :
            Rm += Vrem        
        if Rm > LA :
            # print(mgood/k)
            print("plus grand que", theta)
            return(0)
        if Rm < LB : 
            #print(mgood/k)
            print("plus petit que", theta)
            return(0)
        
    return("Pas fini")