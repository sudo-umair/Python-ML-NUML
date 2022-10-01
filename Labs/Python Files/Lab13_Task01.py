print("Muhammad Umair - 12093")

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'iris_data_2a.csv') 
data1 = data.drop(['petal_length','petal_width','species'],'columns')
print(data1.head())

from sklearn.cluster import KMeans
kmean = KMeans(n_clusters=3) 
kmean.fit(data1) 
print(kmean.labels_)
centers = kmean.cluster_centers_ 
print(centers)
data1['classes'] = kmean.labels_ 

print(data1.head())
df0 = data1[data1['classes']==0]
df1 = data1[data1['classes']==1] 
df2 = data1[data1['classes']==2]

plt.scatter(df0['sepal_length'], df0['sepal_width'],color = 'red') 
plt.scatter(df1['sepal_length'], df1['sepal_width'],color = 'blue') 
plt.scatter(df2['sepal_length'], df2['sepal_width'],color = 'lightblue')

plt.scatter(centers[:,0],centers[:,1], marker='*', color ='purple', linewidths=10) 

plt.xlabel('sepal_length')
plt.ylabel('sepal_width') 
plt.title("IRIS")
plt.show()