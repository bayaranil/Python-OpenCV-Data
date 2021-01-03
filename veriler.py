# 1. KUTUPHANELER
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 2. VERI ON ISLEME
# 2.1. VERI YUKLEME
veriler = pd.read_csv("maaslar.csv")

x = veriler.iloc[:,1:2]
y = veriler.iloc[:,-1]
X = x.values
Y = y.values


#LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

plt.scatter(X,Y, color="red")
plt.plot(X,lin_reg.predict(X), color="blue")
plt.show()

#POLYNOMIAL REGRESSION
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y)
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X))) #buraya x_poly de yazabilirsin.
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y)
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X))) #buraya x_poly de yazabilirsin.
plt.show()


# FUTURE PREDİCTS

print(lin_reg.predict([[11]]))
print(lin_reg.predict([[6.6]]))

print(lin_reg2.predict(poly_reg.fit_transform([[6.6]])))
print(lin_reg2.predict(poly_reg.fit_transform([[11]])))




