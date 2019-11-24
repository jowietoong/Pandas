import pandas as pd
import numpy as np
A = pd.read_csv('cars.csv')
B = A.iloc[np.r_[0:5, 27:32]] 

