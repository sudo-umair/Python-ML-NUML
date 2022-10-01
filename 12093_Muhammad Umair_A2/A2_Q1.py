import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(r'E:\NUML\Semester Data\Semester 5\AI\AI Lab\12093_Muhammad Umair_A2\dataR2.csv')
print(data.head())

print("\nCancer data set dimensions : {}".format(data.shape))
x = data.drop('Classification', 'columns')
y = data['Classification']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=5)

scaler = StandardScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)

from sklearn.metrics import  confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion= 'entropy', random_state=0)
classifier.fit(x_train, y_train)
y_pred_dt = classifier.predict(x_test)
print('Accuracy: ',accuracy_score(y_test, y_pred_dt))

cm = confusion_matrix(y_test, y_pred_dt)
print('Confusion Matrix: \n',cm)
plt.title("Heatmap of Confusion Matrix", fontsize = 15)
sns.heatmap(cm, annot= True)
plt.show()

print(classification_report(y_test, y_pred_dt))