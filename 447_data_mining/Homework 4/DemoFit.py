
# library for plotting
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from scipy.interpolate import spline
import csv

def read_csv(filename):
	x = []
	y = []
	with open(filename, 'r') as read_csv:
		reader = csv.reader(read_csv)
		train_list = list(reader)
		for i in range(1,len(train_list)):
			x.append(train_list[i][0:-1])
			y.append(train_list[i][-1])
		return (x, y)

(x_train, y_train) = read_csv('train.csv')
(x_test, y_test) = read_csv('test.csv')

train_error = []
test_error = []
K = []
for k in range(1,129):
	K.append(k)
	neighborK = KNeighborsClassifier(n_neighbors = k)
	neighborK.fit(x_train, y_train)
	neighborK.predict(x_test)
	train_score = neighborK.score(x_train,y_train,sample_weight = None)
	test_score = neighborK.score(x_test,y_test,sample_weight = None)
	train_error.append(1 - train_score)
	test_error.append(1 - test_score)

plt.title('K-Error')
plt.xlabel('Number of Neighbors')
plt.ylabel('Average Error')
p1 = plt.plot(K, train_error, color = 'b', label = 'train error')
p2 = plt.plot(K, test_error, color = 'r', label = 'test error')
plt.grid(True)
plt.legend(loc = 4)
plt.show()