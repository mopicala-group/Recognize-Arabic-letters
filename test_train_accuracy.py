import cv2
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
from getting_data_to_csv import gen_bana_data
from data_processing import porc_data_nasser

#---Variables---#
file_data = r'F:\MY_WORK\letters_numbers_train\__.csv'
image_size = 64
data_in = 'data_arabic'
global laab
laab = LabelBinarizer()
#-------------------------#
# transform label to binary
def lbi(y):
    lb = laab
    return lb, lb.fit_transform(y)
#-------------------------------------------------------------------------#
# split dataset ,val = amount data test (val = 0.3 -> data_traint = (1-0.3)
def split_t(X, Y, val):
    partition = int(val * len(Y))
    X_train, X_test = np.split(X, [partition])
    y_train, y_test = np.split(Y, [partition])
    return X_train, y_train, X_test, y_test
#----------------------------------------------#
# get inverse  y & res and return acc %variable%
def get_acc(lb, res, y):
    y = lb.inverse_transform(y)
    res = lb.inverse_transform(res)
    accuracy = (np.squeeze(res) == y).mean()
    return accuracy * 100
#--------------------------#
# check acc train & acc test 
def accuracy(Xtrain, Xtest):
    ret, resultA, neig, dist = KNearest.findNearest(Xtrain, k=5)
    ret, resultB, neig, dist = KNearest.findNearest(Xtest, k=5)
    acc_train = get_acc(lbtr, resultA, Ytrain)
    acc_test = get_acc(lbts, resultB, Ytest)
    print("acc-> train:{} : and test:{}".format(acc_train, acc_test))
    return acc_train,acc_test

#----------------#
# train all data 
def train(X, y):
    f = lbi(y)
    knn = cv2.ml.KNearest_create()
    knn.train(X,cv2.ml.ROW_SAMPLE, f)
    return knn

if __name__ == '__main__':
   gen_bana_data(data_in, file_data)   # get Bayan T data &names as csv
   x, y = porc_data_nasser(file_data)  # get Processing in data conv to x,y
   train(x, y)
