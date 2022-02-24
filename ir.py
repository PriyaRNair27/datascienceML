import pandas as pd
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data=load_iris()
data.data.shape
print('classes to predict:',data.target_names)
print('features:',data.feature_names)
x=data.data
y=data.target
print(x.shape,x.shape)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=50,test_size=0.25)
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print('Accuracy  on train data using gini:',accuracy_score(y_true=y_train,y_pred=classifier.predict(x_train)))
print('Accuracy  on test data using gini:',accuracy_score(y_true=y_test,y_pred=y_pred))
classifier_entropy=DecisionTreeClassifier(criterion='entropy')
classifier_entropy.fit(x_train,y_train)
y_pred_entropy=classifier_entropy.predict(x_test)
print('Accuracy  on train data using entropy:',accuracy_score(y_true=y_train,y_pred=classifier_entropy.predict(x_train)))
print('Accuracy  on test data using entropy:',accuracy_score(y_true=y_test,y_pred=y_pred_entropy))
classifier_entropy1=DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
classifier_entropy1.fit(x_train,y_train)
y_pred_entropy1=classifier_entropy1.predict(x_test)
print('Accuracy  on train data using entropy:',accuracy_score(y_true=y_train,y_pred=classifier_entropy1.predict(x_train)))
print('Accuracy  on test data using entropy:',accuracy_score(y_true=y_test,y_pred=y_pred_entropy1))