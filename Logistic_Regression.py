#all module will be imported here:
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data.csv")

velocity_list = df["Velocity"].tolist()
escaped_list = df["Escaped"].tolist()

fig = px.scatter(x= velocity_list, y= escaped_list)
fig.show()

#making an line of Regression:
Velocity_array = np.array(velocity_list)
escaped_array = np.array(escaped_list)

m,c = np.polyfit(Velocity_array, escaped_array,1)

y=[]

for x in Velocity_array:
    y_value = m*x+c
    y.append(y_value)

fig = px.scatter(x=Velocity_array, y= escaped_array)
fig.update_layout(shapes=[
    dict(
        type= 'line',
        y0= min(y), y1= max(y),
        x0= min(Velocity_array),x1= max(Velocity_array)
    )
])
fig.show()

# making an sigmoid function:
X = np.reshape(velocity_list, (len(velocity_list), 1))
Y = np.reshape(escaped_list, (len(escaped_list), 1))

lr = LogisticRegression()
lr.fit(X, Y)

plt.figure()
plt.scatter(X.ravel(), Y, color='black', zorder=20)


def model(x):
  return 1 / (1 + np.exp(-x))


#Using the line formula
X_test = np.linspace(0, 100, 200)
chances = model(X_test * lr.coef_ + lr.intercept_).ravel()

plt.plot(X_test, chances, color='red', linewidth=3)
plt.axhline(y=0, color='k', linestyle='-')
plt.axhline(y=1, color='k', linestyle='-')
plt.axhline(y=0.5, color='b', linestyle='--')

# do hit and trial by changing the value of X_test
plt.axvline(x=X_test[23], color='b', linestyle='--')

plt.ylabel('y')
plt.xlabel('X')
plt.xlim(0, 30)
plt.show()
