# -*- coding: utf-8 -*-
import os
import cv2
import csv
import numpy as np
import pandas as pd
import time

file_data = 'pathes and classes name.csv'
image_size = 64
data_in = 'data_arabic'
def load_image_porc(img=None):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    conv = cv2.resize(gray, (image_size, image_size))
    flo = conv.astype(float)
    return flo


def porc_data_nasser(file_data):
    df = pd.read_csv(file_data)
    images = []
    lables = []
    for data in df.values:
        Name_of_dir = data[0]
        path_of_image = data[1]
        ret_img = load_image_porc(img=path_of_image)
        images.append(ret_img)
        lables.append(Name_of_dir)
    print("step(porc_data) is -[done]")
    return images, lables

if __name__ == '__main__':
    gen_bana_data(data_in, file_data)  # get Bayan T data &names as csv
    x, y = porc_data_nasser(file_data)  # get Processing in data conv to x,y
    time.sleep(2)
    print(x, y)
