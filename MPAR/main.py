
from importations import *
from classes import * 

from iteration_valeurs import * 
from smc import *
from q_learning import *
from visualisation import *
from accessibilite import *

#test
from random_walk import walk


def main():
    
    # structure de données 
    lexer = gramLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    data_listener = gramDataListener()
    walker = ParseTreeWalker()
    walker.walk(data_listener, tree)
    
    #création de states, actions, transitions
    states = data_listener.states
    actions = data_listener.actions
    transitions = data_listener.transitions
    statesid = [state.id for state in states]
    statesgain = [state.gain for state in states]
    
    print(f"Liste des états : {statesid}")
    print(f"Liste des gains : {statesgain}")
    print()
    print(actions)
    print()
    for transition in transitions:
        print(transition)
    print()

    #Vérification : chaque transition est effectuée avec une action définie
    for transition in transitions:
        if str(transition.action) not in str(actions) and transition.action.id != '':
            raise ValueError(f"{transition.action.id} n\'est pas une action valide")
        
    #Vérification : chaque transition part d'un état bien défini vers un état bien défini
    for transition in transitions:
        if str(transition.departure.id) not in str(statesid) :
                    raise ValueError(f"{transition.departure.id} n\'est pas un état valide")
                
        for target in transition.targets : 
            if str(target.id) not in str(statesid) : 
                    raise ValueError(f"{target.id} n\'est pas un état valide")
                
    #Vérif pas déterministe et non-déterministe
    l1 = []
    l2 = []
    for transition in transitions:
        if  transition.action.id != '':
            l1.append(transition.departure.id)
        else :
            l2.append(transition.departure.id)
    intersection = [x for x in l2 if x in l1]
    if len (intersection) !=0 : 
            raise ValueError(f"{intersection[0]} est à la fois déterministe et non-déterministe.")
            
    #Vérif : chaque état à une tansition
    e = []
    for transition in transitions:
        if transition.departure.id not in e : 
            e.append(transition.departure.id)
    if len(e) != len(states) : 
        l = [x.id for x in states if x.id not in e]
        raise ValueError(f"{l[0]} n'a pas de transition.")
    

    #code à exectuer:
    # walk(transitions, states[0])
    # visu_random_walk(states,actions, transitions) 
    # accessibilite('D1',transitions, states)
    # q_learning(states,actions,transitions,100,1/2)
    # accessibilite_mdp('S11',transitions,states,['a']*16)

if __name__ == '__main__':
    main()

