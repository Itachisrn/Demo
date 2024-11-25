import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("D:/Salary_dataset.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

##print(dataset)

print("x_train")
print(x_train)

print("\nx_test")
print(x_test)

print("y_train")
print(y_train)

print("\ny_test")
print(y_test)

from sklearn.linear_model import LinearRegression
# Fitting simple linear regression to the Training set

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_predict = regressor.predict(x_test)
print("\n The Original value", y_test)
print("\n The Predicted value", y_predict)


## Visualising the Training set results

plt.scatter(x_train, y_train, color = 'green')
plt.plot(x_train, regressor.predict(x_train), color = 'red')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

## Visualising the Test set results

plt.scatter(x_test, y_test, color = 'green')
plt.plot(x_train, regressor.predict(x_train), color = 'red')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
