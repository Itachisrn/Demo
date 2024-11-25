import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:/demoData.csv")

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values
#z = dataset.iloc[:2, :3].values

from sklearn.impute import SimpleImputer
#imp = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imp = SimpleImputer(missing_values = np.nan, strategy = 'median')
imp = imp.fit(X[:, 1:4])
X[:, 1:4] = imp.fit_transform(X[:, 1:4])

print("X")
print(X)
#print("\nY")
#print(Y)

#print(z)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

print(X_train)
print(X_test)
