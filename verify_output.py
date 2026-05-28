import pandas as pd
path = r'C:\Users\N.Sree Varshini\Downloads\Dataset_features.csv'
df = pd.read_csv(path)
print('shape', df.shape)
print('new columns:', [c for c in df.columns if 'Length' in c or 'Flag' in c or c == 'Num Cuisines'])
print(df[['Restaurant Name','Restaurant Name Length','Address','Address Length','Has Table booking','Has Table Booking Flag','Has Online delivery','Has Online Delivery Flag']].head(5).to_string(index=False))
