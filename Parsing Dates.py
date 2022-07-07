# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
earthquakes = pd.read_csv("../input/earthquake-database/database.csv")

# set seed for reproducibility
np.random.seed(0)

# does it look like it contains dates? What is the dtype of the column? 
#The column looks like it contains dates in the format m/d/Y
earthquakes['Date'].dtype #the dtype is object

#create a new column "date_parsed" in the earthquakes dataset that has correctly parsed dates in it.
earthquakes.at[3378,'Date']='02/23/1975'   
earthquakes.at[7512,'Date']='04/28/1985'
earthquakes.at[20650,'Date']='03/13/2011'
earthquakes['date_parsed']=pd.to_datetime(earthquakes['Date'],format="%m/%d/%Y")

#Create a Pandas Series day_of_month_earthquakes containing the day of the month from the "date_parsed" column.
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day

#Plot the days of the month from your earthquake dataset.
day_of_month_earthquakes = day_of_month_earthquakes.dropna()
sns.distplot(day_of_month_earthquakes, kde=False, bins=31) #The graph we get makes sense, it gives an even distribution of dates of the month

