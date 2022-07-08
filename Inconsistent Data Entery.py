# modules we'll use
import pandas as pd
import numpy as np

# helpful modules
import fuzzywuzzy
from fuzzywuzzy import process
import chardet

# read in all our data
professors = pd.read_csv("../input/pakistan-intellectual-capital/pakistan_intellectual_capital.csv")

# set seed for reproducibility
np.random.seed(0)
 #replace_matches_in_column_function
def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
   # let us know the function's done
      print("All done!")
    
#tasks:    
#take a look at all the unique values in the "Graduated from" column.
colleges=professors['Graduated from'].unique()
colleges

#Convert every entry in the "Graduated from" column in the professors DataFrame to remove white spaces at the beginning and end of cells.
professors['Graduated from']=professors['Graduated from'].str.strip()

#Correct the "Country" column in the dataframe to replace 'usofa' with 'usa'.
matches=fuzzywuzzy.process.extract('usa','Country',limit=10,scorer=fuzzywuzzy.fuzz.token_sort_ratio)
replace_matches_in_column(df=professors, column='Country', string_to_match="usa", min_ratio=70)
