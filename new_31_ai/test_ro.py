#pentru instalare
# pip install numpy
# pip install -U scikit-learn
from sklearn.linear_model import LinearRegression
import numpy as np

# [temperatura,nr persoane, ora din zi]
X = np.array([
 [22,5,12],
 [18,3,6],
 [27,10,18],
 [23,4,14],
 [21,2,9]
])

# consumul de energie (kWh)
y = np.array([70,50,120,80,40])

#initializam modelul de regresie lineara
model = LinearRegression()

# antrenam modelul
model.fit(X,y)

prezicere = model.predict([[25,6,15]])

print(prezicere)