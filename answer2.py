import pandas as pd
# pandas documentation: https://pandas.pydata.org/docs/user_guide/index.html#user-guide
# other pandas info: https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html
# index - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html?highlight=index#pandas.DataFrame.index
# splitting objects into groups - https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#splitting-an-object-into-groups
# selecting a subset of rows from a group - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.head.html?highlight=head


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
