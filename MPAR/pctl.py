from importations import *

def model_checking(s, P, transitions):
    """Fonction qui vérifie si la propriété P est vraie en partant de l'état s."""
    
    visited = [] # liste des états visités
    to_visit = [s] # liste des états à visiter
    
    while to_visit:
        current = to_visit.pop(0) # on récupère le premier élément de la liste
        visited.append(current) # on ajoute l'état visité à la liste des états visités
        
        if P(current): # si la propriété est vraie pour l'état courant, on renvoie True
            return True
        
        transitions = [t for t in transitions if t.departure.id == current.id] # liste des transitions depuis current
        for t in transitions: # on itère sur les transitions sortantes de l'état courant
            if t not in visited and t not in to_visit: # si l'état n'a pas déjà été visité et n'est pas dans la liste des états à visiter
                to_visit.append(t) # on l'ajoute à la liste des états à visiter
    
    return False # si on a visité tous les états accessibles sans trouver l'état vérifiant la propriété, on renvoie False


def identifier_ensembles(P, s, etats, transitions):
    # Liste des états qui satisfont directement P
    S1 = [e for e in etats if P(s, e)]
    
    # Liste des états qui satisfont P en un nombre fini de pas
    S = []
    # Liste des états qui ne satisfont pas P en un nombre fini de pas
    S0 = []
    
    # Algorithme de vérification de modèle CTL pour identifier S
    for e in etats:
        if e not in S1:
            if model_checking(P, e, transitions)==True: # il existe un chemin qui vérifie P
                S.append(e)
            else:
                S0.append(e)
    return S0, S1, S

def conj_grad(A, b, x_0, eps=1e-5, max_iter=1000):
    """
    Résolution d'un système linéaire Ax = b avec la méthode du gradient conjugué.
    :param A: matrice du système linéaire
    :param b: vecteur du second membre
    :param x_0: vecteur initial de la solution
    :param eps: précision souhaitée
    :param max_iter: nombre maximal d'itérations
    :return: vecteur de la solution
    """
    x = x_0
    r = b - np.dot(A, x)
    p = r
    for i in range(max_iter):
        Ap = np.dot(A, p)
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_new = r - alpha * Ap
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p
        r = r_new
        if np.linalg.norm(r) < eps:
            break
    return x