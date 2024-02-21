# pip install numpy
# pip install -U scikit-learn
# pip install pandas
# pip install textblob

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd


df = pd.read_csv("./data/consum_de_energie.csv") # data frame
print(df.head())

x = df[[""]]

#  temperatura, nr persoane, ora din zi
x = np.array([
    [22,5,12],
    [18,3,6],
    [27,10,18],
    [23,4,14],
    [21,2,9]
])


#  consumul de energie
y = np.array([70,50,120,80,40])


#  initializam modelul de regresie lineara
model = LinearRegression()

#  antrenam modelul
model.fit(x,y)


prezicere = model.predict([[25,6,15]])

print(prezicere, "Kwh")