# CS620
# HW6
# @author: Sai Hymavathi Majeti


import matplotlib.pyplot as plt  
import pandas as pd  
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from numpy import mean
# K Neighbors classifier
from sklearn.neighbors import KNeighborsClassifier 


#Use  a  list  of  numbers  in  the  range  of  1-100,  and  filter  to  generate  a  list  called “neighbors” which include only odd numbersin that range.
listOfNum = list(range(1, 100))
neighbors = []
for num in listOfNum:
    if num % 2 != 0:
        neighbors.append(num)
#print(neighbors)


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class'] # Assign column names to the dataset
dataset = pd.read_csv(url, names=names) # Read dataset to pandas dataframe
X = dataset.iloc[:, :-1].values # the feature set 'sepal-length', 'sepal-width', 'petal-length', 'petal-width'
y = dataset.iloc[:, 4].values # 'Class'

# percentage split 80% training and 20% testing
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  

accuracy = [] #list of avg_accuracy for each 10 - fold

for neighbor in neighbors: 
    classifier = KNeighborsClassifier(n_neighbors = neighbor) #knn classifier
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    #Use  “cross_val_score”function and specify scoring='accuracy' to generate accuracy from each 10-fold cross validation for the list of “neighbors”. 
    cv_score = cross_val_score(classifier, X, y, scoring = 'accuracy', cv = 10)
    avg_accuracy = mean(cv_score)
    accuracy.append(avg_accuracy)

    # display the classificaiton report, confusion matrix and accuracy of the classifier
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(confusion_matrix(y_test, y_pred))  
    print(classification_report(y_test, y_pred)) 
    print(accuracy_score(y_test,y_pred))


#Perform 10-fold  cross validation and  generate a list called “MSE”(misclassification error) by using the equation, MSE= (1-accuracy). 
#Note: Here the  accuracy is a list that  contains the average accuracy of  each 10-fold cross validation (per each neighbors).
MSE = [1 - a for a in accuracy] #list of MSEs for each fold

#Generate a Plot “neighbors” vs “MSE” and 
#also find and print the optimal K using the “MSE” list. Include the plot as a figure in your pdf.
MSE_index = MSE.index(min(MSE))
print(MSE_index)

optimal_K = neighbors[MSE_index]  
#retrieving the neighbor using the index value of the minimum-MSE value 
print('Optimal K is ' + str(optimal_K))

#plot
plt.plot(neighbors, MSE)
plt.xlabel('neighbors')
plt.ylabel('MSE')
plt.title('neighbors vs MSE')
plt.show()
