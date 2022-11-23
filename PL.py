import gurobipy as gp
from gurobipy import GRB
import numpy as np
from typing import Tuple
import logging
import time

def question_1(lower: int, upper: int, average_iter: int = 10, size_lim: int = 15, step: int = 5):
    logging.info("----------------------------")
    logging.info("Running tests for question_1")
    for N in range(step, size_lim+1, step):
        logging.info("---->Starting N = {}".format(N))
        start = time.time()
        #| Average of ``average_iter`` iterations
        total_satisfaction = np.zeros(N)
        for i in range(average_iter):
            with gp.Env(empty=True) as env:
                
                env.setParam('OutputFlag', 0)
                env.start()
                with gp.Model(env=env) as m:
                    U = np.random.randint(lower, upper, size=(N, N))
                    X = m.addMVar((N,N), vtype=GRB.BINARY)
                    m.setObjective(gp.quicksum([gp.quicksum(X[j]*U[j]) for j in range(N)])/N, GRB.MAXIMIZE)
                    m.addConstrs(gp.quicksum(X[j]) == 1 for j in range(N))
                    m.addConstrs(gp.quicksum(X.transpose()[j]) == 1 for j in range(N))
                    m.optimize(callback=None)
                    total_satisfaction += [U[i][np.argmax(X[i])] for i in range(N)]
        logging.info("    | Ecart type satisfaction : {}".format(np.nanstd(total_satisfaction)))
        elapsed = (time.time() - start)/average_iter
        logging.info(f"    | Average time = {elapsed:.4f} s")
    logging.info("Finished tests for question_1")
    logging.info("----------------------------")
        

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("")
    question_1(0, 20, size_lim=100)
    logging.info("\n")