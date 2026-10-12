import pandas as pd 

s1 = pd.Series([2.0,3.1,4.5], index=['a', 'b', 'c'])
print(s1.values)
print(s1.index)
print(s1.loc['a'])
print(s1.iloc[0])
s1.loc['b'] = 10
print(f"Series:\n {s1}") 