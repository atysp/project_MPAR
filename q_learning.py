from importations import *

def q_learning(states, actions, transitions, Ttot=10000, gamma=1/2,):

    statesid = [state.id for state in states]
    statesgain = [float(state.gain) for state in states]

    def indice_Liste(L, elem):
        return L.index(elem)
          
    def simulate (current_state,action):
        """
        simulate : State, Action -> (Int,Int)
        Avec la structure de données :
          states : liste_etats;
          statesid : liste_state.id;
          statesgain : liste_state.gain;
          simulate(simulate(State("S0",""), Action("a"))) renvoie (1,5) ou (2,5)
          simulate : State, Action -> (Int,Int)
        """
        next_transitions = [t for t in transitions if t.departure.id == current_state.id]
        if not next_transitions:
            return current_state
        next_transition = rd.choice(next_transitions)
        weights = np.array(next_transition.weights)
        weights = weights/np.sum(weights)

        next_state = rd.choices(next_transition.targets, weights)
        next_state = next_state[0]

        # return indice_Liste(next_state.id),next_state.gain
        return indice_Liste(statesid,next_state.id),statesgain[indice_Liste(statesid,current_state.id)]

    def choose_state(s,L): 
        """permet de choisir l'état suivant dans l'algo de Q_Learning"""
        #on choisie l'état dans lequel on est et si c'est 3 fois de même le suite on prend l'état 0.
        # si on a 3 fois de suite le même état, on en prend un autre (genre S0)
        if L == [s,s,s]:
            s = 0 #ici on choisit l'état 0 mais on pourrait prendre un état au hasard.
        else:
            if len(L)==3:
                L.pop(0)
                L.append(s) 
            else:
                L.append(s) 
        return s,L

    def choose_action(Q, s, eps=0.1): #on choisie le Dilemne Exploration / Exploitation ε-greedy
        x = rd.random()
        if x < eps:
            action = np.argmax(Q[s])
        else:
            action = rd.randrange(np.shape(Q)[1]) # choix entre les différentes actions
        return action

    def q_learning(choose_state, choose_action, simulate, Ttot, Q0, gamma, etat_init):

        # Initialisation de la fonction Q, de L, de etat et de alpha.
        Q = Q0
        L = []
        etat = etat_init
        alpha = np.ones(np.shape(Q0))

        # Boucle principale
        for t in range(Ttot):
            # Choix de l'état et de l'action
            st,L = choose_state(etat,L)
            print(st,L)
            at = choose_action(Q, st)
            alpha[st,at]+=1

            # Simulation de l'état suivant et de la récompense associée
            st = states[st] # INT -> State
            st1, rt = simulate(st, at) 
            st = indice_Liste(states,st) # State -> Int
            print(st)
            # Mise à jour de la fonction Q
            max_Q = np.max(Q[st1])
            Q[st, at] += 1/alpha[st,at] * (rt + gamma * max_Q - Q[st, at]) #plus on rencontre un état, plus alpha[st,at] augment donc on le modifie moins

            etat = st1 # on a traité cet état qui sera réutiliser dans choose_state

            #affichage
            print(alpha)
            print("-"*12)
            print(Q)
            print()
        return Q

    Q0 = np.zeros((len(states), len(actions)))
    print(Q0)
    etat_init = indice_Liste(states,states[0])
    print(f"mon état initial est {etat_init}")

    Q = q_learning(choose_state, choose_action, simulate, Ttot, Q0, gamma, etat_init)
    return Q 