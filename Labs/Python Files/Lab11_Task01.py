print("Muhammad Umair - 12093")
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm

data = pd.read_csv(r'iris_data.csv')
print(data.head())
x=data.drop('species','columns')
#print(x.head())
y=data['species']
#print(Y.head())

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
scaler = StandardScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
#print(x_train)
#print(x_test)

from sklearn.svm import SVC
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(y_pred)


from sklearn.metrics import confusion_matrix, classification_report,accuracy_score
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print("Accuracy:",accuracy_score(y_test, y_pred))