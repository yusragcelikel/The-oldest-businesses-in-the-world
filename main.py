# Import the pandas library under its usual alias
import pandas as pd

# Load the business.csv file as a DataFrame called businesses
businesses = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/oldest_business_dataset/businesses.csv")

# Sort businesses from oldest businesses to youngest
sorted_businesses = businesses.sort_values(by="year_founded")

# Display the first few lines of sorted_businesses
print(sorted_businesses.head())



# Load countries.csv to a DataFrame
countries = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/oldest_business_dataset/countries.csv")

# Merge sorted_businesses with countries
businesses_countries = sorted_businesses.merge(countries, on="country_code" )

# Filter businesses_countries to include countries in North America only
north_america = businesses_countries[businesses_countries["continent"] == "North America"]
print(north_america.head())



# Create continent, which lists only the continent and oldest year_founded
continent = businesses_countries[["continent", "year_founded"]].sort_values(by="year_founded").drop_duplicates(subset="continent").set_index("continent")

# Merge continent with businesses_countries
merged_continent = continent.merge(businesses_countries, on=["continent", "year_founded"])

# Subset continent so that only the four columns of interest are included
subset_merged_continent = merged_continent[["continent", "country", "business", "year_founded"]]
print(subset_merged_continent)
