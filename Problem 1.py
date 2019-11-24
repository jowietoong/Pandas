import pandas as pd
A = pd.read_csv('cars.csv')
first = A.iloc[0:5]
last = A.iloc[27:32] 
B = [first,last]
C = pd.concat(B)


