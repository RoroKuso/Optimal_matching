"""Contient les différentes fonctions introduites dans le projet"""
import gurobipy as gp
from gurobipy import GRB
import numpy as np
from typing import Tuple
import logging
import time
from sys import argv


def question_1(N, V=None, lower=0, upper=15):
    """
        Maximisation de la satifaction moyenne des agents. Retourne l'affectation obtenue.
        
        Args:
            N (int): taille de la matrice d'utilités
            V (int array): matrice d'utilités. Si non renseignée elle est générée aléatoirement.
            lower (int): borne inférieure si ``V`` non renseignée
            upper (int): borne supérieure si ``V`` non renseignée
    """
    
    logging.info("-----------résolution question_1-----------")
    
    if V is not None:
        U = V
    else:
        U = np.random.randint(lower, upper, size=(N,N))
        
    logging.info("U matrix\n" + str(U))
    #U = U.transpose()
    
    # Création du modèle
    m = gp.Model("question_1")
    
    # Ajout des variables
    X = m.addMVar((N,N), vtype=GRB.BINARY)

    # Ajout de la fonction objectif
    m.setObjective(gp.quicksum((gp.quicksum(X[j]*U[j]) for j in range(N)))/N, GRB.MAXIMIZE)

    # Ajout des contraintes
    m.addConstrs(gp.quicksum(X[j]) == 1 for j in range(N))
    m.addConstrs(gp.quicksum(X.transpose()[j]) == 1 for j in range(N))
    
    # Résolution
    m.optimize(callback=None)
    
    res = [X[i][j].X * U[i][j] for i in range(N) for j in range(N) if X[i][j].X > 0]
    logging.info("affectation obtenue : " + str(res) + "valeur objectif = " + str(m.ObjVal))
    logging.info("<------Fin appel question_1------>")
    return res


def question_4_indicator(N: int, eps: float = 0.01, V=None, lower=0, upper=20):
    """Même rôle que la question 4 mais utilise une contrainte générale INDICATOR.

    Args:
        eps (float): facteur de la somme des satisfaction
        N (int): taille de la matrice d'utilités
        V (int array): matrice d'utilités. Si non renseignée elle est générée aléatoirement.
        lower (int): borne inférieure si ``V`` non renseignée
        upper (int): borne supérieure si ``V`` non renseignée

    Returns:
        array
    """
    if V is not None:
        U = V
    else:
        U = np.random.randint(lower, upper, size=(N,N))
        
    logging.info(">------résolution question_4_indicator------<")
    logging.info("U matrix\n" + str(U))

    # Création du modèle
    m = gp.Model("question4")
    X = np.array([[m.addVar(vtype=GRB.BINARY) for j in range(N)] for i in range(N)])
    Y = m.addVar(vtype = GRB.INTEGER)
    m.update()
    
    # Ajout de la fonction objectif
    obj = gp.LinExpr()
    obj = 0
    for i in range(N):
        for j in range(N):
            obj += eps * X[i][j] * U[i][j]
    obj += Y
    m.setObjective(obj, GRB.MAXIMIZE)
    
    # Ajout des contraintes
    for i in range(N):
        m.addConstr(gp.quicksum(X[i]) == 1)
        m.addConstr(gp.quicksum(X.transpose()[i]) == 1)
        for t in range(N):
            m.addConstr((X[i][t] == 1) >> (Y <= X[i][t] * U[i][t]))
    
    # Résolution        
    m.optimize()
    
    res = [X[i][j].X * U[i][j] for i in range(N) for j in range(N) if X[i][j].X > 0]
    logging.info("affectation obtenue : " + str(res) + "valeur objectif = " + str(m.ObjVal))
    logging.info("<------fin appel question_4_indicator------>")
    return res
    
def question_4(N, eps: float = 0.01, V=None, lower=0, upper=20):
    """Maximisation de la fonction objectif f de la question 4. Retourne l'affectation optimale obtenue.

    Args:
        eps (float): facteur de la somme des satisfaction
        N (int): taille de la matrice d'utilités
        V (int array): matrice d'utilités. Si non renseignée elle est générée aléatoirement.
        lower (int): borne inférieure si ``V`` non renseignée
        upper (int): borne supérieure si ``V`` non renseignée

    Returns:
        array
    """
    
    if V is not None:
        U = V
    else:
        U = np.random.randint(lower, upper, size=(N,N))
    
    logging.info(">------résolution question_4------<")
    logging.info("U matrix\n" + str(U))
    
    # Création du modèle
    m = gp.Model("question4")
    
    # Ajout des variables
    X = np.array([[m.addVar(vtype=GRB.BINARY) for j in range(N)] for i in range(N)])
    Y = m.addVar(vtype = GRB.INTEGER)
    m.update()
    
    # Ajout de la fonction objectif
    obj = gp.LinExpr()
    obj = 0
    for i in range(N):
        for j in range(N):
            obj += eps * X[i][j] * U[i][j]     
    obj += Y
    m.setObjective(obj, GRB.MAXIMIZE)
    
    # Ajout des contraintes
    for i in range(N):
        m.addConstr(gp.quicksum(X[i]) == 1)
        m.addConstr(gp.quicksum(X.transpose()[i]) == 1)
        m.addConstr(Y <= gp.quicksum(X[i][j]*U[i][j] for j in range(N)))
        
    # Résolution
    m.optimize()
    
    res = [X[i][j].X * U[i][j] for i in range(N) for j in range(N) if X[i][j].X > 0]
    logging.info("affectation obtenue : " + str(res) + "valeur objectif = " + str(m.ObjVal))
    logging.info("<------fin appel question_4------>")
    return res

def question_5(N,lb=0,hb=20,V=None):
    if V is not None:
        U = V
    else:
        U = np.random.randint(lb,hb,size=(N,N))
    logging.info(">---------résolution question_5---------<")
    logging.info("U matrix\n" + str(U.transpose()))
    
    # Création du modèle
    m = gp.Model("question5")
    
    # Ajout des variables
    X = np.array([[m.addVar(vtype=GRB.BINARY) for j in range(N)] for i in range(N)])
    Y = m.addVar(vtype = GRB.INTEGER)
    m.update()
    
    # Ajout de la fonction objectif
    m.setObjective(Y, GRB.MINIMIZE)
    
    # Ajout des contraintes
    for i in range(N):
        m.addConstr(gp.quicksum(X[i]) == 1)
        m.addConstr(gp.quicksum(X.transpose()[i]) == 1)
        m.addConstr(Y >= np.max(U[i]) - gp.quicksum(X[i][j] * U[i][j] for j in range(N)))
        m.addConstr(Y >= gp.quicksum(X[i][j] * U[i][j] for j in range(N)) - np.max(U[i]))
    
    # Résolution
    m.optimize()
    
    res = [X[i][j].X * U[i][j] for i in range(N) for j in range(N) if X[i][j].X > 0]
    logging.info("    affectation obtenue : " + str(res) + " ObjVal = " + str(m.ObjVal))
    logging.info("<---------fin appel question_5--------->")
    return res

    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("")
    
    globals()[argv[1]](int(argv[2]), lower=int(argv[3]), upper=int(argv[4]))
    
    logging.info("\n")
