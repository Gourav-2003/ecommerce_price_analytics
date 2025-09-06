import os
import sys

def run_script(path):
    exit_code = os.system(f'python "{path}"')
    if exit_code != 0:
        print(f"Script failed: {path}")
        sys.exit(1)

if __name__ == "__main__":
    print("---- Step 1: Scraping Data ----")
    run_script(r"C:\Users\HP\Documents\ecommerce_price_analytics\scripts\scraper.py")



    print("---- Step 2: Cleaning Data ----")
    run_script(r"C:\Users\HP\Documents\ecommerce_price_analytics\scripts\analysis.py")

    print("---- Step 3: Analysis & Dashboard Creation ----")
    run_script(r"C:\Users\HP\Documents\ecommerce_price_analytics\scripts\data_cleaning.py")

    print("---- Step 4: Sending Alerts ----")
    run_script(r"C:\Users\HP\Documents\ecommerce_price_analytics\scripts\notify.py")

    print("All steps completed successfully!")

