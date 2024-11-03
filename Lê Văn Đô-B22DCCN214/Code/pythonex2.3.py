import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'results.csv')

# Vẽ hàm histogram
for i,x in enumerate(df.columns[4:]):
    print(f"phân bố của {x}")
    df_copy =df.copy()
    tmp =df_copy[x]
    tmp.dropna(axis=0,inplace=True)
    plt.hist(tmp)
    plt.xlabel(x)
    plt.ylabel("Frequency")
    plt.show()