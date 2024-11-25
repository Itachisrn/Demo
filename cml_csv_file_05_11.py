import pandas as pd
import numpy as np
#import csv
#with open("D:/Salary_Data.csv", mode= 'r')as file:
    #csvFile = csv.DictReader(file)
    #for lines in csvFile:
        #print(lines)
#csvFile = pd.read_csv("D:/Salary_Data.csv")
#print(csvFile)

#data=pd.read_excel("D:/Book1.xlsx")
#print(data)

arr = np.array([[5,8,9]
                [9,2,77]
                [55,2,66]])
d=np.savetxt("D:/da.csv", arr, delimiter=",")
print(d)

#df = pd.read_csv("D:/da.csv", header=None)

# Print the DataFrame
#print(df)

#matrix = np.array([[1, 2], [3, 4]])
#print("Matrix:")
#print(matrix)