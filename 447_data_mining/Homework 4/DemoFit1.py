
# library for plotting
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

import csv


X_train = []
Y_train = []
with open('train.csv','rb') as fa:
	reader = csv.reader(fa)
	train_list = list(reader)
	length1 = len(train_list)
	for i in range(1,length1):
		X_train.append(train_list[i][0:11])
		Y_train.append(train_list[i][11])
	print X_train[1]
	print Y_train[1]

X_test = []
Y_test = []
with open('test.csv','rb') as fb:
	reader = csv.reader(fb)
	test_list = list(reader)
	length2 = len(test_list)
	for j in range(1,length2):
		X_test.append(test_list[j][0:11])
		Y_test.append(test_list[j][11])

errorTrain = []
errorTest = []
K = []
for z in range(1,129):
	neighbor = z
	K.append(z)
	neighborK = KNeighborsClassifier(n_neighbors = neighbor)
	neighborK.fit(X_train,Y_train)
	neighborK.predict(X_test)
	score1 = neighborK.score(X_train,Y_train,sample_weight = None)
	score2 = neighborK.score(X_test,Y_test,sample_weight = None)
	errorTrain.append(1 - score1)
	errorTest.append(1 - score2)



plt.xlabel('k')
plt.ylabel('average error')
plt.plot(K, errorTrain)
plt.plot(K, errorTest)
plt.grid(True)
plt.show()

