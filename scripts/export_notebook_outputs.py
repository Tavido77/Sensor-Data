#!/usr/bin/env python3
"""
Export Notebook Outputs Script
Runs the sensor data analysis notebook and exports all visualizations and outputs
to the screenshots folder.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy import stats
import os
from datetime import datetime

# Set style for plots
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Create screenshots directory if it doesn't exist
screenshot_dir = '../screenshots'
os.makedirs(screenshot_dir, exist_ok=True)

print("=" * 80)
print("SENSOR DATA ANALYSIS - OUTPUT EXPORT")
print("=" * 80)
print(f"Export Directory: {os.path.abspath(screenshot_dir)}")
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)
print()

# Load the data
print("Loading data...")
df = pd.read_csv('../reports/sensor_data_merged.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
print(f"✓ Data loaded: {df.shape[0]} rows × {df.shape[1]} columns")
print()

# ============================================================================
# 1. CORRELATION ANALYSIS
# ============================================================================
print("1. Generating Correlation Heatmap...")
correlation_matrix = df[['temperature', 'humidity', 'light', 'pH', 'electrical_conductivity']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, fmt='.2f')
plt.title('Correlation Matrix of Sensor Measurements', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{screenshot_dir}/01_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 01_correlation_heatmap.png")

# Save correlation matrix to text file
with open(f'{screenshot_dir}/01_correlation_matrix.txt', 'w') as f:
    f.write("CORRELATION MATRIX\n")
    f.write("=" * 80 + "\n")
    f.write(correlation_matrix.to_string())
print("   ✓ Saved: 01_correlation_matrix.txt")
print()

# ============================================================================
# 2. DISTRIBUTION PLOTS
# ============================================================================
print("2. Generating Distribution Plots...")
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Distribution of Sensor Measurements', fontsize=16, fontweight='bold')

sensors = ['temperature', 'humidity', 'light', 'pH', 'electrical_conductivity']
colors = ['red', 'blue', 'yellow', 'green', 'purple']

for idx, (sensor, color) in enumerate(zip(sensors, colors)):
    row = idx // 3
    col = idx % 3
    axes[row, col].hist(df[sensor], bins=50, color=color, alpha=0.7, edgecolor='black')
    axes[row, col].set_title(f'{sensor.replace("_", " ").title()}', fontweight='bold')
    axes[row, col].set_xlabel('Value')
    axes[row, col].set_ylabel('Frequency')
    axes[row, col].grid(True, alpha=0.3)

fig.delaxes(axes[1, 2])
plt.tight_layout()
plt.savefig(f'{screenshot_dir}/02_distributions.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 02_distributions.png")
print()

# ============================================================================
# 3. BOX PLOTS
# ============================================================================
print("3. Generating Box Plots...")
fig, axes = plt.subplots(1, 5, figsize=(18, 4))
fig.suptitle('Box Plots for Outlier Detection', fontsize=16, fontweight='bold')

for idx, (sensor, color) in enumerate(zip(sensors, colors)):
    axes[idx].boxplot(df[sensor], patch_artist=True,
                      boxprops=dict(facecolor=color, alpha=0.6),
                      medianprops=dict(color='black', linewidth=2))
    axes[idx].set_title(sensor.replace('_', ' ').title(), fontweight='bold')
    axes[idx].set_ylabel('Value')
    axes[idx].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{screenshot_dir}/03_box_plots.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 03_box_plots.png")
print()

# ============================================================================
# 4. TIME SERIES PLOTS
# ============================================================================
print("4. Generating Time Series Plots...")
fig, axes = plt.subplots(5, 1, figsize=(15, 12))
fig.suptitle('Time Series of Sensor Measurements', fontsize=16, fontweight='bold')

colors_ts = ['red', 'blue', 'orange', 'green', 'purple']

for idx, (sensor, color) in enumerate(zip(sensors, colors_ts)):
    axes[idx].plot(df['timestamp'], df[sensor], color=color, alpha=0.7, linewidth=0.5)
    axes[idx].set_title(sensor.replace('_', ' ').title(), fontweight='bold')
    axes[idx].set_ylabel('Value')
    axes[idx].grid(True, alpha=0.3)
    
axes[-1].set_xlabel('Timestamp')
plt.tight_layout()
plt.savefig(f'{screenshot_dir}/04_time_series.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 04_time_series.png")
print()

# ============================================================================
# 5. STATISTICAL SUMMARY
# ============================================================================
print("5. Generating Statistical Summary...")
stats_output = []
stats_output.append("=" * 80)
stats_output.append("DETAILED STATISTICAL SUMMARY BY SENSOR")
stats_output.append("=" * 80)
stats_output.append("")

for sensor in sensors:
    stats_output.append(f"\n{'=' * 80}")
    stats_output.append(f"{sensor.replace('_', ' ').upper()}")
    stats_output.append(f"{'=' * 80}")
    stats_output.append(f"Mean:              {df[sensor].mean():.4f}")
    stats_output.append(f"Median:            {df[sensor].median():.4f}")
    stats_output.append(f"Minimum:           {df[sensor].min():.4f}")
    stats_output.append(f"Maximum:           {df[sensor].max():.4f}")
    stats_output.append(f"Range:             {df[sensor].max() - df[sensor].min():.4f}")
    stats_output.append(f"Variance:          {df[sensor].var():.4f}")
    stats_output.append(f"Std Deviation:     {df[sensor].std():.4f}")
    stats_output.append(f"25th Percentile:   {df[sensor].quantile(0.25):.4f}")
    stats_output.append(f"75th Percentile:   {df[sensor].quantile(0.75):.4f}")
    stats_output.append(f"IQR:               {df[sensor].quantile(0.75) - df[sensor].quantile(0.25):.4f}")
    stats_output.append(f"Skewness:          {df[sensor].skew():.4f}")
    stats_output.append(f"Kurtosis:          {df[sensor].kurtosis():.4f}")

stats_output.append("\n" + "=" * 80)

with open(f'{screenshot_dir}/05_statistical_summary.txt', 'w') as f:
    f.write('\n'.join(stats_output))
print("   ✓ Saved: 05_statistical_summary.txt")
print()

# ============================================================================
# 6. DAY-NIGHT LIGHT CYCLE ANALYSIS
# ============================================================================
print("6. Generating Day-Night Light Cycle Analysis...")
df['hour'] = df['timestamp'].dt.hour
df['date'] = df['timestamp'].dt.date

fig, axes = plt.subplots(2, 1, figsize=(16, 10))

# Hourly average light intensity
hourly_light = df.groupby('hour')['light'].mean()
axes[0].plot(hourly_light.index, hourly_light.values, marker='o', linewidth=2, markersize=8, color='orange')
axes[0].set_xlabel('Hour of Day', fontsize=12)
axes[0].set_ylabel('Average Light Intensity', fontsize=12)
axes[0].set_title('Day-Night Light Cycle: Average Light Intensity by Hour', fontsize=14, fontweight='bold')
axes[0].grid(True, alpha=0.3)
axes[0].axvspan(0, 6, alpha=0.2, color='navy', label='Night')
axes[0].axvspan(18, 24, alpha=0.2, color='navy')
axes[0].axvspan(6, 18, alpha=0.2, color='yellow', label='Day')
axes[0].legend()
axes[0].set_xticks(range(0, 24))

# Light intensity over time colored by day/night
night_mask = (df['hour'] >= 18) | (df['hour'] < 6)
day_mask = ~night_mask

axes[1].scatter(df[day_mask]['timestamp'], df[day_mask]['light'], 
                s=0.5, alpha=0.3, color='orange', label='Daytime')
axes[1].scatter(df[night_mask]['timestamp'], df[night_mask]['light'], 
                s=0.5, alpha=0.3, color='navy', label='Nighttime')
axes[1].set_xlabel('Timestamp', fontsize=12)
axes[1].set_ylabel('Light Intensity', fontsize=12)
axes[1].set_title('Light Intensity Timeline: Day vs Night', fontsize=14, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{screenshot_dir}/06_day_night_light_cycle.png', dpi=300, bbox_inches='tight')
plt.close()

# Save day-night statistics
day_light = df[day_mask]['light'].mean()
night_light = df[night_mask]['light'].mean()

day_night_stats = []
day_night_stats.append("\nDAY-NIGHT LIGHT CYCLE ANALYSIS")
day_night_stats.append("=" * 60)
day_night_stats.append(f"Average Light (Daytime 6am-6pm):    {day_light:.2f}")
day_night_stats.append(f"Average Light (Nighttime 6pm-6am):  {night_light:.2f}")
day_night_stats.append(f"Day-Night Difference:               {day_light - night_light:.2f}")
if night_light != 0:
    day_night_stats.append(f"Ratio (Day/Night):                  {day_light / night_light:.2f}x")
else:
    day_night_stats.append(f"Ratio (Day/Night):                  N/A")

with open(f'{screenshot_dir}/06_day_night_analysis.txt', 'w') as f:
    f.write('\n'.join(day_night_stats))

print("   ✓ Saved: 06_day_night_light_cycle.png")
print("   ✓ Saved: 06_day_night_analysis.txt")
print()

# ============================================================================
# 7. TEMPERATURE-HUMIDITY RELATIONSHIP
# ============================================================================
print("7. Generating Temperature-Humidity Relationship Analysis...")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Scatter plot with regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(df['temperature'], df['humidity'])
line = slope * df['temperature'] + intercept

axes[0, 0].scatter(df['temperature'], df['humidity'], alpha=0.3, s=1, color='blue')
axes[0, 0].plot(df['temperature'], line, 'r-', linewidth=2, label=f'Linear fit (r={r_value:.4f})')
axes[0, 0].set_xlabel('Temperature', fontsize=12)
axes[0, 0].set_ylabel('Humidity', fontsize=12)
axes[0, 0].set_title('Temperature vs Humidity with Linear Regression', fontsize=14, fontweight='bold')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Time series overlay
ax1 = axes[0, 1]
ax2 = ax1.twinx()
ax1.plot(df['timestamp'], df['temperature'], color='red', alpha=0.7, linewidth=0.5, label='Temperature')
ax2.plot(df['timestamp'], df['humidity'], color='blue', alpha=0.7, linewidth=0.5, label='Humidity')
ax1.set_xlabel('Timestamp', fontsize=12)
ax1.set_ylabel('Temperature', color='red', fontsize=12)
ax2.set_ylabel('Humidity', color='blue', fontsize=12)
ax1.set_title('Temperature and Humidity Time Series Overlay', fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='red')
ax2.tick_params(axis='y', labelcolor='blue')
ax1.grid(True, alpha=0.3)

# Hourly averages
hourly_temp = df.groupby('hour')['temperature'].mean()
hourly_humidity = df.groupby('hour')['humidity'].mean()

axes[1, 0].plot(hourly_temp.index, hourly_temp.values, marker='o', color='red', 
                linewidth=2, markersize=8, label='Temperature')
axes[1, 0].set_xlabel('Hour of Day', fontsize=12)
axes[1, 0].set_ylabel('Average Temperature', color='red', fontsize=12)
axes[1, 0].tick_params(axis='y', labelcolor='red')
axes[1, 0].set_title('Hourly Temperature and Humidity Patterns', fontsize=14, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].set_xticks(range(0, 24))

ax_humidity = axes[1, 0].twinx()
ax_humidity.plot(hourly_humidity.index, hourly_humidity.values, marker='s', color='blue', 
                 linewidth=2, markersize=8, label='Humidity')
ax_humidity.set_ylabel('Average Humidity', color='blue', fontsize=12)
ax_humidity.tick_params(axis='y', labelcolor='blue')

# Correlation by hour
hourly_corr = df.groupby('hour').apply(lambda x: x['temperature'].corr(x['humidity']), include_groups=False)
axes[1, 1].bar(hourly_corr.index, hourly_corr.values, color='purple', alpha=0.7)
axes[1, 1].axhline(y=0, color='black', linestyle='--', linewidth=1)
axes[1, 1].set_xlabel('Hour of Day', fontsize=12)
axes[1, 1].set_ylabel('Correlation Coefficient', fontsize=12)
axes[1, 1].set_title('Temperature-Humidity Correlation by Hour', fontsize=14, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3, axis='y')
axes[1, 1].set_xticks(range(0, 24))

plt.tight_layout()
plt.savefig(f'{screenshot_dir}/07_temperature_humidity_relationship.png', dpi=300, bbox_inches='tight')
plt.close()

# Save temperature-humidity statistics
temp_humid_stats = []
temp_humid_stats.append("\nTEMPERATURE-HUMIDITY RELATIONSHIP ANALYSIS")
temp_humid_stats.append("=" * 60)
temp_humid_stats.append(f"Overall Correlation:        {r_value:.4f}")
temp_humid_stats.append(f"Relationship Type:          {'Inverse' if r_value < 0 else 'Direct'}")
temp_humid_stats.append(f"Linear Regression:")
temp_humid_stats.append(f"  Slope:                    {slope:.6f}")
temp_humid_stats.append(f"  Intercept:                {intercept:.4f}")
temp_humid_stats.append(f"  R-squared:                {r_value**2:.4f}")
temp_humid_stats.append(f"  P-value:                  {p_value:.6f}")
temp_humid_stats.append(f"  Statistical Significance: {'Yes' if p_value < 0.05 else 'No'} (α=0.05)")

with open(f'{screenshot_dir}/07_temperature_humidity_analysis.txt', 'w') as f:
    f.write('\n'.join(temp_humid_stats))

print("   ✓ Saved: 07_temperature_humidity_relationship.png")
print("   ✓ Saved: 07_temperature_humidity_analysis.txt")
print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 80)
print("EXPORT COMPLETE!")
print("=" * 80)
print(f"\nAll outputs saved to: {os.path.abspath(screenshot_dir)}")
print("\nFiles generated:")
print("  1. 01_correlation_heatmap.png")
print("  2. 01_correlation_matrix.txt")
print("  3. 02_distributions.png")
print("  4. 03_box_plots.png")
print("  5. 04_time_series.png")
print("  6. 05_statistical_summary.txt")
print("  7. 06_day_night_light_cycle.png")
print("  8. 06_day_night_analysis.txt")
print("  9. 07_temperature_humidity_relationship.png")
print(" 10. 07_temperature_humidity_analysis.txt")
print("\n" + "=" * 80)
