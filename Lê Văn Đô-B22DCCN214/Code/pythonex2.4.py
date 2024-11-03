import pandas as pd

df = pd.read_csv(r'results.csv')
columns_to_sum = df.columns[5:].tolist()
df[columns_to_sum] = df[columns_to_sum].apply(pd.to_numeric, errors='coerce')
team_stats = df.groupby('Team')[columns_to_sum].sum()
highest_team_stats = team_stats.idxmax()
for stat in team_stats.columns:
    print(f"'{stat}': {highest_team_stats[stat]}")