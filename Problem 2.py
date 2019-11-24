import pandas as pd
A = pd.read_csv('cars.csv')

# Problem 2a
OddColumn = A.iloc[0:5,0::2]

# Problem 2b
MazdaRX4 = A.iloc[0]

#Problem 2c
CamZ28 = A.loc[[23], ['Model','cyl']]

#Problem 2d
MazRX4Wag = A.iloc[[1], [0,2,10]]
FordPanL = A.iloc[[28],[0,2,10]]
HondaCivic = A.iloc[[18], [0,2,10]]
B = [MazRX4Wag, FordPanL, HondaCivic]
cylgear = pd.concat(B)

