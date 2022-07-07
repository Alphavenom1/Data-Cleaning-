#Env
# modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# read in all our data
kickstarters_2017 = pd.read_csv("../input/kickstarter-projects/ks-projects-201801.csv")

# set seed for reproducibility
np.random.seed(0)
# select the usd_goal_real column
original_data = pd.DataFrame(kickstarters_2017.usd_goal_real)

# scale the goals from 0 to 1
scaled_data = minmax_scaling(original_data, columns=['usd_goal_real'])

print('Original data\nPreview:\n', original_data.head())
print('Minimum value:', float(original_data.min()),
      '\nMaximum value:', float(original_data.max()))
print('_'*30)

print('\nScaled data\nPreview:\n', scaled_data.head())
print('Minimum value:', float(scaled_data.min()),
      '\nMaximum value:', float(scaled_data.max()))
original_goal_data=pd.DataFrame(kickstarters_2017.goal)

#Use original_goal_data to create a new DataFrame scaled_goal_data with values scaled between 0 and 1. You must use the minmax_scaling() function.
scaled_goal_data =minmax_scaling(original_goal_data, columns=['goal'])

#normalize the "pledged" column.
index_of_positive_pledges = kickstarters_2017.pledged > 0
positive_pledges = kickstarters_2017.pledged.loc[index_of_positive_pledges]
normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], 
                               name='pledged', index=positive_pledges.index)


      
