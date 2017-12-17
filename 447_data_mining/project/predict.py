# data mining data analysis
# -*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import numpy as np
import model
from sklearn.svm import SVC
import csv

with open('train_label.csv','rb') as fa:
	reader = csv.reader(fa)
	GT = list(reader)
	dropoutP = []
	for i in range(1,len(GT)):
		dropoutP.append(GT[i][1])
Y_train = dropoutP

j = 0
with open('data.csv','rb') as fa:
	reader = csv.reader(fa)
	traindate = list(reader)
	length2 = len(traindate)
	X_train = []
	X_test = []
	for i in range(1,length2):

		p = []
		q = traindate[i][1].split()
		for each in range(len(q)):
			p.append(int(q[each]))
		if j <= 72324:
			X_train.append(p)
			j += 1
		else:
			X_test.append(p)
			j += 1

instance= SVC()
ins = instance.fit(X_train,Y_train)
score = ins.score(X_train,Y_train)
res = ins.predict_proba(X_test)

result = []
for mm in range(0,len(res)):
	result.append(res[mm][1])

print result[0:20]
data = []
for x in range(0,len(result)):
	data.append([str(x+72326),str(result[x])])


fileHearder = ["enrollment_id", "dropout_prob"]

csvFile = open("classification_svm.csv", "w")
writer = csv.writer(csvFile)
writer.writerow(fileHearder)
writer.writerows(data)


