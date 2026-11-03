from sklearn.linear_model import LinearRegression
import pandas as pd

model = LinearRegression()

# reading the data
df = pd.read_csv("D:/AVD/Gen-AI/Gen_AI_Files/Data_3input.csv")
print(df)

# taking input seprate # output is always in dataframe format
X = df[["years", "location"]]
print(X)

# taking output seprately
y = df['salary']
print(y)

# here one column is in string type so we need to convert it string to numeric using get_dummies() method of pandas library
X = pd.get_dummies(X, columns=['location'], dtype= int)
print(X)

# now traning the data using model.fit(input, output).
model = LinearRegression()
# .fit() method is used to train the model data using input and output value.
model.fit(X, y)   

# now we are going to predict the output of 5v years experience individual having location bangalore using predict() method of model

employee = pd.DataFrame({
    'years': [6], 
    "location": ["pune"]
    })

employee = pd.get_dummies(employee,  columns=['location'], dtype=int)
employee = employee.reindex(

    columns=X.columns,
    fill_value=0
)

print(employee)

# predicting the output
result = model.predict(employee)
print(result)