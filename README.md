# Ecommerce Price Analytics and Alerting System

## Overview
This project automates the process of scraping ecommerce product prices, cleaning and analyzing the data, generating insightful visualizations, and sending email alerts on significant price drops. It is built using Python with libraries such as Selenium for scraping, Pandas for data processing, and Matplotlib/Seaborn for visualization.

---

## Features
- Automated web scraping of product prices from ecommerce websites
- Data cleaning and preprocessing pipeline
- Exploratory data analysis and interactive visualizations
- Price volatility detection and alert generation
- Email notifications for significant price drops
- Fully automated daily execution via scheduling

---

## Folder Structure
├── config/ # Configuration files (e.g., email credentials)
├── data/
│ ├── raw/ # Raw scraped data files
│ └── processed/ # Cleaned and processed data files
├── notebooks/ # Jupyter notebooks for prototyping and analysis
├── outputs/
│ ├── figures/ # Charts and visualizations output
│ └── reports/ # Generated reports or summaries
├── scripts/ # Production-ready Python scripts
├── run_daily.bat # Batch file for Windows scheduling
├── main.py # Main pipeline orchestrator script
├── requirements.txt # Python dependencies
└── README.md # This file


---

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Google Chrome browser (version compatible with ChromeDriver)
- ChromeDriver (version matching Chrome browser)

### Installation
1. Clone the repo:  

---

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Google Chrome browser (version compatible with ChromeDriver)
- ChromeDriver (version matching Chrome browser)

### Installation
1. Clone the repo:  

---

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Google Chrome browser (version compatible with ChromeDriver)
- ChromeDriver (version matching Chrome browser)

### Installation
1. Clone the repo:  
git clone (https://github.com/Gourav-2003/ecommerce_price_analytics)
cd ecommerce_price_analytics
2. Create virtual environment (optional but recommended):  
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install dependencies:  
pip install -r requirements.txt
4. Download ChromeDriver matching your Chrome version and place it in a known location. Update path in `scripts/scraper.py`.

---

## Usage

### Run full pipeline manually:  
python main.py

### Automate daily runs on Windows with Task Scheduler:
- Schedule `run_daily.bat` to run at desired times.

---

## Configuration
- Store sensitive information like email credentials in `config/` securely.
- Update these configs before running the notification script.

---

## Contributing
- Fork the repo and create your feature branch.
- Submit pull requests clearly describing your changes.
- Ensure code quality and include any necessary tests.

---

## License
MIT License

Copyright (c) 2025 Gourav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Contact
For queries or support, contact:  
**Gourav** – "gouravmuchhal476@gmail.com"

