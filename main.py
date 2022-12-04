import gurobipy as gp
from gurobipy import GRB
import numpy as np
from lib import *
from perf import *



if __name__ == '__main__':
    """Pour éxécuter les fonctions avec des matrices spécifiques
    """
    logging.basicConfig(level=logging.INFO)
    
    U = np.array([[12,20,6,5,8],
                  [5,12,6,8,5],
                  [8,5,11,5,6],
                  [6,8,6,11,5],
                  [5,6,8,7,7]])
    
    question_1(5, V=U)
    question_4(5, V=U)
    question_5(5, V=U)
