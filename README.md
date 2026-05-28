# End-to-End Business Analytics and Intelligence Platform

## Project Overview

The **End-to-End Business Analytics and Intelligence Platform** is a mini project developed to analyze Flipkart e-commerce product data and generate meaningful business insights using Python, SQL, and Power BI.
The project focuses on building a complete analytics pipeline starting from raw data processing to interactive dashboard visualization. It demonstrates how Business Intelligence and Analytics tools can help organizations make data-driven decisions.

## Problem Statement

E-commerce platforms generate massive amounts of product and customer-related data every day. However, raw data alone cannot help businesses make effective decisions unless it is properly processed and analyzed.
The main problem addressed in this project was to transform unstructured and raw Flipkart product data into meaningful business insights using analytics and visualization techniques.

This project helps solve problems such as:
- Identifying top-performing product categories
- Understanding pricing and discount trends
- Analyzing customer ratings and product performance
- Comparing retail and discounted prices
- Understanding brand-wise product distribution
- Generating insights for better business decision-making

By building an end-to-end analytics pipeline using Python, SQL, and Power BI, the project demonstrates how raw e-commerce data can be converted into interactive dashboards and actionable insights.

## Objectives

- Perform data cleaning and preprocessing
- Analyze e-commerce product data
- Build SQL-based business queries
- Create interactive Power BI dashboards
- Generate actionable business insights
- Understand the complete Business Intelligence workflow

## Technologies & Tools Used
### Programming & Analysis
- Python
- Pandas
- NumPy
- Matplotlib

### Database
- SQLite / SQL

### Visualization
- Microsoft Power BI

### Development Tools
- VS Code
- Jupyter Notebook
- Power Query
- Microsoft Excel

## Complete Analytics Pipeline

The project was completed through the following pipeline:

Raw Flipkart Dataset
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis (EDA)
        ↓
SQL Database Integration
        ↓
Business Query Analysis
        ↓
Power BI Dashboard Development
        ↓
Business Insights & Reporting

## Project Workflow
 1. Data Collection
The raw Flipkart e-commerce dataset was collected in CSV format containing product information such as:
- Product Name
- Category
- Brand
- Retail Price
- Discounted Price
- Ratings
- Product Description

 2. Data Cleaning & Preprocessing
Data preprocessing was performed using Python and Pandas:
- Removed duplicate records
- Handled missing values
- Converted data types
- Processed pricing columns
- Structured dataset for analysis

3. Exploratory Data Analysis (EDA)
EDA was performed to understand business trends and product behavior:
- Product category analysis
- Brand analysis
- Discount analysis
- Pricing analysis
- Rating distribution analysis

Graphs and visualizations were created using Matplotlib.

 4. SQL-Based Analytics
The cleaned dataset was integrated with SQL for business query analysis.

Some business queries performed:
- Top product categories
- Average product pricing
- Brand-wise product count
- Highest discount categories
- Product distribution by price range

5. Power BI Dashboard Development
An interactive dashboard was created in Power BI to visualize business insights.

Dashboard Features:
- KPI Cards
- Interactive Filters
- Product Category Analysis
- Price Comparison Charts
- Discount Insights
- Ratings Overview

## Dashboard Preview

- Flipkart_Dashboard(1).pbix → Power BI dashboard

## Files Included

- mini_project_pycode.py → Python analysis and preprocessing code
- cleaned_flipkart_dataset.csv→ Cleaned dataset
- Flipkart_Dashboard(1).pbix→ Power BI dashboard
- Namanireport.pdf → Project report
- screenshots -> SQL queries with output

## Business Questions Solved Using SQL Queries

### i. Top Product Categories by Product Count

SELECT product_category_tree, COUNT(*) AS total_products
FROM Flipkart
GROUP BY product_category_tree
ORDER BY total_products DESC;

### ii. Average Price by Category

SELECT product_category_tree, AVG(retail_price) AS avg_price
FROM Flipkart
GROUP BY product_category_tree;

### iii. Categories with Highest Discounts

SELECT product_category_tree, AVG(discount_percent) AS avg_discount
FROM Flipkart
GROUP BY product_category_tree
ORDER BY avg_discount DESC;

### iv. Top 5 Brands by Product Listings

SELECT brand, COUNT(*) AS product_count
FROM Flipkart
GROUP BY brand
ORDER BY product_count DESC
LIMIT 5;

### v. Average Rating by Category

SELECT product_category_tree, AVG(overall_rating) AS avg_rating
FROM Flipkart
GROUP BY product_category_tree
ORDER BY avg_rating DESC;

### vi. Total Discount Value Offered

SELECT SUM(retail_price - discounted_price) AS total_discount_saved
FROM Flipkart;

### vii. Product Distribution by Price Range

SELECT price_range, COUNT(*) AS product_count
FROM Flipkart
GROUP BY price_range;

## Key Insights

- Clothing and electronics categories contain the highest number of products.
- Most products belong to low and medium price ranges.
- Discounts significantly influence customer purchasing behavior.
- Certain brands dominate marketplace listings.
- Product ratings are generally positive.

## Team Members

- Namami Verma(EN23CS301649)
- Mohit Mukati(EN23CS301633)

## Conclusion

This project successfully demonstrates the implementation of an end-to-end Business Analytics and Intelligence workflow using Python, SQL, and Power BI.
The platform converts raw e-commerce data into interactive visual insights that help in understanding business performance, customer behavior, pricing trends, and marketplace patterns effectively.
