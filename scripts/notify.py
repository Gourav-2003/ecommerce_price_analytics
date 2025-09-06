import pandas as pd
import smtplib
from email.mime.text import MIMEText
import yaml

# Load config
with open(r"C:\Users\HP\Documents\ecommerce_price_analytics\config\config.yaml", 'r') as f:
    config = yaml.safe_load(f)

# Config variables
email_config = config['email']
alert_config = config['alerts']
paths_config = config['paths']

# Load preprocessed data
df = pd.read_csv(paths_config['dashboard_output'])

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Alert threshold from config
alert_threshold = alert_config['price_drop_threshold']

# Latest drop date where price dropped more than threshold
last_drop_date = df[(df['price_pct_change'] < -alert_threshold)]['date'].max()

# Filter alerts
latest_alerts = df[
    (df['date'] == last_drop_date) &
    (df['alert'] == True) &
    (df['price_pct_change'] < -alert_threshold)
]

if latest_alerts.empty:
    print("No significant price drop alerts found for latest date. No email sent.")
else:
    print(f"Alerts found: {len(latest_alerts)}")
    alert_lines = []
    for _, row in latest_alerts.iterrows():
        line = (f"Product: {row['product_clean']}\n"
                f"Date: {row['date'].strftime('%Y-%m-%d')}\n"
                f"Price: ₹{row['price']:.2f}\n"
                f"Price Drop: {row['price_pct_change']:.2f}%\n"
                f"Volatility (7-day std dev): {row['rolling_std']:.2f}\n")
        alert_lines.append(line)
    message_body = "\n\n".join(alert_lines)

    # Email sending function
    def send_email(subject, body, to_email):
        from_email = email_config['sender']
        password = email_config['app_password']
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            server.quit()
            print("Alert email sent successfully.")
        except Exception as e:
            print("Failed to send email:", e)

    recipient_email = email_config['recipient']
    subject = f"URGENT: Price Drop Alert on Ecommerce Products - {last_drop_date.strftime('%Y-%m-%d')}"
    send_email(subject, message_body, recipient_email)
