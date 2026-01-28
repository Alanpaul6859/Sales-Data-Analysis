
import pandas as pd

df = pd.read_csv("sales_data.csv")

df.drop_duplicates(inplace=True)

for col in df.select_dtypes(include=["int64", "float64"]):
    df[col].fillna(df[col].median(), inplace=True)

for col in df.select_dtypes(include=["object"]):
    df[col].fillna("Unknown", inplace=True)

total_revenue = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

print("Total Revenue:", total_revenue)
print("Average Sales:", average_sales)
print("Best Product:", best_product)
