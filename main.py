import gurobipy as gp
from gurobipy import GRB
import numpy as np

V = np.array([[12, 20, 6, 5, 8],
            [5,12,6,8,5],
            [8,5,11,5,6],
            [6,8,6,11,5],
            [5,6,8,7,7]])

# Create a new model
m = gp.Model("test")

X = m.addMVar((5,5),vtype=GRB.BINARY)

m.setObjective(gp.quicksum([gp.quicksum(X[i]*V[i]) for i in range(5)])/5., GRB.MAXIMIZE)

m.addConstrs(gp.quicksum(X[i]) == 1 for i in range(5))
m.addConstrs(gp.quicksum(X.transpose()[i]) == 1 for i in range(5))

m.optimize()
print(X.X)

print ( "Obj : % g " % m.ObjVal )

