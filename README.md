# mini-data-warehouse
Mini project to handle data storage

```plaintext
mini_data_warehouse/
│
├── data/
│   ├── raw/              # CSVs go here
│   └── warehouse.db      # SQLite database file
│
├── sql/
│   ├── schema.sql        # CREATE TABLE statements
│   └── queries.sql       # (optional) saved analytic queries
│
├── src/
│   ├── db.py             # connection helpers + run_query()
│   ├── load_data.py      # load CSVs into tables
│   ├── analytics.py      # Python functions that call SQL + return insights
│   └── __init__.py
│
└── main.py               # simple CLI or demo script to run analyses
```

## Examples of Analytics Provided
- **Total Sales**: Calculate the total sales from the sales data.
- **Average Order Value**: Compute the average value of orders over a specified period.
- **Customer Segmentation**: Analyze customer data to segment them based on purchasing behavior.
- **Monthly Trends**: Generate reports on sales trends month-over-month.
