#!/usr/local/bin/python
# coding:utf-8
import os
from keras.layers import Dense, Embedding, Merge, Flatten, RepeatVector, TimeDistributed, Concatenate
import numpy as np
from keras.models import Sequential
from keras.utils import np_utils
from keras.callbacks import TensorBoard
from keras.layers import Dropout
import csv

with open('enrollment_list.csv','rb') as fa:
	reader = csv.reader(fa)
	enrollment = list(reader)
	length1 = len(enrollment)
	enrollment_id = []
	for i in range(1,length1):
		enrollment_id.append(enrollment[i][0])

with open('train_label.csv','rb') as fa:
	reader = csv.reader(fa)
	GT = list(reader)
	length2 = len(GT)
	Y_train = []
	for i in range(1,length2):
		Y_train.append(int(GT[i][1]))

with open('train_data.csv','rb') as fa:
	reader = csv.reader(fa)
	traindate = list(reader)
	length2 = len(traindate)
	X_train = []
	for i in range(1,length2):

		p = []
		q = traindate[i][1].split()
		for each in range(len(q)):
			p.append(int(q[each]))
		X_train.append(p)

with open('test_data.csv','rb') as fa:
	reader = csv.reader(fa)
	testdata = list(reader)
	length2 = len(testdata)
	X_test = []
	for i in range(1,length2):

		p = []
		q = testdata[i][1].split()
		for each in range(len(q)):
			p.append(int(q[each]))
		X_test.append(p)

X_test = np.array(X_test)
X_env = np.array(X_train[41327:72325])
X_train = np.array(X_train)
Y_env = np_utils.to_categorical(Y_train[41327:72325],2)
Y_train = np_utils.to_categorical(Y_train,2)

model = Sequential()

model.add(Dense(200, input_dim=6, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(200, input_dim=200, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(200, input_dim=200, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(200, input_dim=200, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(200, input_dim=200, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(2, activation='softmax'))
tensorboard = TensorBoard(log_dir='log', histogram_freq=0, write_graph=True, write_images=True)

print(model.summary())

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
his = model.fit(X_train, Y_train, validation_data=(X_env, Y_env),epochs=10, batch_size=100, verbose=2,callbacks=[tensorboard])

scores = model.evaluate(X_env, Y_env, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))

yp = model.predict(X_test)

data = []
for x in range(0,len(yp)):
	data.append([str(x+72326),str(yp[x][1])])


fileHearder = ["enrollment_id", "dropout_prob"]

csvFile = open("classification2.csv", "w")
writer = csv.writer(csvFile)
writer.writerow(fileHearder)
writer.writerows(data)

