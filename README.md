# Sensor Data Analysis Project

## Overview
This project analyzes sensor data collected over a 7-day period (March 1-7, 2025) as part of the Smart City digital ecosystem research. The dataset contains 120,960 measurements from five different IoT sensors monitoring environmental conditions.

**Source**: Grant No.BR24992852 "Intelligent models and methods of Smart City digital ecosystem for sustainable development and the citizens' quality of life improvement"

## Dataset Description

### Data Collection System
The data was collected using **IoT sensors** connected to an ESP Arduino microcontroller:
- **Transmission Method**: Wi-Fi via HTTP protocol
- **Collection Frequency**: Every 5 seconds
- **Records per Day**: 17,280 measurements
- **Total Records**: 120,960 rows (7 days)
- **Time Period**: March 1-7, 2025
- **Storage Format**: CSV files (one per day)

### Sensors Monitored
1. **Temperature Sensor** - Ambient temperature measurements
2. **Humidity Sensor** - Relative humidity levels
3. **Light Sensor** - Light intensity monitoring
4. **pH Sensor** - pH level measurements
5. **Electrical Conductivity (EC) Sensor** - Conductivity readings

### Hardware Setup
- **Microcontroller**: ESP Arduino
- **Communication**: Wi-Fi network
- **Server**: Local server receiving HTTP transmissions
- **Data Pipeline**: Automatic CSV generation and storage

## Project Structure
```
.
├── notebooks/
│   └── sensor_data_analysis.ipynb    # Main analysis notebook
├── reports/
│   ├── sensor_data_2025-03-01.csv   # Daily data files
│   ├── sensor_data_2025-03-02.csv
│   ├── sensor_data_2025-03-03.csv
│   ├── sensor_data_2025-03-04.csv
│   ├── sensor_data_2025-03-05.csv
│   ├── sensor_data_2025-03-06.csv
│   ├── sensor_data_2025-03-07.csv
│   └── sensor_data_merged.csv       # Combined dataset
├── scripts/
│   └── merge_csv.py                 # Data merging script
└── README.md
```

## Analysis Objectives

This Exploratory Data Analysis (EDA) addresses the following tasks:

### 1. Trend Analysis
- ✅ Plot temporal trends for temperature, humidity, and light
- ✅ Visualize sensor measurements over the 7-day period
- ✅ Identify time-based patterns and variations

### 2. Correlation Analysis
- ✅ Analyze relationships between temperature, humidity, and light
- ✅ Create correlation heatmaps and scatter plots
- ✅ Quantify inter-sensor dependencies

### 3. Pattern Recognition
- ✅ Day-night light cycles identification
- ✅ Humidity-temperature inverse relationship analysis
- ✅ Temporal and environmental pattern detection

### 4. Statistical Summary
- ✅ Mean values for all sensors
- ✅ Minimum and maximum values
- ✅ Variance and standard deviation
- ✅ Quartile analysis and outlier detection

## Analysis Summary

### 1. Data Quality
- **Missing Values**: No missing values detected in the dataset
- **Data Integrity**: All 120,960 records are complete and valid
- **Time Coverage**: Continuous monitoring over 7 days

### 2. Correlation Analysis
The correlation matrix reveals very weak correlations between all sensor measurements:

| Sensor Pair | Correlation Coefficient |
|-------------|------------------------|
| Temperature vs Humidity | 0.0037 |
| Temperature vs Light | -0.0004 |
| Temperature vs pH | 0.0007 |
| Temperature vs Electrical Conductivity | 0.0031 |
| Humidity vs Light | -0.0012 |
| Humidity vs pH | 0.0015 |
| Humidity vs Electrical Conductivity | -0.0016 |
| Light vs pH | -0.0025 |
| Light vs Electrical Conductivity | -0.0012 |
| pH vs Electrical Conductivity | 0.0013 |

**Key Finding**: All correlations are near zero (< 0.004), indicating that the sensor measurements are **highly independent** of each other. This suggests:
- Each sensor is measuring truly independent environmental factors
- No significant cross-influence between measured parameters
- Data may be randomly distributed or from a controlled environment

### 3. Distribution Analysis
All five sensors show **uniform distributions** across their measurement ranges:
- **Temperature**: Evenly distributed across the temperature range
- **Humidity**: Uniform distribution with no clustering
- **Light**: Consistent spread across light intensity values
- **pH**: Uniform distribution across pH scale
- **Electrical Conductivity**: Even distribution across conductivity values

**Interpretation**: The uniform distributions suggest either:
- Random data generation, or
- A highly controlled environment with intentional variation
- Lack of natural environmental patterns (which typically show normal distributions)

### 4. Outlier Detection
Box plot analysis reveals:
- **Minimal outliers** across all sensors
- Data points are well-contained within expected ranges
- No extreme anomalies requiring data cleaning
- Consistent data quality throughout the collection period

### 5. Time Series Patterns
Temporal analysis shows:
- **No clear trends**: Sensor values don't show increasing or decreasing patterns over the 7-day period
- **Stationary behavior**: All sensors maintain consistent statistical properties over time
- **Uniform variation**: Temperature ranges from 20-25°C, humidity from 40-60%, light from ~100-1000 units
- **High-frequency data**: 5-second intervals capture fine-grained temporal dynamics
- **Continuous monitoring**: No data gaps or missing periods across the entire week

### 6. Statistical Summary
Detailed statistical analysis for each sensor (Section 10 in notebook):

**Temperature:**
- Range: 20-25°C with uniform distribution
- Mean: ~22.5°C
- Variance: Consistent across all time periods
- No outliers detected

**Humidity:**
- Range: 40-60% with uniform distribution
- Mean: ~50%
- Variance: Stable throughout monitoring period

**Light:**
- Range: ~100-1000 units
- Mean: ~549 units
- **Critical Finding**: No day-night cycle detected
  - Daytime average (6am-6pm): 548.69
  - Nighttime average (6pm-6am): 549.52
  - Difference: -0.83 (statistically negligible)
- Interpretation: Indoor environment or continuous artificial lighting

**pH:**
- Range: 6.0-8.0
- Median: ~7.0 (neutral)
- Uniform distribution suggests controlled environment

**Electrical Conductivity:**
- Range: 0.6-2.0 units
- Stable measurements throughout monitoring period

### 7. Day-Night Light Cycle Analysis (Section 11)
**Key Finding**: The analysis reveals **NO significant day-night pattern** in light measurements:

- **Hourly Analysis**: Light intensity remains remarkably consistent across all 24 hours
- **Day vs Night Comparison**:
  - Average daytime light: 548.69
  - Average nighttime light: 549.52
  - Ratio: 1.00x (essentially identical)
  
**Implications**:
- Data likely collected from an **indoor environment**
- Continuous **artificial lighting** present
- Not exposed to natural daylight cycles
- Consistent with controlled Smart City monitoring station

### 8. Temperature-Humidity Relationship (Section 12)
**Statistical Analysis**:
- **Correlation coefficient**: r = 0.0037 (extremely weak positive)
- **R-squared**: 0.0000 (no explanatory power)
- **P-value**: 0.204 (NOT statistically significant at α=0.05)
- **Linear regression slope**: 0.0146 (nearly flat)

**Conclusion**:
- **NO inverse relationship** detected between temperature and humidity
- Variables are **statistically independent**
- Any apparent relationship is due to random variation
- Suggests controlled environmental conditions where temperature and humidity are independently regulated

**Hourly Correlation Analysis**:
- Correlation varies by hour between -0.03 and +0.04
- No consistent pattern throughout the day
- Reinforces independence of measurements

## Key Insights

### Statistical Independence
The analysis strongly indicates that all five sensor measurements are **statistically independent**:
- Correlation coefficients are negligible (|r| < 0.004)
- No predictive power between variables
- Each sensor provides unique, non-redundant information

### Data Characteristics
1. **Uniform Distribution**: All sensors show uniform rather than normal distributions
2. **No Temporal Patterns**: Absence of trends, daily cycles, or seasonality
3. **High Data Quality**: Zero missing values, minimal outliers
4. **Statistical Independence**: All sensor pairs show negligible correlations (|r| < 0.004)
5. **Stationarity**: Statistical properties remain constant over time
6. **Indoor Environment**: Lack of day-night light cycle indicates indoor monitoring
7. **Controlled Conditions**: Temperature-humidity independence suggests environmental controls

### Implications
These characteristics of the IoT sensor data suggest:
- **Smart City Environment**: Collected from a controlled or monitored urban setting
- **High-Frequency Monitoring**: 5-second intervals provide granular temporal resolution
- **IoT Infrastructure**: Part of a digital ecosystem for sustainable development
- **Research Quality Data**: Collected under Grant No.BR24992852 for quality of life studies
- **Urban Monitoring**: Supports analysis of environmental conditions in city settings

## Research Context
This analysis is part of a continuous assessment for the Smart City digital ecosystem project focusing on:
- Sustainable development monitoring
- Citizens' quality of life improvement
- Intelligent models and methods for urban environments
- Real-time environmental data collection and analysis

## Technologies Used
- **Python 3.13.7**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **matplotlib** - Visualization
- **seaborn** - Statistical data visualization
- **scikit-learn** - Data preprocessing and standardization
- **scipy** - Statistical analysis and linear regression

## How to Use

1. **Install Dependencies**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn scipy
   ```

2. **Merge Daily Data** (if needed):
   ```bash
   python scripts/merge_csv.py
   ```

3. **Run Analysis**:
   Open `notebooks/sensor_data_analysis.ipynb` in Jupyter Notebook or JupyterLab

4. **Execute Cells**: Run all cells sequentially to reproduce the analysis

## Visualizations Included
1. **Correlation Heatmap** (Section 5) - Visual representation of weak inter-sensor correlations
2. **Distribution Histograms** (Section 6) - Frequency distributions showing uniform patterns for all sensors
3. **Box Plots** (Section 7) - Outlier detection and quartile analysis revealing minimal outliers
4. **Time Series Plots** (Section 8) - Temporal patterns for all five sensors over 7 days
5. **Statistical Summary Table** (Section 10) - Complete statistics (mean, min, max, variance, IQR, skewness, kurtosis)
6. **Day-Night Light Analysis** (Section 11) - Hourly light patterns and day/night comparison plots
7. **Temperature-Humidity Relationship** (Section 12) - Scatter plot with linear regression, time series overlay, hourly patterns, and correlation by hour

## Future Work
Potential extensions aligned with Smart City research:
- **Environmental Pattern Detection**: Investigate why no day-night cycles exist; analyze deployment location
- **Multi-sensor Fusion**: Develop combined models using all five independent sensors
- **Anomaly Detection**: Implement algorithms for unusual pattern detection in controlled environments
- **Predictive Modeling**: Despite weak correlations, explore time-series forecasting for each sensor
- **Comparative Analysis**: Compare with outdoor sensors to validate indoor hypothesis
- **Real-time Dashboard**: Create monitoring interface for continuous Smart City surveillance
- **Sensor Placement Optimization**: Use independence findings to optimize sensor deployment
- **Integration with City Data**: Correlate with building occupancy, HVAC systems, or urban activity

## Academic Context
This project forms part of continuous assessment for:
- **Research Grant**: BR24992852
- **Focus Area**: Smart City digital ecosystem
- **Objectives**: Sustainable development and quality of life improvement
- **Methodology**: Intelligent models and data-driven analysis

## Repository
GitHub: [https://github.com/Tavido77/Sensor-Data](https://github.com/Tavido77/Sensor-Data)

## License
This project is available for educational and research purposes.

---

**Last Updated**: November 26, 2025
