import pandas as pd

# Đọc file CSV
df = pd.read_csv(r'results.csv')

# Chọn các cột cần tính toán
numeric_columns = df.columns[5:]  
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df.fillna(0, inplace=True)

# Tính toán cho toàn giải
overall_stats = {
    'Name': 'all',
    'Median': [df[col].median() for col in numeric_columns],
    'Mean': [df[col].mean() for col in numeric_columns],
    'Std': [df[col].std() for col in numeric_columns],
}

# Tính toán cho từng đội
team_stats = []
teams = df['Team'].unique()
for team in teams:
    team_data = df[df['Team'] == team]
    team_stats.append({
        'Name': team,
        'Median': [team_data[col].median() for col in numeric_columns],
        'Mean': [team_data[col].mean() for col in numeric_columns],
        'Std': [team_data[col].std() for col in numeric_columns],
    })

# Kết hợp dữ liệu
results = [overall_stats] + team_stats
result_df = pd.DataFrame(results)

# Tạo final_result_df bằng cách ghép các cột
final_result_df = pd.DataFrame({
    'Index': range(len(result_df)),
    'Name': result_df['Name'],
})

#tạo một DataFrame mới cho các chỉ số
stats_df = pd.DataFrame({
    **{f'Median of {col}': [row['Median'][numeric_columns.get_loc(col)] for row in results] for col in numeric_columns},
    **{f'Mean of {col}': [row['Mean'][numeric_columns.get_loc(col)] for row in results] for col in numeric_columns},
    **{f'Std of {col}': [row['Std'][numeric_columns.get_loc(col)] for row in results] for col in numeric_columns},
})

# Kết hợp final_result_df và stats_df
final_result_df = pd.concat([final_result_df, stats_df], axis=1)

# Xuất kết quả ra file CSV
final_result_df.to_csv(r'results2.csv', index=False)
