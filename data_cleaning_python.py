import pandas as pd
import numpy as np

# Sample Data Creation
data = {
    'Customer_ID': [101, 102, 103, 104, 102, 105, 106],
    'Age': [25, np.nan, 35, 40, np.nan, 29, np.nan],
    'Income': [50000, 60000, np.nan, 80000, 60000, 52000, 95000],
    'Score': [70, 75, 80, np.nan, 75, 82, 90]
}
df = pd.DataFrame(data)

# 1. Removing Duplicates
df = df.drop_duplicates()

# 2. Imputation Strategies
df['Age'] = df['Age'].fillna(df['Age'].median())  # Median for skewed/discrete Age
df['Income'] = df['Income'].fillna(df['Income'].mean())  # Mean for Income

# 3. Time-Series/Sequential Interpolation (for Score)
df['Score'] = df['Score'].interpolate(method='linear')

# 4. Drop remaining nulls (if any exist)
df_clean = df.dropna()

print(df_clean)