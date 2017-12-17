# data mining data analysis
# -*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import numpy as np
import model
import csv
from sklearn.decomposition import PCA

def pca_list(x, var):
	res = []
	for i in x:
		cur = []
		for j in range(0,10):
			if var[j] > 0.01:
				cur.append(i[j])
		res.append(cur)
	return res

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

X_train = np.array(X_train)
X_test = np.array(X_test)

var = PCA(n_components=10, copy=True, 
	whiten=False, svd_solver='auto', 
	tol=0.0, iterated_power='auto', random_state=None).fit(X_train).explained_variance_ratio_
print var

X_train = pca_list(X_train,var)
X_test = pca_list(X_test, var)



