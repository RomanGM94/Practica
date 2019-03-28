from mlxtend.data import iris_data
from mlxtend.plotting import plot_decision_regions
from mlxtend.classifier import Perceptron
import matplotlib.pyplot as plt
import numpy as np

# Loading Data

X, y = iris_data()
X = X[:, [0, 3]] # sepal length and petal width
#print(X)
X = X[0:100] # class 0 and class 1
print(X.shape)
y = y[0:100] # class 0 and class 1
print(y.shape)

# standardize
X[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()
print(X)

# Rosenblatt Perceptron

ppn = Perceptron(epochs=5, 
                 eta=0.05, 
                 random_seed=0,
                 print_progress=3)
ppn.fit(X, y)
x2=np.array([[0.35866332 ,0.91401319],[5.7,1.3]])
print("\n",ppn.predict(x2))