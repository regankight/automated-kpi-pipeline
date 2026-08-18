# Automated KPI Report Pipeline

Python KPI reporting pipeline built against generated CRM-style data, with data cleaning, KPI calculation, refresh orchestration, and failure handling.

## Overview

This project implements a lightweight KPI reporting workflow using generated CRM-style data. It cleans incomplete, duplicated, and inconsistent records, calculates conversion rate, average deal size, and deal velocity, and runs the reporting workflow with basic failure handling.

## Pipeline Design

- **ETL modularity:** Python pipeline organized as `generate → clean → calculate → notify`.
- **Data validation:** Null filtering, duplicate removal, date coercion, and missing-value handling.
- **Report output:** Calculates conversion rate, average deal size, and average deal velocity from cleaned CRM-style data.
- **Refresh and failure handling:** Runs the reporting workflow and catches failures through a notification function.

All code is fully modular and executable via `main.py`, with output stored in the `output/` directory.

## Use Case

The project showcases how to build a lightweight automated reporting solution without needing heavy backend infrastructure. It combines data cleaning, KPI calculation, and a simulated refresh process, similar to how BI and RevOps teams streamline reporting workflows.

## Key Features

- **Data Generation:** Simulates messy, real-world CRM data (incomplete, duplicated, and inconsistent).
- **Data Cleaning:** Standardizes data, handles nulls, and removes duplicates.
- **KPI Calculation:** Computes conversion rates, average deal size, and average deal velocity.
- **Automated Refresh Simulation:** Uses a simple schedule to mimic a weekly update.
- **Failure Alert Simulation:** Provides basic error handling through simulated alerts.

## Technologies Used

- **Python:** Core logic and automation simulation.
- **Pandas:** Data manipulation and cleaning.
- **NumPy:** Data generation and randomization.

## Project Structure

```
automated-kpi-dashboard/
├── data_generator.py       # Simulates messy CRM data
├── data_cleaning.py        # Cleans and standardizes data
├── kpi_calculator.py       # Calculates key sales metrics
├── notification_sim.py     # Simulates failure notifications
├── output/                 # Folder for saved .csv report
├── main.py                 # Runs the full pipeline
└── README.md               # Project documentation
```

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/regankight/automated-kpi-dashboard.git
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. View the KPI report in your terminal and as a CSV in the `output/` folder.


## Connect with Me

Check out more of my work on GitHub or [LinkedIn](https://www.linkedin.com/in/regankight).
