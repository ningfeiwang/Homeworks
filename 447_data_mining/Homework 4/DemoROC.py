
# library for plotting
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.metrics import roc_curve
import csv

def read_csv(filename):
	x = []
	y = []
	with open(filename, 'r') as read_csv:
		reader = csv.reader(read_csv)
		train_list = list(reader)
		for i in range(1,len(train_list)):
			x.append(train_list[i][0:-1])
			y.append(int(train_list[i][-1]))
		return (x, y)

(x_train, y_train) = read_csv('train.csv')
(x_test, y_test) = read_csv('test.csv')

neighborK = KNeighborsClassifier(n_neighbors = 65)
neighborK.fit(x_train, y_train)
predict_proba = neighborK.predict_proba(x_test)

proba = []

for i in range(0,len(predict_proba)):
	proba.append(predict_proba[i][1])

x = np.array(proba)
y = np.array(y_test)
fpr, tpr, threshold = roc_curve(y, x, pos_label = 1)

plt.title('ROC')
plt.plot(fpr, tpr, label = 'KNN Classifier', color = 'r')
plt.plot([0,1], [0,1], label = 'Random Guess', color = 'b')
plt.legend(loc="lower right")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.grid(True)
plt.show()