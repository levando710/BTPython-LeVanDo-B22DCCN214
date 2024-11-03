import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r'D:\btlpython\results.csv')

# Lấy các cột chỉ số
indicator_columns = df.columns[5:8]
df[indicator_columns] = df[indicator_columns].replace('N/a', pd.NA)
data = df[indicator_columns].apply(pd.to_numeric, errors='coerce').dropna()

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Sử dụng K-means để phân nhóm
n_clusters = 4  # Có thể thay đổi số lượng nhóm
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(data_scaled)

# Gán nhãn cho mỗi cầu thủ
df['Cluster'] = kmeans.labels_

# Hiển thị một số thông tin về các cầu thủ trong từng nhóm
for i in range(n_clusters):  # Số nhóm
    print(f"\nCluster {i}:")
    print(df[df['Cluster'] == i][['Player', 'Team', 'Cluster']].head())

# Vẽ biểu đồ phân cụm
plt.figure(figsize=(10, 6))
x_index = 0  # Cột đầu tiên trong data_scaled
y_index = 1  # Cột thứ hai trong data_scaled
plt.scatter(data_scaled[:, x_index], data_scaled[:, y_index], c=df['Cluster'], cmap='viridis', marker='o')
plt.title('K-means Clustering of Players')
plt.xlabel(f'Feature {x_index + 1}')
plt.ylabel(f'Feature {y_index + 1}')
plt.colorbar(label='Cluster')
plt.grid()
plt.show()