# End-to-End E-Commerce Business Intelligence and Analytics Platform

## 📌 Project Overview

The **End-to-End E-Commerce Business Intelligence and Analytics Platform** is a complete Business Intelligence and Data Analytics solution developed for analyzing Flipkart e-commerce product data.

This project transforms raw e-commerce data into meaningful business insights using:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- SQL-Based Analytics
- Interactive Power BI Dashboard

The platform helps businesses analyze:
- Product categories
- Pricing trends
- Discounts
- Brand performance
- Ratings distribution
- Product segmentation

The final deliverable is an interactive **Power BI Dashboard** for business decision-making.

---

# 🎯 Objectives

- Build a complete end-to-end analytics pipeline
- Perform data cleaning and preprocessing
- Analyze e-commerce business data using Python and SQL
- Generate interactive visualizations
- Develop a Power BI Business Intelligence dashboard
- Enable data-driven decision-making

---

# 🛠 Technology Stack & Tools Used

## Programming Language
- Python 3.9+

## Python Libraries
- Pandas
- NumPy
- Matplotlib
- SQLAlchemy

## Database
- SQLite
- MySQL

## BI & Visualization Tool
- Microsoft Power BI Desktop

## Data Processing Tools
- Microsoft Excel
- Power Query

## IDEs & Platforms
- VS Code
- Jupyter Notebook
- SQLite Browser
- Power BI Desktop

---

# ✨ Features & Functionalities

## ✅ Data Cleaning & Preprocessing
- Missing value handling
- Duplicate removal
- Data type conversion
- Date formatting
- Feature engineering

## ✅ Exploratory Data Analysis (EDA)
- Product category analysis
- Pricing analysis
- Discount analysis
- Ratings analysis
- Brand analysis

## ✅ SQL-Based Analytics
- Aggregation queries
- Category analysis
- Brand analysis
- Price analysis
- Discount evaluation

## ✅ Interactive Power BI Dashboard
- KPI Cards
- Interactive slicers
- Dynamic filtering
- Charts & graphs
- Business insight generation

---

# 📂 Project Workflow

```text
Raw CSV Dataset
       ↓
Data Cleaning (Excel + Python)
       ↓
EDA using Pandas & Matplotlib
       ↓
SQL Database Analysis
       ↓
Power BI Dashboard Development
       ↓
Business Intelligence Insights
```

---

# 📊 Final Project Output

## 🎯 Power BI Dashboard

The dashboard provides:
- Total Products KPI
- Average Price KPI
- Average Discount KPI
- Average Rating KPI
- Total Discount Saved KPI
- Product category analysis
- Brand analysis
- Price range segmentation
- Ratings overview
- Retail vs Discounted Price comparison

---

## 🖼 Dashboard Screenshot

```md
![Flipkart E-Commerce Analytics Dashboard](screenshots/dashboard_final.png)
```

> Save your dashboard screenshot inside:
>
> `screenshots/dashboard_final.png`

---

# ❓ Business Questions Solved Using SQL Queries

## 1. Top Product Categories by Product Count

```sql
SELECT product_category_tree, COUNT(*) AS total_products
FROM Flipkart
GROUP BY product_category_tree
ORDER BY total_products DESC;
```

### Purpose
Identifies categories with the highest number of products.

---

## 2. Average Price by Category

```sql
SELECT product_category_tree, AVG(retail_price) AS avg_price
FROM Flipkart
GROUP BY product_category_tree;
```

### Purpose
Analyzes average product pricing across categories.

---

## 3. Categories with Highest Discounts

```sql
SELECT product_category_tree, AVG(discount_percent) AS avg_discount
FROM Flipkart
GROUP BY product_category_tree
ORDER BY avg_discount DESC;
```

### Purpose
Finds categories offering the highest discounts.

---

## 4. Top 5 Brands by Product Listings

```sql
SELECT brand, COUNT(*) AS product_count
FROM Flipkart
GROUP BY brand
ORDER BY product_count DESC
LIMIT 5;
```

### Purpose
Displays brands with the maximum product listings.

---

## 5. Average Rating by Category

```sql
SELECT product_category_tree, AVG(overall_rating) AS avg_rating
FROM Flipkart
GROUP BY product_category_tree
ORDER BY avg_rating DESC;
```

### Purpose
Evaluates customer satisfaction by category.

---

## 6. Total Discount Value Offered

```sql
SELECT SUM(retail_price - discounted_price) AS total_discount_saved
FROM Flipkart;
```

### Purpose
Calculates total savings provided through discounts.

---

## 7. Product Distribution by Price Range

```sql
SELECT price_range, COUNT(*) AS product_count
FROM Flipkart
GROUP BY price_range;
```

### Purpose
Analyzes distribution of products across price ranges.

---

# 📈 Dashboard Insights

- Clothing and Computers are dominant product categories.
- Most products belong to low and medium price ranges.
- Discounts significantly influence purchasing behavior.
- Certain brands dominate marketplace listings.
- Product ratings are generally positive.

---

# ⚙ Installation & Execution Steps

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/ecommerce-bi-platform.git
cd ecommerce-bi-platform
```

---

## Step 2: Install Required Libraries

```bash
pip install pandas numpy matplotlib sqlalchemy
```

---

## Step 3: Add Dataset

Place the raw CSV dataset inside the `/data` folder.

Example:

```bash
/data/ecommerce_raw.csv
```

---

## Step 4: Run Data Cleaning Script

```bash
python data_cleaning.py
```

This generates:
- Cleaned dataset
- Processed analytical data

---

## Step 5: Setup Database

```bash
python db_setup.py
```

This creates:
- SQLite database
- Structured relational tables

---

## Step 6: Open Power BI Dashboard

1. Open Power BI Desktop
2. Open the `.pbix` dashboard file
3. Refresh data connections if required

---

# 📁 Project Structure

```bash
project/
│
├── data/
│   ├── ecommerce_raw.csv
│   └── ecommerce_clean.csv
│
├── scripts/
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   └── db_setup.py
│
├── database/
│   └── ecommerce.db
│
├── dashboard/
│   └── Ecommerce_Dashboard.pbix
│
├── screenshots/
│   └── dashboard_final.png
│
└── README.md
```

---

# 🧪 Testing Performed

- Data Validation Testing
- SQL Query Testing
- Python Unit Testing
- Integration Testing
- Dashboard Testing

---

# 👨‍💻 Team Members

| Name | Enrollment Number |
|------|-------------------|
| Namami Verma | EN23CS301649 |
| Mohit Mukati | EN23CS301633 |

---

# 🚀 Future Scope

- Real-time data integration
- Machine learning based forecasting
- Cloud deployment
- Automated ETL pipelines
- Mobile dashboard optimization
- Natural language querying
- Advanced customer analytics

---

# 📚 References

- Power BI Documentation
- Pandas Documentation
- NumPy Documentation
- Kaggle E-Commerce Dataset

---

# 📌 Conclusion

This project successfully demonstrates the implementation of a complete Business Intelligence and Analytics workflow for e-commerce data using Python, SQL, and Power BI.

The platform enables businesses to generate actionable insights through interactive visualizations and data-driven analytics.

---

# ⭐ Repository Guidelines

- Ensure the repository is public for evaluation.
- Upload:
  - Source code
  - Dataset (if allowed)
  - Power BI dashboard (.pbix)
  - Screenshots
  - README.md
- Verify all repository links and files are accessible properly.
