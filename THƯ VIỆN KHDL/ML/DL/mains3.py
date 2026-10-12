import pandas as pd 
import numpy as np 

df = pd.DataFrame({'Total': [1,3,5], 'Quantity': [2, np.nan, 6]}, index=['a', 'b', 'c'])
print(df.dropna())