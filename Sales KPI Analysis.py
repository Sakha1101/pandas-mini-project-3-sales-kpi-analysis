# Sales KPI & Performance Analysis - Mini Project 3

import pandas as pd
import numpy as np

# ===============================
# 1. Load Dataset
# ===============================

df = pd.read_csv("sales_mini_project_3_full.csv")

pd.set_option("display.max_columns", None)

print("Initial Shape:", df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())


# ===============================
# 2. Data Cleaning
# ===============================

# Standardize Region
df["Region"] = df["Region"].str.strip().str.title()

# Standardize Category names
df["Category"] = df["Category"].str.strip().replace({
    "Home & Kitchen": "Home and Kitchen",
    "furnitures": "Furniture",
    "electronic": "Electronics"
})

# Convert Cost to numeric
df["Cost"] = df["Cost"].replace({"missing": pd.NA})
df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")

# Convert Quantity to numeric
df["Quantity"] = df["Quantity"].replace({
    "two": "2",
    "three": "3"
})
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").astype("Int64")

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce",
    format="mixed",
    dayfirst=True
)

# Convert Sales and Profit to numeric
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")


# ===============================
# 3. Cleaning Validation
# ===============================

before_shape = df.shape
before_region_dist = df["Region"].value_counts(normalize=True) * 100

# Drop critical missing values
df = df.dropna(subset=["Sales", "Order_Date"])

# Remove duplicate records
df = df.drop_duplicates()

after_shape = df.shape
after_region_dist = df["Region"].value_counts(normalize=True) * 100

print("Before Shape:", before_shape)
print("After Shape:", after_shape)
print("Rows Removed:", before_shape[0] - after_shape[0])
print("Region Distribution Before Cleaning:")
print(before_region_dist.round(2))
print("Region Distribution After Cleaning:")
print(after_region_dist.round(2))
print("Final Null Check:")
print(df.isnull().sum())


# ===============================
# 4. Feature Engineering
# ===============================

# Row-level profit margin
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

# Revenue category using rank-based qcut to handle repeated sales values
df["Revenue_Category"] = pd.qcut(
    df["Sales"].rank(method="first"),
    q=3,
    labels=["Low", "Medium", "High"]
)

# Year-Month for trend analysis
df["Year_Month"] = df["Order_Date"].dt.to_period("M")


# ===============================
# 5. KPI Summary
# ===============================

total_revenue = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
aov = total_revenue / total_orders

print("\nKPI SUMMARY")
print(f"Total Revenue: ₹{total_revenue:,.0f}")
print(f"Total Profit: ₹{total_profit:,.0f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ₹{aov:,.2f}")


# ===============================
# 6. Region-wise Performance
# ===============================

df_region = df.groupby("Region", as_index=False).agg(
    Total_Revenue=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Order_Count=("Order_ID", "nunique")
)

df_region["Profit_Margin"] = (
    df_region["Total_Profit"] / df_region["Total_Revenue"] * 100
).round(2)

df_region = df_region.sort_values(
    by="Total_Revenue",
    ascending=False
).reset_index(drop=True)

print("\nREGION-WISE PERFORMANCE")
print(df_region)


# ===============================
# 7. Category-wise Performance
# ===============================

df_category = df.groupby("Category", as_index=False).agg(
    Total_Revenue=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Order_Count=("Order_ID", "nunique")
)

df_category["Profit_Margin"] = (
    df_category["Total_Profit"] / df_category["Total_Revenue"] * 100
).round(2)

df_category = df_category.sort_values(
    by="Total_Revenue",
    ascending=False
).reset_index(drop=True)

print("\nCATEGORY-WISE PERFORMANCE")
print(df_category)


# ===============================
# 8. Product Performance
# ===============================

df_product = df.groupby("Product", as_index=False).agg(
    Total_Revenue=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

df_product["Profit_Margin"] = (
    df_product["Total_Profit"] / df_product["Total_Revenue"] * 100
).round(2)

top_products_by_revenue = df_product.sort_values(
    by="Total_Revenue",
    ascending=False
).head(5).reset_index(drop=True)

top_products_by_profit = df_product.sort_values(
    by="Total_Profit",
    ascending=False
).head(5).reset_index(drop=True)

top_products_by_margin = df_product.sort_values(
    by="Profit_Margin",
    ascending=False
).head(5).reset_index(drop=True)

print("\nTOP 5 PRODUCTS BY REVENUE")
print(top_products_by_revenue)

print("\nTOP 5 PRODUCTS BY PROFIT")
print(top_products_by_profit)

print("\nTOP 5 PRODUCTS BY PROFIT MARGIN")
print(top_products_by_margin)


# ===============================
# 9. Monthly Trend Analysis
# ===============================

df_month = df.groupby("Year_Month", as_index=False).agg(
    Total_Revenue=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

df_month["Profit_Margin"] = (
    df_month["Total_Profit"] / df_month["Total_Revenue"] * 100
).round(2)

df_month = df_month.sort_values(
    by="Year_Month"
).reset_index(drop=True)

print("\nMONTHLY SALES TREND")
print(df_month)


# ===============================
# 10. Export Final Reports
# ===============================

df_region.to_csv("region_performance.csv", index=False)
df_category.to_csv("category_performance.csv", index=False)
df_product.to_csv("product_performance.csv", index=False)
df_month.to_csv("monthly_trend.csv", index=False)

print("\nReports exported successfully.")