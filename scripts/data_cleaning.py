import pandas as pd

def clean_data(raw_file, processed_file):
    # Step 1: Load raw data
    df = pd.read_csv(raw_file)
    
    # Step 2: Handle missing values
    df_clean = df.dropna(subset=['title', 'price'])
    
    # Step 3: Fix data types
    df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce')  # convert price to numeric
    df_clean['date'] = pd.to_datetime(df_clean['date'], errors='coerce')  # convert date to datetime
    
    # Step 4: Remove duplicates based on url and date
    df_clean = df_clean.drop_duplicates(subset=['url', 'date'])
    
    # Step 5: Optional - Reset index
    df_clean = df_clean.reset_index(drop=True)
    
    # Step 6: Save cleaned data to processed folder
    df_clean.to_csv(processed_file, index=False)
    print(f"Cleaned data saved to {processed_file}")

if __name__ == '__main__':
    RAW_FILE = r"C:\Users\HP\Documents\ecommerce_price_analytics\data\raw\product_prices_raw.csv"
    PROCESSED_FILE = r"C:\Users\HP\Documents\ecommerce_price_analytics\data\processed\product_prices_clean.csv"
    clean_data(RAW_FILE, PROCESSED_FILE)
