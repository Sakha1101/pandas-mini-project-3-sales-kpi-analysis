\# Sales KPI \& Performance Analysis



\## Project Objective



This project analyzes sales performance to identify key business drivers, profitable regions, strong product categories, and areas of profit leakage using Python and Pandas.



\---



\## Dataset Information



The dataset contains 850+ sales records with realistic business issues such as:



\* Missing values

\* Duplicate entries

\* Mixed date formats

\* Inconsistent category names

\* Incorrect data types

\* Negative profit cases



\### Columns Used



\* Order\_ID

\* Customer\_ID

\* Region

\* Product

\* Category

\* Sales

\* Cost

\* Profit

\* Quantity

\* Order\_Date



\---



\## Data Cleaning Performed



\* Standardized Region and Category names

\* Converted Sales, Cost, Quantity, and Order\_Date into proper data types

\* Removed rows with missing Sales and Order\_Date values

\* Removed duplicate records

\* Kept negative profit values because they represent actual business loss



\---



\## Feature Engineering



Created new business metrics:



\* Profit\_Margin

\* Revenue\_Category

\* Year\_Month for trend analysis



\---



\## KPI Metrics



The following KPIs were created:



\* Total Revenue

\* Total Profit

\* Average Order Value (AOV)

\* Profit Margin %



\---



\## Analysis Performed



\### Region-wise Performance



Analyzed:



\* Revenue contribution

\* Profit contribution

\* Profitability by region



\### Category-wise Performance



Compared:



\* High-performing categories

\* Low-margin categories



\### Product Analysis



Identified:



\* Top products by revenue

\* Top products by profit

\* High-margin products

\* Profit leakage products



\### Monthly Trend Analysis



Tracked:



\* Monthly revenue trend

\* Monthly profit trend

\* Monthly profitability trend



\---



\## Key Business Insights



\* South region generated the highest revenue.

\* West region showed stronger profitability efficiency.

\* Home and Kitchen category performed strongly in both revenue and profit margin.

\* Bottle generated high revenue but relatively lower profit margin, indicating possible profit leakage.

\* Fan and TV appeared as core business-driving products due to strong revenue and profit contribution.

\* High profit margin alone does not guarantee high total profit contribution.



\---



\## Business Recommendations



\* Focus on products generating both high revenue and strong profitability.

\* Investigate low-margin high-revenue products for discount or operational leakage.

\* Increase sales efforts for high-margin products with lower volume.

\* Track revenue and profit together instead of focusing only on sales growth.



\---



\## Tools \& Technologies Used



\* Python

\* Pandas

\* NumPy

\* Jupyter Notebook



\---



\## Project Files



\* Sales KPI Analysis.py

\* sales\_mini\_project\_3\_full.csv

\* region\_performance.csv

\* category\_performance.csv

\* product\_performance.csv

\* monthly\_trend.csv



