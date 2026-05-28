import pandas as pd
import os

path = r'C:\Users\N.Sree Varshini\Downloads\Dataset .csv'
print('path exists:', os.path.exists(path))
df = pd.read_csv(path)
print('shape:', df.shape)
print('columns:', df.columns.tolist())
print(df.head(5).to_string())
