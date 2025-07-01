import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\krish\\Downloads\\Updated_AI_Learning_Plan_MrK_4hrs_day.csv')
print(df.head())

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
s = pd.Series(data)
print(s.iloc[4])


# Creating a DataFrame from a dictionary
data = {'Student': ['David', 'Samuel', 'Terry', 'Evan'],
        'Age': [27, 24, 22, 32],
        'Country': ['UK', 'Canada', 'China', 'USA'],
        'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
        'Marks': [85, 72, 89, 76]}
df1 = pd.DataFrame(data)
unique_dates = df1['Age'].unique()
print(unique_dates) 

X=np.array([[1,0],[0,1]])

Y=np.array([[2,2],[2,2]]) 
Z=np.dot(X,Y) 
print(Z) # Output: [[2 2]
