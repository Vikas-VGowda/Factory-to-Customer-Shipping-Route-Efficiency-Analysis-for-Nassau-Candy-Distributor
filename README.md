# Factory-to-Customer Shipping Route Efficiency Analysis

## Project Overview

The Factory-to-Customer Shipping Route Efficiency Analysis project focuses on evaluating shipping performance across multiple factory-to-customer routes within the Nassau Candy distribution network. The objective is to identify efficient and inefficient shipping routes, analyze delivery lead times, evaluate shipping modes, and uncover operational bottlenecks that may affect overall supply chain performance.

Using data cleaning, exploratory data analysis (EDA), route performance analysis, and interactive dashboard development, this project provides valuable insights into logistics efficiency and delivery operations.

---

## Problem Statement

Efficient transportation and logistics are critical components of supply chain management. Delays in shipping routes can increase operational costs, reduce customer satisfaction, and negatively impact business performance.

This project aims to:

- Analyze shipping lead times across different routes.
- Identify the fastest and slowest shipping routes.
- Compare shipping performance across regions and shipping methods.
- Monitor sales and profit metrics alongside logistics performance.
- Build an interactive dashboard for route monitoring and business decision-making.

---

## Objectives

- Clean and prepare shipping data for analysis.
- Calculate shipment lead times.
- Analyze shipping performance by region.
- Evaluate the effectiveness of different shipping methods.
- Identify top-performing and underperforming routes.
- Generate actionable insights through data visualization.
- Develop an interactive Streamlit dashboard for business users.

---

## Dataset Description

The dataset contains shipment-level records including customer, location, product, sales, and shipping information.

### Key Features

| Feature | Description |
|----------|------------|
| Order ID | Unique order identifier |
| Order Date | Date when the order was placed |
| Ship Date | Date when the order was shipped |
| Ship Mode | Shipping method used |
| Customer ID | Unique customer identifier |
| City | Customer city |
| State/Province | Customer state |
| Region | Geographic sales region |
| Product ID | Product identifier |
| Product Name | Product description |
| Sales | Revenue generated |
| Gross Profit | Profit generated |
| Factory | Manufacturing location |
| Lead Time | Shipping duration |
| Factory_State_Route | Factory-to-destination route |

---

# Tools & Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly Express
- Streamlit

## Development Environment

- Google Colab
- Visual Studio Code

## Dashboard Framework

- Streamlit

## Version Control

- GitHub

---

# Data Cleaning

The dataset underwent several preprocessing steps to improve quality and consistency.

## Cleaning Steps

- Checked dataset dimensions and structure.
- Inspected data types.
- Checked for missing values.
- Removed duplicate records.
- Converted date columns into datetime format.
- Created Lead Time feature.
- Generated Factory_State_Route feature.
- Validated data consistency.

### Lead Time Calculation

```python
Lead Time = Ship Date - Order Date
```

### Route Creation

```python
Factory_State_Route = Factory + " → " + State/Province
```

---

# Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to identify patterns, trends, and inefficiencies in the shipping process.

---

## 1. Lead Time Distribution

### Objective

Analyze shipment duration and identify unusual delivery patterns.

### Findings

- Lead times vary across shipments.
- Certain routes experience significantly longer delivery times.
- Lead time distribution helps identify operational bottlenecks.

### Business Impact

Understanding lead time behavior enables logistics teams to improve delivery efficiency and customer satisfaction.

---

## 2. Regional Order Distribution

### Objective

Examine shipment volumes across different geographic regions.

### Findings

- Pacific and Atlantic regions contributed the highest number of orders.
- Gulf region recorded comparatively lower shipment volume.
- Regional demand patterns vary considerably.

### Business Impact

Helps allocate logistics resources according to regional demand.

---

## 3. Ship Mode Analysis

### Objective

Evaluate the popularity and performance of shipping methods.

### Findings

- Standard Class is the most frequently used shipping mode.
- First Class and Same Day services account for smaller shipment volumes.
- Different shipping methods exhibit different operational characteristics.

### Business Impact

Supports optimization of shipping service offerings and logistics planning.

---

## 4. Sales Distribution Analysis

### Objective

Analyze revenue generation patterns.

### Findings

- Revenue varies significantly across orders.
- Some products contribute substantially more sales than others.
- High-value orders influence overall business performance.

### Business Impact

Helps identify important revenue-generating products and routes.

---

## 5. Profit Distribution Analysis

### Objective

Evaluate profitability across shipments.

### Findings

- Most transactions generate positive profit.
- Profitability varies by route and product.
- Some routes may require operational improvements to increase margins.

### Business Impact

Supports profit optimization and strategic decision-making.

---

# Route Performance Analysis

Route-level analysis was conducted to evaluate logistics efficiency.

---

## Fastest Routes Analysis

### Objective

Identify the routes with the lowest average lead time.

### Method

Routes were grouped using the Factory_State_Route feature and ranked according to average lead time.

### Findings

- Several routes consistently achieve low delivery times.
- These routes demonstrate strong operational efficiency.
- They can serve as benchmarks for other routes.

### Metrics Used

- Average Lead Time
- Number of Shipments

---

## Slowest Routes Analysis

### Objective

Identify routes with the highest average lead time.

### Method

Routes were ranked according to average lead time in descending order.

### Findings

- Certain routes experience significantly longer delivery times.
- These routes may contain transportation or operational bottlenecks.
- Further investigation is recommended.

### Metrics Used

- Average Lead Time
- Number of Shipments

---

# Dashboard Development

An interactive dashboard was developed using Streamlit for real-time route analysis.

---

## Dashboard Features

### KPI Cards

The dashboard provides:

- Total Orders
- Average Lead Time
- Total Sales
- Total Profit

---

### Interactive Filters

Users can filter data using:

- Region
- Ship Mode

---

### Visualizations Included

#### Average Lead Time by Region

Compares delivery performance across different geographic regions.

#### Average Lead Time by Ship Mode

Evaluates shipping method efficiency.

#### Top 10 Fastest Routes

Displays the routes with the shortest average delivery times.

#### Bottom 10 Slowest Routes

Highlights routes requiring operational improvement.

#### Dataset Preview

Provides quick access to filtered shipment records.

---

# Key Insights

## Logistics Performance

- Delivery performance varies considerably across routes.
- Some routes consistently outperform others.

## Regional Trends

- Regional shipment demand differs significantly.
- Demand influences logistics workload and delivery performance.

## Shipping Methods

- Standard Class dominates shipment volume.
- Different shipping modes exhibit similar lead time behavior.

## Route Optimization

- Fast-performing routes can be used as operational benchmarks.
- Slow-performing routes highlight opportunities for process improvement.

---

# Business Recommendations

- Investigate routes with excessive lead times.
- Improve transportation planning for underperforming routes.
- Continuously monitor route-level KPIs.
- Optimize shipping mode allocation.
- Use dashboard insights for data-driven logistics decisions.

---

# Conclusion

This project successfully analyzed factory-to-customer shipping routes using data cleaning, exploratory data analysis, route performance evaluation, and dashboard visualization techniques.

The Streamlit dashboard provides an interactive platform for monitoring logistics performance, identifying bottlenecks, and supporting strategic decision-making. By leveraging route-level insights, organizations can improve delivery efficiency, reduce delays, and enhance overall supply chain operations.


# Author

**Vikas Gowda**
