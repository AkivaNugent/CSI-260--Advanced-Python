import pandas as pd
#Replacing values:
df = pd.read_csv('data.csv')
#df.fillna(1, inplace = True) This fails due to conflicting data types

#Replacing values in a specific column
df = pd.read_csv('data.csv')
df.fillna({"Calories": 000}, inplace=True)

extract_df = df[df['Calories'] == 000]
print(extract_df.to_string())

x1 = df["Calories"].mean()
df.fillna({"Calories": x1}, inplace=True)
print("Average calories = ",x1)
"""
x2 = df["Calories"].median()
df.fillna({"Calories": x2}, inplace=True)
print("Median calories = ",x2)

x3 = df["Calories"].mode()[0]
df.fillna({"Calories": x3}, inplace=True)
print("The mode =  ",x3)

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())
"""