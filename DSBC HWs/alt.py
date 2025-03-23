# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'Temperature': [70, 75, 80, 65, 72],
    'Humidity': [60, 55, 50, 65, 58],
    'Wind_Speed': [10, 15, 5, 12, 8],
    'Sales': [100, 120, 90, 80, 110]
})

# One-hot encode categorical variable
encoded_df = pd.get_dummies(df, columns=['Weather_Condition'])

# Calculate correlation matrix
correlation_matrix = encoded_df.corr()

# Visualize correlation matrix
plt.figure(figsize=(10,8))
plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto')
plt.colorbar()
plt.title('Correlation Matrix')
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

# Add correlation values in each cell
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', 
                 ha='center', va='center')

plt.tight_layout()
plt.show()
