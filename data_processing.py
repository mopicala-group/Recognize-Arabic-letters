# -*- coding: utf-8 -*-
from getting_data_to_csv import gen_bana_data
import os
import cv2
import csv
import numpy as np
import pandas as pd
import time

file_data = 'pathes_and_classes_name.csv'
image_size = 64
data_in = 'data_arabic'


def load_image_porc(img=None):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray,5)
    th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)
    conv = cv2.resize(th3, (image_size, image_size))
    re_shape = conv.reshape((1, image_size * image_size))
    return re_shape

def porc_data_nasser(file_data):
    df = pd.read_csv(file_data)
    images = np.empty((0, image_size * image_size))
    lables = []
    for data in df.values:
        Name_of_dir=data[0]
        path_of_image=data[1]
        ret_img = load_image_porc(img=path_of_image)
        images = np.append(images, ret_img, 0)
        lables.append(Name_of_dir)
        
    images = np.array(images, np.float32)
    print("step(porc_data) is -[done]")
    return images ,lables

if __name__ == '__main__':
    gen_bana_data(data_in, file_data)  # get Bayan T data &names as csv
    x, y = porc_data_nasser(file_data)  # get Processing in data conv to x,y
    time.sleep(2)
    print(x, y)
