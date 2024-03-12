import pandas as pd

df = pd.read_csv('C:/Users/dtgiv/Downloads/loan_data.csv')
print(df)

pd.set_option('display.max_columns', 200)

#convert data to categorical type
df['Loan_ID'] = df['Loan_ID'].astype('category')
df['Loan_ID'] = df['Loan_ID'].cat.codes
df['Gender'] = df['Gender'] .astype('category')
df['Gender'] = df['Gender'].cat.codes
df['Married'] = df['Married'] .astype('category')
df['Married'] = df['Married'].cat.codes
df['Dependents'] = df['Dependents'] .astype('category')
df['Dependents'] = df['Dependents'].cat.codes
df['Education'] = df['Education'] .astype('category')
df['Education'] = df['Education'].cat.codes
df['Self_Employed'] = df['Self_Employed'] .astype('category')
df['Self_Employed'] = df['Self_Employed'].cat.codes
df['Property_Area'] = df['Property_Area'] .astype('category')
df['Property_Area'] = df['Property_Area'].cat.codes
df['Loan_Status'] = df['Loan_Status'] .astype('category')
df['Loan_Status'] = df['Loan_Status'].cat.codes
print(df)

#check for nulls
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())

#separate out independent variables and dependent variable
x = df.drop(columns = 'Loan_Status')
print(x)

y = df['Loan_Status']
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 21)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

#because the range of values in my independent variable dataset (x) is so great, I will scale the data

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(random_state = 0).fit(x_train_scaled, y_train)

print(log_reg.predict(x_train_scaled))

print(log_reg.score(x_train_scaled, y_train))

print(log_reg.score(x_test_scaled, y_test))


