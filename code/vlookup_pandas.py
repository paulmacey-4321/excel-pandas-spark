import pandas as pd

# Create a DataFrame from the dataset
data = {'Region': ['Region 1', 'Region 2', 'Region 3'],
        'January': [1000, 4000, 7000],
        'February': [2000, 5000, 8000],
        'March': [3000, 6000, 9000]}
df = pd.DataFrame(data)

# Create a new DataFrame with a lookup value
lookup = pd.DataFrame({'Region': ['Region 2'],
                      'Lookup': ['Region2_Total']})

# Use the merge() function to perform a vlookup
merged_df = pd.merge(df, lookup, on='Region', how='left')

# Print the resulting DataFrame
print(merged_df)


or

lookup_value = df.loc[df['Region'] == 'Region 2', 'Region'].values[0]