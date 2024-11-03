import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Đọc dữ liệu từ file CSV
df = pd.read_csv(r'results.csv')


# Lấy các cột chỉ số bắt đầu từ cột thứ 6
indicator_columns = df.columns[5:25]

# Chọn dữ liệu và loại bỏ các hàng có giá trị NaN
df[indicator_columns] = df[indicator_columns].replace('N/a', pd.NA)
data = df[indicator_columns].dropna()

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Sử dụng K-means để phân nhóm
n_clusters=5 # Có thể thay đổi số lượng nhóm
kmeans = KMeans(n_clusters, random_state=42)  # Có thể thay đổi số lượng random_state
kmeans.fit(data_scaled)

# Gán nhãn cho mỗi cầu thủ
df['Cluster'] = kmeans.labels_

# Sử dụng PCA để giảm chiều dữ liệu cho việc trực quan hóa
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Thêm thông tin PCA vào DataFrame
df['PCA1'] = data_pca[:, 0]
df['PCA2'] = data_pca[:, 1]

# Hiển thị một số thông tin về các cầu thủ trong từng nhóm
for i in range(n_clusters):  # Số nhóm
    print(f"\nCluster {i}:")
    print(df[df['Cluster'] == i][['Player', 'Team', 'Cluster']].head())

# Vẽ biểu đồ phân cụm
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=df, palette='viridis', legend='full')
plt.title('K-means Clustering of Players')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.grid()
plt.show()