import pandas as pd
import numpy as np

f1 = open('train.csv')
f2 = open('test.csv')

train = pd.read_csv(f1)
test = pd.read_csv(f2)

label_set = list(train.columns)
inp_label = label_set
inp_label.remove('label')
target_label = ['label']

train_x = np.array(train[inp_label].values, dtype = 'float64')
train_y = np.array(train[target_label].values, dtype = 'float64')
test_x = np.array(test[inp_label].values, dtype = 'float64')

spn, spx = train_x.shape
nl = spn
train_x = train_x.reshape([spn, 28, 28, 1]) / 255
spn = train_y.shape[0]
if(nl != spn):
    print("Shape Error")
train_y = train_y.reshape([spn])
spn = test_x.shape[0]
test_x = test_x.reshape([spn, 28, 28, 1]) / 255
