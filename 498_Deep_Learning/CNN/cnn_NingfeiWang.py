import numpy
from keras.datasets import mnist
from keras.models import Sequential,Model 
from keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image 
from keras import backend as K
from PIL import Image
import os
import numpy as np
import cv2
from keras.utils import np_utils
from keras.callbacks import TensorBoard
from keras.layers import Dropout
# from keras.layers import Input
from keras import regularizers


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
			# print all_img
			for each_img in all_img:
				if not os.path.isfile(os.path.join(path,each_dir,each_img_dir,each_img)):
					continue
				# print path,each_dir,each_img

				if 'gif' in each_img:
					continue
					# a = each_img.split('.')
					# each_img1 = each_img
					# each_img = a[0]+'.png'
					# Image.open(os.path.join(path,each_dir,each_img_dir,each_img1)).save(os.path.join(path,each_dir,each_img_dir,each_img))
				img = cv2.imread(os.path.join(path,each_dir,each_img_dir,each_img))
				# print each_img
				resized_img = cv2.resize(img, (height, width)).astype('float32')
				img = resized_img.reshape(1, height, width,3).astype('float32')
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
# load data
# (X_train, y_train), (X_test, y_test) = mnist.load_data()
# reshape to be [samples][pixels][width][height]
	global path, width, height
	
	path = '/Users/wangningfei/Desktop/Lehigh_Fall2017/CSE498/data'
	p=0
	q=0
	width=140
	height=140
	# X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
	# X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')
	(X_train,y_train),(X_test,y_test) = get_img()
	# normalize inputs from 0-255 to 0-1
	X_train = X_train / 255
	X_test = X_test / 255
	# one hot encode outputs
	y_train = np_utils.to_categorical(y_train)
	y_test = np_utils.to_categorical(y_test)
	num_classes = 5

	# create model
	
	# input_tensor = Input(shape=(height, width, 3))
	# create model
	# while p<20:
	model = Sequential()

	kernel_regularizer=regularizers.l2(0.01)

	model.add(Conv2D(32, (3, 3), input_shape=(140, 140, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Conv2D(32, (5, 5), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Conv2D(32, (5, 5), activation='relu'))
	model.add(Conv2D(64, (5, 5), activation='relu'))

	# model.add(Conv2D(32, (5, 5), activation='relu'))
	# model.add(MaxPooling2D(pool_size=(2, 2)))
	# model.add(Conv2D(64, (5, 5), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	# model.add(Conv2D(32, (5, 5), activation='relu'))
	# model.add(MaxPooling2D(pool_size=(2, 2)))
	# model.add(Dropout(0.2))

	model.add(Flatten())

	model.add(Dense(32, activation='relu'))
	model.add(Dropout(0.2))

	model.add(Dense(100, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(5, activation='softmax'))
	# k='log'+str(q)
	tensorboard = TensorBoard(log_dir='log', histogram_freq=0, write_graph=True, write_images=True)
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	# Fit the model
	model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32, verbose=2, callbacks=[tensorboard])
	q+=1
	p+=4
	# Final evaluation of the model

	scores = model.evaluate(X_test, y_test, verbose=0)

	print("Baseline Error: %.2f%%" % (100-scores[1]*100))   
if __name__ == '__main__':
	main()