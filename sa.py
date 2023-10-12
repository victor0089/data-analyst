import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
# Display the first few rows of the dataset
print(df.head())

# Get an overview of the dataset
print(df.info())

# Get statistical summary of the dataset
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Calculate total sales by product category
total_sales = df.groupby('Category')['Sales'].sum()
print(total_sales)

# Visualize total sales by product category:
total_sales.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Total Sales by Category')
plt.show()

#Calculate average sales by region and month:
average_sales = df.groupby(['Region', 'Month'])['Sales'].mean()
print(average_sales)

# Visualize average sales by region and month using a line chart:
average_sales.unstack(level='Region').plot(kind='line', marker='o')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.title('Average Sales by Region and Month')
plt.legend()
plt.show()

