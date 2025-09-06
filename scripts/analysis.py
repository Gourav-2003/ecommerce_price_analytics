import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis(raw_file, output_dashboard_file, output_figures_folder):
    # Load data
    df = pd.read_csv(raw_file)
    df['date'] = pd.to_datetime(df['date'])

    # Clean product name
    df['product_clean'] = df['title'].str.split(',').str[0].str.replace('"', '').str.strip()

    # Price percentage change per product
    df['price_pct_change'] = df.groupby('product_clean')['price'].pct_change() * 100

    # Rolling stats (7-day std and mean)
    rolling_window = 7
    rolling_vol = df.groupby('product_clean').rolling(window=rolling_window, on='date')['price'].std().reset_index(name='rolling_std')
    rolling_mean = df.groupby('product_clean').rolling(window=rolling_window, on='date')['price'].mean().reset_index(name='rolling_mean')
    rolling_stats = pd.merge(rolling_vol, rolling_mean, on=['product_clean', 'date'])
    df_rolling = pd.merge(df, rolling_stats, on=['product_clean', 'date'], how='left')

    # Add alert flag (price change > 5%)
    df_rolling['alert'] = df_rolling['price_pct_change'].abs() > 5

    # Format date for output
    df_rolling['date'] = pd.to_datetime(df_rolling['date']).dt.strftime('%Y-%m-%d')
    df_rolling.fillna('', inplace=True)  # Optional replace NaNs

    # Save dashboard csv
    df_rolling.to_csv(output_dashboard_file, index=False)

    # [Optional] Generate and save key figures
    sns.set_palette("deep")
    plt.figure(figsize=(7, 4))
    sns.histplot(df['price'], bins=20, kde=True)
    plt.axvline(df['price'].mean(), color='blue', linestyle='--', label='Mean')
    plt.axvline(df['price'].median(), color='red', linestyle=':', label='Median')
    plt.title('Price Distribution')
    plt.xlabel('Price (INR)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_figures_folder}/price_distribution.png")
    plt.close()

    # Add more plots as needed similarly

if __name__ == '__main__':
    RAW_FILE = r"C:\Users\HP\Documents\ecommerce_price_analytics\data\raw\product_prices_raw.csv"
    DASHBOARD_FILE = r"C:\Users\HP\Documents\ecommerce_price_analytics\outputs\dashboard_data.csv"
    FIGURES_FOLDER = r"C:\Users\HP\Documents\ecommerce_price_analytics\outputs\figures"

    run_analysis(RAW_FILE, DASHBOARD_FILE, FIGURES_FOLDER)
