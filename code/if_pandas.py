import pandas as pd

# Create a DataFrame from the dataset
data = {'Region': ['Region 1', 'Region 2', 'Region 3'],
        'January': [1000, 4000, 7000],
        'February': [2000, 5000, 8000],
        'March': [3000, 6000, 9000]}
df = pd.DataFrame(data)

# Sum the values in the Region 2 column
region2_sum = df[df['Region'] == 'Region 2'].sum().sum()

# Use an if-condition to check the sum and return "bonus" or "no bonus"
if region2_sum > 13000:
    print("bonus")
else:
    print("no bonus")
