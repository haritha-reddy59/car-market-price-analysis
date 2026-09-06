import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/cardekho_dataset.csv/cardekho_dataset.csv")
df = df.drop(columns=['Unnamed: 0'])
df = df.drop_duplicates()
df = df[df['vehicle_age'] > 0]
df = df[df['seats'] > 0]

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset size
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data information
print("\nDataset information:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nStatistical summary:")
print(df.describe())
print("\nData types:")
print(df.dtypes)
print("\nUnique values:")
print("Brands:", df['brand'].nunique())
print("Seller types:", df['seller_type'].nunique())
print("Fuel types:", df['fuel_type'].nunique())
print("Transmission types:", df['transmission_type'].nunique())
print("\nFuel types:")
print(df['fuel_type'].unique())

print("\nTransmission types:")
print(df['transmission_type'].unique())

print("\nSeller types:")
print(df['seller_type'].unique())
print("\nInvalid values:")
print("Vehicle age <= 0:", (df['vehicle_age'] <= 0).sum())
print("KM driven <= 0:", (df['km_driven'] <= 0).sum())
print("Mileage <= 0:", (df['mileage'] <= 0).sum())
print("Engine <= 0:", (df['engine'] <= 0).sum())
print("Max power <= 0:", (df['max_power'] <= 0).sum())
print("Seats <= 0:", (df['seats'] <= 0).sum())
print("Selling price <= 0:", (df['selling_price'] <= 0).sum())
df.to_csv("data/cleaned_cardekho_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final shape:", df.shape)
print("\nTop 10 Car Brands:")
print(df['brand'].value_counts().head(10))
print("\nAverage Selling Price by Brand:")
print(
    df.groupby('brand')['selling_price']
      .mean()
      .sort_values(ascending=False)
      .head(10)
)
print("\nTop 10 Most Expensive Cars:")
print(
    df[['brand', 'model', 'selling_price']]
      .sort_values('selling_price', ascending=False)
      .head(10)
)
print("\nAverage Selling Price by Fuel Type:")
print(
    df.groupby('fuel_type')['selling_price']
      .mean()
      .sort_values(ascending=False)
)
print("\nAverage Selling Price by Transmission:")
print(
    df.groupby('transmission_type')['selling_price']
      .mean()
      .sort_values(ascending=False)
)

print("\nAverage Selling Price by Vehicle Age:")
print(
    df.groupby('vehicle_age')['selling_price']
      .mean()
      .sort_index()
)
print("\nNumber of Cars by Fuel Type:")
print(df['fuel_type'].value_counts())
df.groupby('fuel_type')['selling_price'].mean()
df['fuel_type'].value_counts()

import matplotlib.pyplot as plt

# Top 10 car brands
brand_counts = df['brand'].value_counts().head(10)

plt.figure(figsize=(10, 6))
brand_counts.plot(kind='bar')

plt.title('Top 10 Car Brands')
plt.xlabel('Brand')
plt.ylabel('Number of Cars')
plt.xticks(rotation=45)
plt.tight_layout()
plt.tight_layout()
plt.savefig("images/top_10_car_brands.png", bbox_inches="tight")
plt.show()
plt.close()

# Average selling price by brand
avg_price_brand = (
    df.groupby('brand')['selling_price']
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 6))
avg_price_brand.plot(kind='bar')

plt.title('Top 10 Brands by Average Selling Price')
plt.xlabel('Brand')
plt.ylabel('Average Selling Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.tight_layout()
plt.savefig("images/average_price_by_brand.png", bbox_inches="tight")
plt.show()
plt.close()
# Number of cars by fuel type
fuel_counts = df['fuel_type'].value_counts()

plt.figure(figsize=(8, 5))
fuel_counts.plot(kind='bar')

plt.title('Number of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.xticks(rotation=0)
plt.tight_layout()
plt.tight_layout()
plt.savefig("images/cars_by_fuel_type.png", bbox_inches="tight")
plt.show()
plt.close()
# Number of cars by transmission type
transmission_counts = df['transmission_type'].value_counts()

plt.figure(figsize=(8, 5))
transmission_counts.plot(kind='bar')

plt.title('Number of Cars by Transmission Type')
plt.xlabel('Transmission Type')
plt.ylabel('Number of Cars')
plt.xticks(rotation=0)
plt.tight_layout()
plt.tight_layout()
plt.savefig("images/cars_by_transmission.png", bbox_inches="tight")
plt.show()
plt.close()

# Average selling price by vehicle age
age_price = (
    df.groupby('vehicle_age')['selling_price']
      .mean()
      .sort_index()
)

plt.figure(figsize=(10, 6))
age_price.plot(kind='line', marker='o')

plt.title('Vehicle Age vs Average Selling Price')
plt.xlabel('Vehicle Age (Years)')
plt.ylabel('Average Selling Price')
plt.grid(True)
plt.grid(True)
plt.tight_layout()
plt.savefig("images/vehicle_age_vs_price.png", bbox_inches="tight")
plt.show()
plt.close()
# KM Driven vs Selling Price

plt.figure(figsize=(10, 6))

plt.scatter(
    df['km_driven'],
    df['selling_price'],
    alpha=0.5
)

plt.title('KM Driven vs Selling Price')
plt.xlabel('KM Driven')
plt.ylabel('Selling Price')
plt.tight_layout()
plt.tight_layout()
plt.savefig("images/km_driven_vs_price.png", bbox_inches="tight")
plt.show()
plt.close()

# Engine Size vs Selling Price

plt.figure(figsize=(10, 6))

plt.scatter(
    df['engine'],
    df['selling_price'],
    alpha=0.5
)

plt.title('Engine Size vs Selling Price')
plt.xlabel('Engine (CC)')
plt.ylabel('Selling Price')
plt.tight_layout()
plt.tight_layout()
plt.savefig("images/engine_vs_price.png", bbox_inches="tight")
plt.show()
plt.close()
# Max Power vs Selling Price

plt.figure(figsize=(10, 6))

plt.scatter(
    df['max_power'],
    df['selling_price'],
    alpha=0.5
)

plt.title('Max Power vs Selling Price')
plt.xlabel('Max Power (bhp)')
plt.ylabel('Selling Price')
plt.tight_layout()
plt.savefig("images/max_power_vs_price.png", bbox_inches="tight")
plt.show()
plt.close()
# Mileage vs Selling Price

plt.figure(figsize=(10, 6))

plt.scatter(
    df['mileage'],
    df['selling_price'],
    alpha=0.5
)

plt.title('Mileage vs Selling Price')
plt.xlabel('Mileage (km/l)')
plt.ylabel('Selling Price')
plt.tight_layout()
plt.tight_layout()
plt.savefig("images/mileage_vs_price.png", bbox_inches="tight")
plt.show()
plt.close()
# Correlation with Selling Price

print("\nCorrelation with Selling Price:")

correlation = df[
    ['vehicle_age', 'km_driven', 'mileage',
     'engine', 'max_power', 'selling_price']
].corr()['selling_price'].sort_values(ascending=False)

print(correlation)
print("\nFinal Columns for SQL:")
print(df.columns.tolist())
print("\nBrand Count:")
print(df['brand'].value_counts())
