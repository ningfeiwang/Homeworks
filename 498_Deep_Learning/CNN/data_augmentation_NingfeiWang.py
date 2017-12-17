from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
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
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
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
                print each_img

                if 'gif' in each_img:
                    # continue
                    a = each_img.split('.')
                    each_img1 = each_img
                    each_img = a[0]+'.png'
                    Image.open(os.path.join(path,each_dir,each_img_dir,each_img1)).save(os.path.join(path,each_dir,each_img_dir,each_img))
                
  

                img = load_img(os.path.join(path,each_dir,each_img_dir,each_img))  
                x = img_to_array(img)  
                x = x.reshape((1,) + x.shape) 
                i = 0
                for batch in datagen.flow(x, batch_size=1,
                                          save_to_dir=os.path.join(path,each_dir,each_img_dir), save_prefix=each_img_dir, save_format='jpeg'):
                    i += 1
                    if i > 4:
                        print i
                        break  
if __name__ == '__main__':
    # shape to be [samples][pixels][width][height]
    global path, width, height
    
    path = '/Users/wangningfei/Desktop/Lehigh_Fall2017/CSE498/data'
    get_img()