# Predicting U.S. Unemployment Rate from Macroeconomic Indicators

## Project Overview
This project predicts quarterly U.S. unemployment rates using GDP growth rate,
Consumer Price Index for commodities, and lagged versions of these variables.
Data is sourced from the Federal Reserve Economic Data (FRED) database.

## Team
David Hyeongseok Lee, Ethan Kim

## Data Sources
All datasets are from FRED (Federal Reserve Bank of St. Louis):
- GDP Growth Rate: https://fred.stlouisfed.org/series/A191RL1Q225SBEA
- Unemployment Rate: https://fred.stlouisfed.org/series/UNRATE
- CPI Commodities: https://fred.stlouisfed.org/series/CUSR0000SAC
- 
Raw data files are included in the `/data` folder of this repository.

## HOW TO REPRODUCE

### 1. Clone the repository
```bash
git clone https://github.com/hyeongseokl/EKDL.git
cd EKDL
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the full pipeline
```bash
python run_all.py
```

This will execute join.py, EDA.ipynb, and models_2.ipynb in order.
