# PPG Inventory Risk Management Analytics Pipeline

## Project Overview

This project was developed as part of a cloud-based data engineering and analytics solution for PPG Industries. The objective of the project is to build an end-to-end inventory risk management pipeline using Microsoft Azure and Medallion Architecture to support business decision-making.

The system ingests multiple operational datasets, processes them through Bronze, Silver, Gold, and Curated layers, and generates business insights through Power BI dashboards.

---

## Business Problems Addressed

The project addresses the following inventory management challenges:

* Identify materials below reorder level
* Detect recoverable assets (excess inventory)
* Identify Magna Carta (MC) Dead Stock
* Detect Magna Carta (MC) Expired Materials
* Calculate inventory provision amounts
* Identify unfulfilled production orders caused by inventory shortages
* Analyze customer sales orders affected by stockout risks

---

## Architecture

The solution follows the Medallion Architecture framework:

```text
Source CSV Files
        │
        ▼
Bronze Layer
(Raw Data Storage)
        │
        ▼
Silver Layer
(Data Cleaning & Standardization)
        │
        ▼
Gold Layer
(Business Logic & Analytics)
        │
        ▼
Curated Layer
(Star Schema & Reporting)
        │
        ▼
Power BI Dashboard
```

---

## Technologies Used

### Cloud Platform

* Microsoft Azure

### Data Integration

* Azure Data Factory (ADF)

### Storage

* Azure Data Lake Storage Gen2 (ADLS)

### Data Processing

* Azure Synapse Analytics
* Serverless SQL Pool

### Reporting

* Microsoft Power BI

### File Format

* CSV
* Parquet

---

## Datasets

The project utilizes six operational datasets:

| Dataset                | Description                       |
| ---------------------- | --------------------------------- |
| materials.csv          | Material master data              |
| inventory_snapshot.csv | Monthly inventory balances        |
| purchase_orders.csv    | Procurement transactions          |
| production_orders.csv  | Manufacturing consumption records |
| suppliers.csv          | Supplier master data              |
| sales_orders.csv       | Customer sales transactions       |

---

## Gold Layer Business Logic

### Q1 – Below Reorder Level

Identify materials whose current inventory is below the predefined reorder level.

### Q2 – Recoverable Assets

Identify materials where current inventory exceeds twelve-month consumption.

### Q3 – Magna Carta Dead Stock

Identify materials with no consumption activity for at least nine months and no expiry tracking.

### Q4 – Magna Carta Expired Materials

Identify materials whose expiry date has passed.

### Q5 – Inventory Provision Calculation

Calculate financial provision amounts for obsolete inventory.

### Q6 – Unfulfilled Production Orders

Identify production orders affected by insufficient inventory.

### Q7 – Customer Sales Impact Analysis

Identify customer sales orders affected by stockout-risk materials.

---

## Gold Layer Data Extension (D1)

A custom data extension was implemented by adding the `lot_expiry_date` attribute to inventory records.

Distribution of generated expiry dates:

| Category           | Percentage |
| ------------------ | ---------- |
| Expired Materials  | 10%        |
| No Expiry Tracking | 25%        |
| Future Expiry      | 65%        |

This extension enabled the implementation of Magna Carta Expired (Q4) analysis.

---

## Data Transformation

The project transforms raw CSV datasets into Parquet format using CETAS (Create External Table As Select).

Benefits of Parquet:

* Reduced storage requirements
* Faster analytical queries
* Improved performance for Power BI reporting
* Industry-standard format for data lake architectures

---

## Dashboard Features

The Power BI dashboard provides:

* Inventory Risk Overview
* Recoverable Asset Analysis
* Dead Stock Monitoring
* Expired Inventory Tracking
* Provision Amount Analysis
* Production Risk Analysis
* Customer Sales Impact Analysis

---

## Key Outcomes

* Built an end-to-end Azure Data Engineering pipeline
* Implemented Medallion Architecture
* Developed inventory risk business logic
* Automated data transformation and analytics workflows
* Generated business-ready datasets in Parquet format
* Delivered interactive Power BI dashboards for decision support

---

## Team Contribution

My primary contributions included:

* D1 Expiry Date Data Extension
* Q6 Unfulfilled Production Analysis
* Q7 Customer Sales Impact Analysis
* Gold Layer Parquet Export using CETAS
* Gold Layer Documentation and Testing
* Azure Synapse Business Logic Development

---

