from supabase import create_client
import pandas as pd

URL = "https://llpbjoyengtehjvaqwbg.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxscGJqb3llbmd0ZWhqdmFxd2JnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTQ1MTEyNjEsImV4cCI6MjExMDA4NzI2MX0.cvAKz7jI5L6_cj-0UUJFzrSlO57NlEUrzxdZ1KORhos"

def get_county_report(county, start_date, end_date):
    supabase = create_client(URL, KEY)
    
    # Parameterized 
    response = supabase.table("orders").select("*").eq("county", county).execute()
    
    df = pd.DataFrame(response.data)
    
    if df.empty:
        print(f"No results for {county}")
        return pd.DataFrame(columns=["product", "total_orders", "total_quantity", "total_revenue_kes"])
    
    summary = df.groupby("product").agg(
        total_orders=("product", "count"),
        total_quantity=("quantity", "sum"),
        total_revenue_kes=("total_value", "sum")
    ).reset_index()
    
    return summary

#test
r = '=' *38
print(r)
print('KISUMU TEST REPORT.')
print(r)
print(get_county_report("Kisumu", "2024-01-01", "2024-12-31"))

print()

print(r)
print('KAKAMEGA TEST REPORT.')
print(r)
print(get_county_report("Kakamega", "2024-01-01", "2024-12-31"))

print(r)
print('SIAYA TRST REPORT')
print(r)
print(get_county_report("Siaya", "2024-01-01", "2024-12-31"))
