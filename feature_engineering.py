import pandas as pd
import os

input_path = r'C:\Users\N.Sree Varshini\Downloads\Dataset .csv'
output_path = r'C:\Users\N.Sree Varshini\Downloads\Dataset_features.csv'

assert os.path.exists(input_path), f"Input file not found: {input_path}"

df = pd.read_csv(input_path)

# Feature extraction from existing columns

df['Restaurant Name Length'] = df['Restaurant Name'].fillna('').astype(str).map(len)
df['Address Length'] = df['Address'].fillna('').astype(str).map(len)
df['Num Cuisines'] = df['Cuisines'].fillna('').astype(str).map(lambda x: len([c for c in x.split(',') if c.strip()]))

# Encode binary categorical variables
noyes_map = {'Yes': 1, 'No': 0, 'yes': 1, 'no': 0, 'YES': 1, 'NO': 0}

df['Has Table Booking Flag'] = df['Has Table booking'].map(noyes_map).fillna(0).astype(int)
df['Has Online Delivery Flag'] = df['Has Online delivery'].map(noyes_map).fillna(0).astype(int)
df['Is Delivering Now Flag'] = df['Is delivering now'].map(noyes_map).fillna(0).astype(int)
df['Switch to Order Menu Flag'] = df['Switch to order menu'].map(noyes_map).fillna(0).astype(int)

# Keep the original categorical columns and add engineered features
# Save the transformed dataset

df.to_csv(output_path, index=False)
print(f"Saved engineered dataset to: {output_path}")
