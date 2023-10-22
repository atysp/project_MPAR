from importations import *
from random_walk import random_walk

def visu_random_walk(states, actions, transitions,n=3):

    #Création du graphe
    dot = Digraph(comment='MPAR', format='png')
    for state in states :  
        dot.node(str(state.id), color="red")
        
    for k in range (len(transitions)) : 
        for j in range (len(transitions[k].targets)) : 
            target = transitions[k].targets[j]
            somme = np.sum(transitions[k].weights)
            frac = transitions[k].weights[j] / somme
            frac = Fraction(frac).limit_denominator(10)
            if (type(transitions[k].action) != str) : 
                dot.edge(transitions[k].departure.id,target.id,label = f"{transitions[k].action.id},{frac.numerator}/{frac.denominator}",  color="black")
            else :
                dot.edge(transitions[k].departure.id,target.id,label = f"{frac.numerator}/{frac.denominator}",  color="black")
    
    #Marche aléatoire
    start_state = states[0]
    dot.node(str(start_state.id), color="blue")
    dot.view("Etat initial")
    dot.node(str(start_state.id), color="red")
    end_state = random_walk(transitions, start_state)
    print(f"Chemin 1: départ de {start_state} et arrivée à {end_state}")
    dot.node(str(end_state.id), color="green")
    dot.view("Transition numéro 1")
    dot.node(str(end_state.id), color="red")
    print()
    for i in range(1,n):
        dot.node(str(end_state.id), color="red")
        start_state = end_state
        end_state = random_walk(transitions, start_state)
        dot.node(str(end_state.id), color="green")
        dot.view(f"transition numéro {str(i+1)}")
        print(f"Chemin {i+1}: départ de {start_state} et arrivée à {end_state}")
        print()
        time.sleep(1)
