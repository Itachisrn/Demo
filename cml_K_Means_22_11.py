import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt

# from scipy.special import label
from sklearn.cluster import KMeans

#Read the data
data = pd.read_csv("D:/demoData_2.csv")
X = data.iloc[:,[3, 4]].values
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,init='k-means++', max_iter=300, n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Applying K-Means
kmeans = KMeans(n_clusters= 3, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)

#Visiualizing the data
plt.scatter(X[y_kmeans == 0,0], X[y_kmeans == 0,1], s=100, c='red', label='Çluster_1')
plt.scatter(X[y_kmeans == 1,0], X[y_kmeans == 1,1], s=100, c='green', label='Çluster_2')
plt.scatter(X[y_kmeans == 2,0], X[y_kmeans == 2,1], s=100, c='black', label='Çluster_3')
plt.scatter(X[y_kmeans == 3,0], X[y_kmeans == 3,1], s=100, c='cyan', label='Çluster_4')
plt.scatter(X[y_kmeans == 4,0], X[y_kmeans == 4,1], s=100, c='magenta', label='Çluster_5')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'Yellow', label='Centroids')
plt.title('The final clustered data')
plt.xlabel('The X-axis data')
plt.ylabel('The Y-axis data')
plt.legend()
plt.show()


