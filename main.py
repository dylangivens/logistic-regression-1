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

#8:30