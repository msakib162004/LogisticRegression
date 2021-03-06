# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CTbBv3N6PNoq83Dd2AmfT8zZZyHbUJEA
"""

import pandas as pd
from pandas.api.types import is_string_dtype

data = pd.read_csv('adult.csv', na_values='?')

data

from sklearn.preprocessing import Binarizer
cont_col = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
b_data = pd.DataFrame()

for col in data.columns:
  if col in cont_col:
    bin = Binarizer(threshold=data[col].mean())
    b_data[col] = bin.transform(data[[col]]).flatten()
  else:
    b_data[col] = data[col].copy()

b_data

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.get_dummies(b_data, drop_first=True)

data

train_x, test_x, train_y, test_y = train_test_split(data.drop('salary_ >50K', axis=1), data['salary_ >50K'], train_size=0.85)

train_y

Log_Reg = LogisticRegression()
Log_Reg.fit(train_x, train_y)

from sklearn.metrics import accuracy_score, f1_score

acc = Log_Reg.predict(test_x)

acc1 = accuracy_score(test_y, acc)
f11 = f1_score(test_y, acc)

print(acc1, f11)