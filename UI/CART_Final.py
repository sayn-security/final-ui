#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd  
import numpy as np   
from sklearn.model_selection import train_test_split  
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils import shuffle
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from pandas import ExcelFile
from sklearn.metrics import accuracy_score
#from __future__ import print_function
import time
import warnings
from sklearn.externals.six import StringIO  
#from IPython.display import Image  
from sklearn.tree import export_graphviz
#import pydotplus
from sklearn.preprocessing import LabelEncoder
import decimal
def machineLearning():
    start = time.time()


    warnings.filterwarnings('ignore') 


    # Excel file name.
    fileName = "bigDataFile.xlsx"
    fn = "DataCollected.xlsx"
    data1 = pd.read_excel(fn, sheetname='Sheet1')
    data = pd.read_excel(fileName, sheetname='Sheet1')
    #data = shuffle(data)
    X = data.drop(['subject'], axis=1)
    y = data['subject']
    X1 = data1.drop(["subject"], axis=1)
    #print (X1)
    y1 = data1["subject"]
    labelencoder = LabelEncoder()
    #print(y1)
    # conver subject column to numirical value
    #y = labelencoder.fit_transform(data['subject'])
    #y1 = labelencoder.fit_transform(data1["subject"])
    # Divide data into training and test sets.
    # The train_test_split method that allows us to seamlessly divide data into training and test sets.
    #print(y1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=0)
    #X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0, random_state=1)
    clf = tree.DecisionTreeClassifier(criterion="gini", min_impurity_split=.1995)
    #print(clf.max_leaf_nodes)
    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)
    #print(X_test)
    #Predict the response for test dataset
    #print(clf.similarity_index())
    y_pred = clf.predict(X1)
    #print(clf.score(X1,y1))
    print(y_pred)
    #print(clf.decision_path(X, check_input=True))
    #print(clf.decision_path)
    # Model Accuracy, how often is the classifier correct?
    '''print("Classification_report\n",metrics.classification_report(y1, y_pred))
    print("Confusin Matrix")
    print(metrics.confusion_matrix(y1, y_pred))
    print("Accuracy:",metrics.accuracy_score(y1, y_pred))'''
    
    '''dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_pdf("intersting.pdf")'''
    
    end = time.time()
    print("Runtime:",end - start)
    return y_pred

def main():
    print(machineLearning())
    print("done")
    
if __name__ == "__main__":
    main()

