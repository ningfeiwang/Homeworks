# data mining data analysis
# -*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import numpy as np
import model
# from sklearn.neural_network import MLPClassifier
# from sklearn.naive_bayes import BernoulliNB
# from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
# from sklearn import ensemble
import csv

with open('enrollment_list.csv','rb') as fa:
	reader = csv.reader(fa)
	enrollment = list(reader)
	enrollment_id = []
	courseid = []
	course =[]
	for i in range(1,len(enrollment)):
		enrollment_id.append(enrollment[i][0])		
		courseid.append(enrollment[i][2])
		if enrollment[i][2] not in course:
			course.append(enrollment[i][2])
	index = []
	for lo in range(0,len(course)):
		index.append(lo)
	courseidfinal = []
	for ll in range(0,len(courseid)):
		ind = course.index(courseid[ll])
		courseidfinal.append(index[ind])
	print course

with open('train_label.csv','rb') as fa:
	reader = csv.reader(fa)
	GT = list(reader)
	dropoutP = []
	for i in range(1,len(GT)):
		dropoutP.append(GT[i][1])

with open('activity_log.csv','rb') as fa:
	reader = csv.reader(fa)
	activity = list(reader)
	length3 = len(activity)
	print length3
	attrTime = [[] for z in range(120542)]
	attrState = [[] for z in range(120542)]
	count = 0
	i = 0
	while(i<length3-1):
		if(activity[i][0] != activity[i+1][0]):
			count += 1
		i += 1
		
		attrTime[count-1].append(activity[i][1])

		attrState[count-1].append(activity[i][2])

# problem - working on course assignments
# video - watching course videos.
# access - accessing other course objects except videos and assignments
# wiki - accessing the course wiki
# discussion - accessing the course forum
# navigation - navigating to other part of the course.
# page_close - closing the web page
attr = [[] for z in range(120542)] #times of every student operating
times = []
for stu in range(0,len(attrState)):
	length4 = len(attrState[stu])
	times.append(length4)
	problemT =0
	videoT =0
	accessT =0
	wikiT =0
	discussionT =0
	navigationT =0
	page_closeT =0
	for m in range(0,len(attrState[stu])):
		if(attrState[stu][m] == 'problem'):
			problemT += 1
		if(attrState[stu][m] == 'video'):
			videoT += 1
		if(attrState[stu][m] == 'access'):
			accessT += 1
		if(attrState[stu][m] == 'wiki'):
			wikiT += 1
		if(attrState[stu][m] == 'discussion'):
			discussionT += 1
		if(attrState[stu][m] == 'navigate'):
			navigationT += 1
		if(attrState[stu][m] == 'page_close'):
			page_closeT += 1
	attr[stu].append([problemT,videoT,accessT,wikiT,discussionT,navigationT,page_closeT])

Y_train = dropoutP

X_train = [[] for z in range(72325)]
X_test = [[] for z in range(48217)]

for i in range(0,72325):
	M = []
	M.append(courseidfinal[i])
	M.append(times[i])
	for j in range(0,len(attr[i][0])):	
		M.append(attr[i][0][j])
	for lii in range(0,len(M)):
		
		X_train[i].append(M[lii])

for i in range(72325,120542):
	M = []
	M.append(courseidfinal[i])
	M.append(times[i])
	for j in range(0,len(attr[i][0])):	
		M.append(attr[i][0][j])
	for lii in range(0,len(M)):
		X_test[i-72325].append(M[lii])

print Y_train[1:10]
print X_train[1:3]
print X_test[48216]
# print X_train.shape

# instance = BernoulliNB().fit(X_train,Y_train)
instance = SVC(C=1.0, kernel='sigmoid', degree=3, gamma='auto', 
	coef0=0.0, shrinking=True, probability=True, tol=0.001, 
	cache_size=200, class_weight=None, verbose=False, max_iter=-1, 
	decision_function_shape='ovr', random_state=None)
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


