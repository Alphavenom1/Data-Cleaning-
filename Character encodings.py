# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

# set seed for reproducibility
np.random.seed(0)

#create a variable new_entry that changes the encoding from "big5-tw" to "utf-8". new_entry should have the bytes datatype.
new_entry = (sample_entry.decode("big5-tw")).encode('utf-8', errors="replace")

#Use the code cell below to read in this file at path "../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv".
with open("../input/fatal-police-shootings-in-the-us/put isPoliceKillingsUS.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
print(result)
#output is : {'encoding': 'Windows-1252', 'confidence':      o.73, 'language': ''}
police_killings=pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='Windows-1252')
police_killings.head()

#Save a version of the police killings dataset to CSV with UTF-8 encoding. 
police_killings.to_csv("/kaggle/working/police_killings-utf8.csv")
