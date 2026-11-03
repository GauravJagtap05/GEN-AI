#  small machine learning program to read a csv file and print the prediction logic 

import pandas as pd
from sklearn.linear_model import LinearRegression
# here sklearn is package and linear regression is a class in sklearn package and LinearRegression is a method


df = pd.read_csv("D:/AVD/Gen-AI/Gen_AI_Files/Data.csv")
print(df)

X = df[["years"]]   # input column should alwats be in dataframe format x is input to our program
print(X)
y = df["salary"]
print(y)

# now traning the model
model = LinearRegression()
model.fit(X, y)

#now we have to predict the output for 5 years experience using .predict() method()

employee = pd.DataFrame({"years": [7]})
result = model.predict(employee)
print('result for 7 years experience is :', result)


