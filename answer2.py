import pandas as pd

# read CSV file into pandas dataframe
df = pd.read_csv('col.csv')

# initially set Result to 'No' for all rows
df['Result'] = 'No'

# Group the dataframe by Col1 using 'df.groupby()',
# and use .head(1) to select the first row of each group.
# Use.loc[] to set Result to 'Yes' for the selected rows
df.loc[df.groupby('Col1').head(1).index, 'Result'] = 'Yes'

# write updated dataframe to a new CSV file
df.to_csv('col1_updated.csv', index=False)
