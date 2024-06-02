import pandas as pd

# Read the CSV file
data = pd.read_csv('data.csv')

# Display the first few rows of the data
print("First few rows of the data:")
print(data.head())

# Display basic statistics
print("\nBasic statistics:")
print(data.describe())

# Calculate the mean of a specific column (replace 'column_name' with the actual column name)
column_name = 'column_name'
mean_value = data[column_name].mean()
print(f"\nMean value of {column_name}: {mean_value}")

# Filter data based on a condition (replace 'column_name' and 'value' with actual values)
filtered_data = data[data[column_name] > value]
print(f"\nFiltered data (where {column_name} > value):")
print(filtered_data)

# Save the filtered data to a new CSV file
filtered_data.to_csv('filtered_data.csv', index=False)
print("\nFiltered data saved to 'filtered_data.csv'")
