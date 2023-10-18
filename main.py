# Import the pandas library under its usual alias
import pandas as pd

# Load the business.csv file as a DataFrame called businesses
businesses = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/oldest_business_dataset/businesses.csv")

# Sort businesses from oldest businesses to youngest
sorted_businesses = businesses.sort_values(by="year_founded")

# Display the first few lines of sorted_businesses
print(sorted_businesses.head())


