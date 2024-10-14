import pandas as pd

# Sample data
data = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Product_Name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics'],
    'Price': [1200, 800, 400, 100, 300],
    'Quantity_Sold': [50, 100, 80, 200, 120]
}

products = pd.DataFrame(data)

print("Arithmetic")
total = products["Price"] * products["Quantity_Sold"]
print(total)
print(total.sum())

print("Statistical")
print(products["Price"].mean())
print(products["Price"].median())
print(products["Quantity_Sold"].mean())
print(products["Quantity_Sold"].median())

print("Merging")
print(pd.concat([products, products], axis=1))

print("Missing Values")
products.loc[2, "Price"] = pd.NA
products.loc[3, "Quantity_Sold"] = pd.NA
print(products)
print(products[["Price", "Quantity_Sold"]].fillna(products[["Price", "Quantity_Sold"]].mean()))
list = products.dropna()
print(list)