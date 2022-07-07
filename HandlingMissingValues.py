
# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0) 


# print the first five rows of the sf_permits DataFrame.
print(sf_permits.head())

#What percentage of the values in the dataset are missing?
total_missing_cells=sf_permits.isnull().sum().sum()
total_cells=np.product(sf_permits.shape)
percent_missing =(total_missing_cells/total_cells)*100

#Figure out why the data is missing:Street Number Suffix data is missing because it might not exist, Zipcode is missing because it wasn't recorded

#If you removed all of the rows of sf_permits with missing values, how many rows are left?
new_dropped_rows=sf_permits.dropna()
rows=sf_permits.shape[0]-new_dropped_rows.shape[0] #No rows are left

#removing all the columns with empty values
sf_permits_with_na_dropped = sf_permits.dropna(axis=1) #Create a new DataFrame called sf_permits_with_na_dropped that has all of the columns with empty values removed

dropped_columns = sf_permits.shape[1]-sf_permits_with_na_dropped.shape[1] #How many columns were removed from the original sf_permits DataFrame? Use this number to set the value of the dropped_columns variable below.

#replacing all the NaN's in the sf_permits data with the one that comes directly after it and then replacing any remaining NaN's with 0. Set the result to a new DataFrame sf_permits_with_na_imputed.
sf_permits_with_na_imputed = sf_permits.fillna(method='bfill',axis=0).fillna(0)
