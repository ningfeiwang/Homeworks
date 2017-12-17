#!/usr/local/bin/python
# coding:utf-8

from PIL import Image
import os
import numpy as np
import cv2
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.callbacks import TensorBoard
from keras.layers import Dropout

def get_name(filepath):
	name_list = os.listdir(filepath)
	return name_list

def get_img():
	all_dir = get_name(path)
	X_train = []
	y_train = []
	X_test = []
	y_test = []
	a = []
	for each_dir in all_dir:
		if not os.path.isdir(os.path.join(path,each_dir)):
			continue
		label = 0
		all_img_dir = get_name(os.path.join(path,each_dir))
		for each_img_dir in all_img_dir:
			if not os.path.isdir(os.path.join(path,each_dir,each_img_dir)):
				continue
			all_img = get_name(os.path.join(path,each_dir,each_img_dir))
			for each_img in all_img:
				if not os.path.isfile(os.path.join(path,each_dir,each_img_dir,each_img)):
					continue
				print path,each_dir,each_img_dir,each_img

				if 'gif' in each_img:
					a = each_img.split('.')
					each_img1 = each_img
					each_img = a[0]+'.png'
					Image.open(os.path.join(path,each_dir,each_img_dir,each_img1)).save(os.path.join(path,each_dir,each_img_dir,each_img))
				img = cv2.imread(os.path.join(path,each_dir,each_img_dir,each_img))
				# print each_img
				resized_img = cv2.resize(img, (height, width)).astype('float32')
				img = resized_img.reshape(1, height*width*3).astype('float32')
				if 'train' in each_dir:
					X_train.append(img)
					y_train.append(label)
				elif 'test' in each_dir:
					X_test.append(img)
					y_test.append(label)
			if len(all_img_dir)>0:
				label+=1
	X_train = np.concatenate(X_train)
	X_test = np.concatenate(X_test)
	y_train = np.array(y_train)
	y_test = np.array(y_test)
	return (X_train,y_train),(X_test,y_test)

def main():
	global path, width, height
	
	path = '***********'
	# p=0
	width=30
	height=30
	list_his=[]
	loss=[]
	# while p<=600:

	(X_train,y_train),(X_test,y_test) = get_img()

	X_train = X_train / 255
	X_test = X_test / 255
	num_classes=5

	# one hot encode outputs
	y_train = np_utils.to_categorical(y_train,num_classes)
	y_test = np_utils.to_categorical(y_test,num_classes)

	# design model
	model = Sequential()
	model.add(Dense(400, input_dim=width*height*3, activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(300, input_dim=400, activation='relu'))
	model.add(Dense(num_classes, activation='softmax'))
	# tensorboard = TensorBoard(log_dir='log', histogram_freq=0, write_graph=True, write_images=True)

	# print out summary of the model
	print(model.summary())

	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	# Fit the model
	his = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=30, batch_size=70, verbose=2)
	# Final evaluation of the model
	# print (max(his.history['val_acc']))
	# list_his.append(max(his.history['val_acc']))
	# loss.append(min(his.history['val_loss']))
	scores = model.evaluate(X_test, y_test, verbose=0)
	print("Baseline Error: %.2f%%" % (100-scores[1]*100))
	# print list_his
	# print loss

if __name__ == '__main__':
	main()