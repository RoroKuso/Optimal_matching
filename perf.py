"""Bibliothèque pour les tests de performances"""
import gurobipy as gp
from gurobipy import GRB
import numpy as np
from typing import Tuple
import logging
import time
from sys import argv, stdout
from lib import *
    
def perf_tests(fonction, lower: int = 0, upper: int = 20, average_iter: int = 10, size_lim: int = 100, step: int = 5):
    """Calcul de performances pour la fonction ``question_5``

    Args:
        lower (int): borne inférieure des valeurs des utilités
        upper (int): borne supérieure des valeurs des utilités
        average_iter (int, optional): nombre d'itérations par instance. Vaut 10 par défaut.
        size_lim (int, optional): taille maximale des matrices. Vaut 15 par défaut.
        step (int, optional): saut pour la taille des matrices. Vaut 5 par défaut.
    """
    logging.info(f">---------Tests de performances {fonction.__name__}---------<")
    
    for N in range(step, size_lim+1, step):
        start = time.time()
        
        for i in range(average_iter):
            U = np.random.randint(lower, upper, size=(N,N))
            logging.disable(logging.INFO) # pour éviter les affichages de la fonction
            fonction(N,V=U)
            
        logging.disable(logging.NOTSET) # réactivation des affichages
        elapsed = (time.time() - start) / average_iter
        logging.info(f"    |(size, avrg time) = ({N},{elapsed:.3f})")
    
    logging.info(f"<---------fin des tests {fonction.__name__}--------->")
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("")
    
    perf_tests(globals()[argv[1]], int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6]))
    
    logging.info("\n")
