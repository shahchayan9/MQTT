import pandas as pd
import json
from collections import defaultdict

# Load CSV files for each reservoir
oroville_df = pd.read_csv('Oroville_WML.csv')
shasta_df = pd.read_csv('Shasta_WML.csv')
sonoma_df = pd.read_csv('Sonoma_WML.csv')

# Convert the data for each reservoir into JSON format
oroville_json = oroville_df.to_json(orient='records', date_format='iso')
shasta_json = shasta_df.to_json(orient='records', date_format='iso')
sonoma_json = sonoma_df.to_json(orient='records', date_format='iso')

# Convert JSON strings into Python objects
oroville_data = json.loads(oroville_json)
shasta_data = json.loads(shasta_json)
sonoma_data = json.loads(sonoma_json)

# Aggregate daily data
daily_reports = defaultdict(lambda: {"Oroville_TAF": 0, "Shasta_TAF": 0, "Sonoma_TAF": 0})

for entry in oroville_data:
    daily_reports[entry["Date"]]["Oroville_TAF"] = entry["TAF"]

for entry in shasta_data:
    daily_reports[entry["Date"]]["Shasta_TAF"] = entry["TAF"]

for entry in sonoma_data:
    daily_reports[entry["Date"]]["Sonoma_TAF"] = entry["TAF"]

# Convert aggregated data into a list of daily reports
aggregated_reports = [{"Date": date, **report} for date, report in daily_reports.items()]

# Convert to DataFrame and save to a CSV file
daily_report_df = pd.DataFrame(aggregated_reports)
daily_report_df.to_csv('reports/daily_reports.csv', index=False)

print("Daily reports have been generated and saved to 'reports/daily_reports.csv'.")
