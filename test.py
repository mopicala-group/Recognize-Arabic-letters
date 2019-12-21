from os import listdir, mkdir
from os.path import isdir, join, isfile, splitext
import re
import os
import cv2
import csv
import numpy as np
import pandas as pd
import time
import getting_data_to_csv as gtd
import data_processing as dp
import test_train_accuracy as tta


image_size = 64
csv_file='csv_output_file.csv'
data_input='cut_images' 
data_in1='image'
data_in = r'E:\PycharmProjects\letters_numbers_train\cut_images\image'
dc={}




def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if
            re.match(r'.*\.(jpg|jpeg|png|bmp)', f, flags=re.I)]

def write_images_to_csv():
   for x in listdir(data_input):
        join(data_input, x)

   with open(csv_file, 'w', newline='') as file1:
        writer = csv.writer(file1)
        writer.writerow(["Name_of_image"])
        for sub_dir in listdir(data_input):
            a = join(data_input, sub_dir)
            if not isdir(join(data_input, sub_dir)):
                continue
            name_of_dir = sub_dir
            i=1
            for img_path in image_files_in_folder(join(data_input, sub_dir)):
                writer.writerow(['b' +str(i)])
                image = cv2.imread(img_path)
                i=i+1
                if image is None:
                    print("Error")
                    continue
        print("step(gen_bana_data) is -[done]")

def process_cut_data(data):
    ret_img = dp.load_image_porc(data_in)
    for x in ret_img:
        img = cv2.imread(x)
        images1 = np.empty((0, image_size * image_size))
        images1 = np.array(images1, np.float32)
        images1 = images1.reshape((images1.size, 1))
        return images1


img='E:\PycharmProjects\letters_numbers_train\1_52'

def test(KNearest,img):  

    lb2 = b.inverse_Transform(c)
    for tt in range (len(c)):
        dc[str(c[tt].tolist())] = lb2[tt]

    if img is not None:
        img = dp.load_image_porc(img=img)
        g=cv2.imread(img)
        img=np.float32(img)
        ret, resultA, neig, dist = KNearest.findNearest(img, k=1)
        res=int(resultA[0][0])
        return res
    else:
        return False

if __name__ == '__main__':

     gtd.gen_bana_data(data_input ,csv_file)
     x,y =dp.porc_data_nasser(csv_file)
     a,b,c=tta.train(x,y)
     img1=cv2.imread(img)
     re=test(a, img1)
     print(re)







