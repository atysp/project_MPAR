from importations import *

def random_walk(transitions, current_state):

    """ Passer d'un état à un état suivant dans les MC et les MDP en tenant compte des poids de chaque transition"""

    while True:
        print(f"current_state : {current_state}")
        next_transitions = [t for t in transitions if t.departure.id == current_state.id]
        print(f"next_transitions : {next_transitions}")
        if not next_transitions:
            return current_state
        next_transition = rd.choice(next_transitions)
        weights = np.array(next_transition.weights)
        weights = weights/np.sum(weights)

        next_state = rd.choices(next_transition.targets, weights)
        next_state = next_state[0]
        print(f"next_action : {next_transition.action}")
        print(f"next_state : {next_state}")
        return next_state
    
def walk(transitions, current_state, n = 3):

    """Marche Aléatoire avec n transitions"""
    
    i = 0
    while i<n:
        print(f"current_state : {current_state}")
        next_transitions = [t for t in transitions if t.departure.id == current_state.id]
        print(f"next_transitions : {next_transitions}")
        if not next_transitions:
            return current_state
        next_transition = rd.choice(next_transitions)
        weights = np.array(next_transition.weights)
        weights = weights/np.sum(weights)

        next_state = rd.choices(next_transition.targets, weights)
        next_state = next_state[0]
        print(f"next_action : {next_transition.action}")
        print(f"next_state : {next_state}")
        current_state = next_state
        i+=1
    return next_state
    
def random_walk_without_comment(transitions, current_state):
    while True:
        next_transitions = [t for t in transitions if t.departure.id == current_state.id]
        if not next_transitions:
            return current_state
        next_transition = rd.choice(next_transitions)
        weights = np.array(next_transition.weights)
        weights = weights/np.sum(weights)

        next_state = rd.choices(next_transition.targets, weights)
        next_state = next_state[0]
        return next_state