import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 120, 150, 130, 140],
    'Expenses': [80, 90, 100, 110, 95]
}

# Creating a DataFrame
df = pd.DataFrame(data)
# Plotting Sales and Expenses data (stacked bar plot)
plt.figure(figsize=(10, 6))  # Set figure size
plt.bar(df['Month'], df['Sales'], color='blue', label='Sales')
plt.bar(df['Month'], df['Expenses'], bottom=df['Sales'], color='red', label='Expenses')
plt.title('Monthly Sales and Expenses (Stacked Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()  # Show legend
plt.grid(axis='y')  # Show grid lines on y-axis
plt.show()