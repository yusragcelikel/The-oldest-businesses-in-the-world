# Import the pandas library under its usual alias
import pandas as pd

# Load the business.csv file as a DataFrame called businesses
businesses = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/oldest_business_dataset/businesses.csv")

# Sort businesses from oldest businesses to youngest
sorted_businesses = businesses.sort_values(by="year_founded")

# Display the first few lines of sorted_businesses
print("\nThe first few lines of sorted_businesses:\n")
print(sorted_businesses.head(), "\n")



# Load countries.csv to a DataFrame
countries = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/oldest_business_dataset/countries.csv")

# Merge sorted_businesses with countries
businesses_countries = sorted_businesses.merge(countries, on="country_code" )

# Filter businesses_countries to include countries in North America only
north_america = businesses_countries[businesses_countries["continent"] == "North America"]
print("\nNorth America only:\n")
print(north_america.head(), "\n")



# Create continent, which lists only the continent and oldest year_founded
continent = businesses_countries[["continent", "year_founded"]].sort_values(by="year_founded").drop_duplicates(subset="continent").set_index("continent")

# Merge continent with businesses_countries
merged_continent = continent.merge(businesses_countries, on=["continent", "year_founded"])

# Subset continent so that only the four columns of interest are included
subset_merged_continent = merged_continent[["continent", "country", "business", "year_founded"]]
print("\ncontinent, country, business, year_founded columns:\n")
print(subset_merged_continent, "\n")



# Use .merge() to create a DataFrame, all_countries
all_countries = businesses.merge(countries, on="country_code", how="right",  indicator=True)

# Filter to include only countries without oldest businesses
missing_countries = all_countries[all_countries["_merge"] != "both"]

# Create a series of the country names with missing oldest business data
missing_countries_series = missing_countries["country"]

# Display the series
print("\nSeries of the country names with missing oldest business data:\n")
print(missing_countries_series, "\n")



# Import new_businesses.csv
new_businesses = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/oldest_business_dataset/new_businesses.csv")

# Add the data in new_businesses to the existing businesses
all_businesses = pd.concat([new_businesses, businesses])

# Merge and filter to find countries with missing business data
new_all_countries = all_businesses.merge(countries, on="country_code", how="outer",  indicator=True)
new_missing_countries = new_all_countries[new_all_countries["_merge"] != "both"]

# Group by continent and create a "count_missing" column
count_missing = new_missing_countries.groupby("continent").agg({"country":"count"})
count_missing.columns = ["count_missing"]
print("\nThe count of missing countries in each continent:\n")
print(count_missing, "\n")



# Import categories.csv and merge to businesses
categories = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/oldest_business_dataset/categories.csv")
businesses_categories = businesses.merge(categories, on="category_code")

# Create a DataFrame which lists the number of oldest businesses in each category
count_business_cats = businesses_categories.groupby("category").agg({"business":"count"})

# Rename column and display the first five rows of the DataFrame
count_business_cats.columns = ["count"]
print(count_business_cats.head())



# Filter using .query() for CAT4 businesses founded before 1800; sort results
old_restaurants = businesses_categories.query('category_code =="CAT4" and year_founded < 1800')

# Sort the DataFrame
sorted_old_restaurants = old_restaurants.sort_values(by="year_founded", ascending=True)
print(sorted_old_restaurants)