import pandas as pd

# Create a DataFrame from the dataset
data = {'Region': ['Region 1', 'Region 2', 'Region 3'],
        'January': [1000, 4000, 7000],
        'February': [2000, 5000, 8000],
        'March': [3000, 6000, 9000]}
df = pd.DataFrame(data)

# Calculate the average sales for January
january_avg = df['January'].mean()
print(january_avg)