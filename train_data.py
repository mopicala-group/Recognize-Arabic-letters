from os import listdir, mkdir
from os.path import isdir, join, isfile, splitext
import re
import os
import cv2
import csv
import numpy as np
import pandas as pd
import time

file_data = 'pathes and classes name.csv'
image_size = 64
data_in = 'data_arabic'

def image_files_in_folder(folder):
        return [os.path.join(folder, f) for f in os.listdir(folder) if
                re.match(r'.*\.(jpg|jpeg|png|bmp)', f, flags=re.I)]
                
def gen_bana_data(data_input ,data_output):
    

    for x in listdir(data_input):
        join(data_input, x)

    
    with open(data_output, 'w', newline='') as file1:
        writer = csv.writer(file1)
        writer.writerow(["Name_of_dir", "path_of_image"])
        for sub_dir in listdir(data_input):
            a = join(data_input, sub_dir)
            if not isdir(join(data_input, sub_dir)):
                continue
            name_of_dir = sub_dir
            for img_path in image_files_in_folder(join(data_input, sub_dir)):
                writer.writerow(['b'+str(name_of_dir), img_path])
                image = cv2.imread(img_path)
                if image is None:
                    print("Error")
                    continue
    print("step(gen_bana_data) is -[done]")


if __name__ == '__main__':
    gen_bana_data(data_in ,file_data) #get Bayan T data &names as csv

