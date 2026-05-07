# Data Dictionary
## Predicting U.S. Unemployment Using Macroeconomic Indicators

---

### joined_data.csv
**Location:** joined_data.csv  
**Description:** Integrated quarterly dataset merging GDP growth rate, unemployment rate, and CPI commodities. This is the primary dataset used for all modeling.

| Column | Type | Unit | Description | Source | Range |
|--------|------|------|-------------|--------|-------|
| observation_date | string | YYYY-MM-DD | First date of each quarter, standardized to ISO 8601 format | Derived | 1956-01-01 to 2025-10-01 |
| gdp_growth_rate | float | Percent (%) | Quarterly percent change in real U.S. GDP, seasonally adjusted at annual rates | BEA via FRED (A191RL1Q225SBEA) | -28.0 to 34.9 |
| unemployment_rate | float | Percent (%) | Seasonally adjusted unemployment rate, averaged across the three months of each quarter | BLS via FRED (UNRATE) | 3.4 to 13.0 |
| cpi_commodities | float | Index (1982-1984 = 100) | Average price level of physical goods for U.S. urban consumers, averaged across the three months of each quarter | BLS via FRED (CUSR0000SAC) | 31.17 to 226.96 |
| covid_dummy | integer | Binary (0 or 1) | Flags quarters affected by the COVID-19 pandemic. 1 = Q2 2020 (2020-04-01) and Q3 2020 (2020-07-01), 0 = all other quarters | Derived | 0 or 1 |

---

### gdp_growth.csv
**Location:** data/gdp_growth.csv  
**Description:** Raw quarterly GDP growth rate data downloaded from FRED.

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| observation_date | string | YYYY-MM-DD | First date of each quarter |
| A191RL1Q225SBEA | float | Percent (%) | Quarterly percent change in real GDP, seasonally adjusted at annual rates |

---

### unemployment_rate.csv
**Location:** data/unemployment_rate.csv  
**Description:** Raw monthly unemployment rate data downloaded from FRED.

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| observation_date | string | YYYY-MM-DD | First date of each month |
| UNRATE | float | Percent (%) | Seasonally adjusted monthly unemployment rate |

---

### cpi_commodities.csv
**Location:** data/cpi_commodities.csv  
**Description:** Raw monthly CPI commodities data downloaded from FRED.

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| observation_date | string | YYYY-MM-DD | First date of each month |
| CUSR0000SAC | float | Index (1982-1984 = 100) | Seasonally adjusted monthly CPI for all urban consumers: commodities |

---

### Notes

- All raw datasets were downloaded as CSV files from the Federal Reserve Bank of St. Louis FRED database.
- Monthly datasets (unemployment_rate, cpi_commodities) were aggregated to quarterly frequency by averaging the three monthly values within each quarter before merging.
- The covid_dummy column was created during exploratory data analysis. The two flagged quarters (2020-04-01 and 2020-07-01) were removed from the modeling dataset due to their extreme outlier values.
- CPI commodities was first differenced prior to modeling to address non-stationarity.
- All date values in the integrated dataset represent the first day of each quarter (January 1, April 1, July 1, October 1).
