# Any groupby operation involves one of the following
# operations on the original object. They are −
#       Splitting the Object
#       Applying a function

# In many situations, we split the data into sets
# and we apply some functionality on each subset.

# In the apply functionality, we can perform the following operations −
#   Aggregation − computing a summary statistic
#   Transformation − perform some group-specific operation
#   Filtration − discarding the data with some condition

print("==========================================================")

# Syntax
# dataframe_object.groupby('key')

import pandas as pd
import numpy as np
import pprint

input_data = {
            'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings','kings'],
            'Rank': [1, 2, 2, 3, 3, 4],
            'Year': [2014, 2015, 2014, 2015, 2014, 2015],
            'Points': [876, 789, 863, 673, 741, 812]
            }

df = pd.DataFrame(input_data)

print(df)

print("==========================================================")

# groupby - DataFrameGroupBy object will be created
print(df.groupby('Team'))


# Viewing the groups
groupby_teams_dict = df.groupby('Team').groups
pprint.pprint(groupby_teams_dict)

print("==========================================================")

# groupby 2 keys
groupby_teams_year_dict = df.groupby(['Team','Year']).groups
pprint.pprint(groupby_teams_year_dict)

print("==========================================================")

# iterating through groups

grouped = df.groupby('Year')

for year,group in grouped:
   print(year)
   print(group)

print("==========================================================")

# numpy does the numerical related stuff, while pandas 
# focueses on more aggregation/ bulk manipulation stuff

print(grouped['Rank'].agg(np.sum))