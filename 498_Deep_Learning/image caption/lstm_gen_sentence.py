import os  
import cv2
import numpy as np 
import Image
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Sequential, Model
from keras.layers import LSTM, Dense, Embedding, Merge, Flatten, RepeatVector, TimeDistributed, Concatenate
# from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image as Image
from keras.preprocessing import sequence as Sequence
from keras.callbacks import TensorBoard, ModelCheckpoint
from keras.utils import plot_model, to_categorical
from collections import Counter

# all_dir = get_name(path)


IMAGE_ROOT = '**********'
TRAIN_CAPTION_PATH = '**********'
TEST_CAPTION_PATH = '**********'


SENTENCE_MAX_LENGTH = 100 # In this dataset, the maximum length is 84.
EMBEDDING_SIZE = 256


WORDS_PATH = 'words.txt'

SENTENCE_MAX_LENGTH = 100 # In this dataset, the maximum length is 84.

EMBEDDING_SIZE = 256

IMAGE_SIZE = 224






# print dic
# for k in range(0, len(dic.keys())):
# 	if dic[dic.keys()[k]] == '<SOS>':
# 		one_hot[k,k] = 1
# 		print k


# img = cv2.imread('/Users/wangningfei/Downloads/flickr30k_images/flickr30k_images/371903.jpg')

image = Image.img_to_array(Image.load_img('**********', target_size=(IMAGE_SIZE, IMAGE_SIZE, 3)))
			# print each_img
# resized_img = cv2.resize(img, (224,224)).astype('float32')
img = image.reshape(1, 224,224,3).astype('float32')
	

base_model = VGG16(weights='imagenet', include_top=True)
base_model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)
for layer in base_model.layers[1:]:
    layer.trainable = False

image_model = Sequential()
image_model.add(base_model)
image_model.add(Dense(EMBEDDING_SIZE, activation='relu'))
image_model.add(RepeatVector(SENTENCE_MAX_LENGTH))


# we use an Embedding layer to generate a good representation for captions.
language_model = Sequential()
# language_model.add(Embedding(voc_size, EMBEDDING_SIZE, input_length=SENTENCE_MAX_LENGTH))
language_model.add(LSTM(128, input_shape=(SENTENCE_MAX_LENGTH, 12503), return_sequences=True))
language_model.add(TimeDistributed(Dense(128)))


# after merging CNN feature (image) and embedded vector (caption), we feed them into a LSTM model
# at its end, we use a fully connected layer with softmax activation to convert the output into probability 
model = Sequential()
model.add(Merge([image_model, language_model], mode='concat'))
# model.add(Concatenate([image_model, language_model]))
model.add(LSTM(1000, return_sequences=True))
# model.add(Dense(voc_size, activation='softmax', name='final_output'))
model.add(TimeDistributed(Dense(12503, activation='softmax')))

# draw the model and save it to a file.

# plot_model(model, to_file='model.pdf', show_shapes=True)


# model = model
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.load_weights('**********')
# my_generator = Data_generator()

dic = {}
ppp = ' '
# one_hot = np.zeros([i,i])
i = 0
qq = []
xx = '<SOS>'
image = np.array(img)
with open('words.txt','r') as word:
	# content = [x.strip() for x in word.readlines()]
	# print(len(content))
	# print(content[:5])

	for x in word:
		i += 1
	one_hot = np.zeros([1,100,i])

i = 0
for k in range(0, 100):
	ppp = ' '
	i = 0
	qq.append(xx)
	# print my_generator
	with open('words.txt','r') as word:
		if xx == '<EOS>':
			break
		for x in word:
			dic[i] = x

			if k ==0: 
				if dic[i].split('\n')[0] == '<SOS>':
					print i
					print dic[i]
					one_hot[0,k,i] = 1
				i += 1
			else:
				if dic[i].split('\n')[0] == xx:
					one_hot[0,k,i] = 1
				i += 1


	one = np.array(one_hot)
	# print('one', one)
	

	# predict = model.predict({'input_1':preprocess_input(image),'lstm_1_input':one})
	# print(predict.shape)
	# max_index = np.argmax(predict, axis=-1)
	# print(max_index)
	# print(max_index.shape)

	# print('xincpder', predict.shape)

	# predict = model.predict_classes({'input_1':preprocess_input(image),'lstm_1_input':one})
	# print predict


	# break

	predict = model.predict_classes({'input_1':preprocess_input(image),'lstm_1_input':one})
	print predict

	with open('words.txt','r') as word:
		p = 0
		for line in word:
			if p == predict[0][k]:
				xx = line.split('\n')[0]
			p += 1
	for ll in range(0, len(qq)):
		ppp = ppp + qq[ll].split('\n')[0] + ' '
	# print predict
	print ppp





# sentence = '<SOS>'
# with open('words.txt', 'r') as reader:
# 	con = [x.strip() for x in reader.readlines()]

# one_hot = np.zeros((1, 100, 12503))
# index_sos = con.index(sentence)

# one_hot[0, 0, index_sos] = 1

# print(index_sos)
# cv2.imshow('image', image.astype(np.uint8))
# cv2.waitKey(0)
# predict = model.predict_classes([preprocess_input(np.array([image])), one_hot])

# print(predict)

