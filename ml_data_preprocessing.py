import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:\\New folder (2)\\Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
## print(x)
## print(y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
## print(x)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
print("x")
print(x)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print("\n y")
print(y)

## Splitting the dataset into the Training set and Test set 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
## print(x_train)
## print(x_test)
print("\n y_train")
print(y_train)
print("\n y_test")
print(y_test)

##  Feature Scaling 

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])
print("\n x_train")
print(x_train)
print("\n x_test")
print(x_test)