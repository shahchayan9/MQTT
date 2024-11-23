# Water Reservoir Data Analysis

This project analyzes water mark levels (WML) from multiple reservoirs in California. The data is aggregated and used to generate daily reports on the water availability for each reservoir.

## Files

- Contains CSV files with water mark levels (WML) for different reservoirs (e.g., Oroville, Shasta, Sonoma).
- Contains Python scripts for processing the data and generating reports.
- Contains generated daily reports.

## How to Use

1. Run the Python scripts in `scripts/` to generate daily reports.
2. The data will be output in JSON format and aggregated into daily summaries.

## Technologies

- Python
- Pandas (for data manipulation)
- MQTT (for data transmission)

## Installation

Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/Water-Reservoir-Data-Analysis.git
```

## Water-Reservoir-Data-Analysis/
```
├── Oroville_WML.csv
├── Shasta_WML.csv
├── Sonoma_WML.csv
├── daily_reports.csv  # The generated report
├── data_processing.py  # The Python script for data processing
├── mqtt_publisher.py   # The Python script for MQTT publishing (optional)
└── README.md
```
