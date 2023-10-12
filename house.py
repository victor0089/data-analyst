
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset Assuming you have a CSV file named "housing_data.csv" in the current directory, load the dataset into a Pandas DataFrame:

df = pd.read_csv("housing_data.csv")

# Explore the data
# Display the first few rows of the dataset
print(df.head())

# Get an overview of the dataset
print(df.info())

# Get statistical summary of the dataset
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Perform data analysis tasks
# Calculate the average price of houses by the number of bedrooms:
average_price = df.groupby('bedrooms')['price'].mean()
print(average_price)

# Visualize the average price of houses by the number of bedrooms using a bar chart:
average_price.plot(kind='bar')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Average Price')
plt.title('Average Price of Houses by Bedrooms')
plt.show()

# Calculate the correlation between house prices and other numerical variables:
correlation = df[['price', 'sqft_living', 'bedrooms', 'bathrooms']].corr()
print(correlation)

# Visualize the correlation matrix using a heatmap:
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(correlation.shape[1]), correlation.columns, rotation=45)
plt.yticks(range(correlation.shape[1]), correlation.columns)
plt.title('Correlation Matrix')
plt.show()

#Plot the distribution of house prices:
plt.hist(df['price'], bins=30)
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Distribution of House Prices')
plt.show()
