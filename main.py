"""Main script that runs the full KPI reporting pipeline."""

from data_generator import generate_mock_data
from data_cleaning import clean_data
from kpi_calculator import calculate_kpis
from notification_sim import notify_failure
import pandas as pd
import os

def run_pipeline():
    print("Running KPI dashboard pipeline...\n")
    try:
        # Step 1: Extract
        raw_data = generate_mock_data()

        # Step 2: Clean/Validate
        cleaned_data = clean_data(raw_data)

        # Step 3: Calculate KPIs
        kpis = calculate_kpis(cleaned_data)

        # Step 4: Print to console
        print("KPI Report:")
        for key, value in kpis.items():
            print(f"{key}: {value}")

        # Step 5: Save to CSV (safe for any working directory)
        output_path = os.path.join(os.path.dirname(__file__), "output", "kpi_report.csv")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pd.DataFrame([kpis]).to_csv(output_path, index=False)
        print(f"\nSaved to {output_path}")

    except Exception as e:
        notify_failure(str(e))

if __name__ == "__main__":
    run_pipeline()
