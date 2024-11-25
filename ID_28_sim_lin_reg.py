import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:/house_rent.csv")
X = dataset.iloc[:, :-1].values  
y = dataset.iloc[:, -1].values    
X = X[:, 0].reshape(-1, 1)  

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X = imputer.fit_transform(X)

imputer_y = SimpleImputer(missing_values=np.nan, strategy='mean')
y = imputer_y.fit_transform(y.reshape(-1, 1)).flatten() 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('House Rent vs Feature (Training set)')
plt.xlabel('Feature')  
plt.ylabel('House Rent')
plt.show()

plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('House Rent vs Feature (Test set)')
plt.xlabel('Feature')  
plt.ylabel('House Rent')
plt.show()