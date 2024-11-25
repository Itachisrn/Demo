import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:/house_rent.csv")
x = dataset.iloc[:, :].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, :])
x[:, :] = imputer.transform(x[:, :])
print(x)