import pandas as pd

df = pd.read_csv(r'results.csv')
df.iloc[:, 5:] = df.iloc[:, 5:].replace(',', '', regex=True)
df.iloc[:, 4:] = df.iloc[:, 4:].apply(pd.to_numeric, errors='coerce')
for x in df.columns[4:]:
    tmp =df[['Player',x]].sort_values(x)
    tmp.dropna(axis=0, inplace=True)
    print(f'3 cầu thủ có {x} cao nhất')
    print(tmp[-3:][::-1])
    print(f'3 cầu thủ có {x} thấp nhất')
    print(tmp[:3])