
#Normalizing and standardizing the features
import pandas as pd
import numpy as np
#handling csv files
print("Reading realEstate_trans.csv")
Read_csv_filename = 'realEstate_trans.csv'
Read_csv_data = pd.read_csv(Read_csv_filename)

def normalize(col):    
#Normalize column/ min max scaling
    return (col - col.min()) / (col.max() - col.min())

def standardize(col):
#Standardize column
    return (col - col.mean()) / col.std()

# list of columns to normalize and standardize
cols = ['price_mean','sq__ft','zip']
Read_csv_data['price_mean'] = np.nan
#Read_csv_data.drop("price_mean",axis=1,inplace=True)
#fillna using mean
Read_csv_data['price_mean'] = Read_csv_data['price_mean'].fillna(Read_csv_data.groupby('zip')['price'].transform('mean'))
for col in cols:
    Read_csv_data['n_' + col] = normalize(Read_csv_data[col])
    Read_csv_data['s_' + col] = standardize(Read_csv_data[col])

print("Head records from realEstate_trans.csv file")
print(Read_csv_data.head(5))

Write_csv_filename = 'output/realEstate_trans_ns.csv'
with open(Write_csv_filename,'w+') as write_csv:
    write_csv.write(Read_csv_data.to_csv(sep=',',index = False))

write_csv.close()