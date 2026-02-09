import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def explore_holidays(file_path):
    """
    Explores the holidays dataset extracted by extraction.py.
    """
    print(f"\n{'='*20} Exploring Holidays Data {'='*20}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    
    print("--- Dataset Shape ---")
    print(df.shape)
    print("\n--- First 5 Rows ---")
    print(df.head())
    print("\n--- Data Info ---")
    print(df.info())

def explore_weather(file_path):
    """
    Explores the weather dataset extracted by extraction.py.
    """
    print(f"\n{'='*20} Exploring Weather Data {'='*20}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    
    print("--- Dataset Shape ---")
    print(df.shape)
    print("\n--- First 5 Rows ---")
    print(df.head())
    
    # Basic visualization: Missing Values Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap - Weather Data')
    output_path = os.path.join(os.path.dirname(file_path), 'weather_missing_values.png')
    plt.savefig(output_path)
    plt.close()
    print(f"\nSaved missing values heatmap to {output_path}")

if __name__ == "__main__":
    # Paths based on extraction.py output
    base_path = "C:/Users/LENOVO/Desktop/S2/Python for D 2/TrafficFlow/data"
    
    explore_holidays(os.path.join(base_path, "holidays.csv"))
    explore_weather(os.path.join(base_path, "weather.csv"))