

## Distributor County Report

A weekly reporting script for the distributor's operations team.
Replaces manual SQL typing in a database tool. Connects to Supabase, accepts a county name and date range, and returns a clean summary table for the Monday report.

## What It Does

- Accepts county name and date range (county, start_date, end_date)
- Connects to Supabase cloud database with parameterized query (safe, no SQL injection)
- Returns a clean summary table with product, total_orders, total_quantity, total_revenue_kes
- Handles no-results case by returning an empty DataFrame with correct columns instead of crashing

## Setup

```bash
pip install supabase pandas
Set your Supabase URL and KEY in the script:
URL = "https://llpbjoyengtehjvaqwbg.supabase.co"
KEY = "your-anon-key"
## Usage
from county_report import get_county_report

# Get Monday report for Kisumu
report = get_county_report("Kisumu", "2024-01-01", "2024-12-31")
print(report)

# Test other counties
print(get_county_report("Kakamega", "2024-01-01", "2024-12-31"))
print(get_county_report("Siaya", "2024-01-01", "2024-12-31"))
## Sample Output
              product  total_orders  total_quantity  total_revenue_kes
0      Cooking Oil 5L             1              15                25500
1   Maize Flour 2kg              1              20                12000
2         Sugar 1kg              1              25                17250
[3 rows x 4 columns]

No results for Kakamega
Empty DataFrame
Columns: [product, total_orders, total_quantity, total_revenue_kes]
Index: []

No results for Siaya
Empty DataFrame
Columns: [product, total_orders, total_quantity, total_revenue_kes]
Index: []
## Stack

Python, Supabase, pandas

