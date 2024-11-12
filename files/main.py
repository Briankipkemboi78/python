import pandas as pd

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

print(squirrel_data.columns)

fur_count = squirrel_data.groupby('Primary Fur Color')['Unique Squirrel ID'].count()
sq_count = fur_count.reset_index().rename(columns={'Unique Squirrel ID': 'count'})
sq_count.to_csv('fur_count.csv', index=False)