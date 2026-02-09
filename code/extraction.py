import requests
import pandas as pd
import os

def scrape_holidays(url="https://paie-tunisie.com/264/fr/jours-feries"):
    """
    Scrapes holidays from paie-tunisie.com.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"Fetching holidays from {url}...")
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
        
        # Use pandas to parse tables directly
        dfs = pd.read_html(response.text)
        if dfs:
            return dfs[0]
    except Exception as e:
        print(f"Error scraping holidays: {e}")
        
    return None

def scrape_weather(url="https://www.infoclimat.fr/observations-meteo/temps-reel/tunis-carthage/60715.html"):
    """
    Scrapes weather data from infoclimat.fr.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"Fetching weather from {url}...")
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
        
        # Infoclimat usually contains data in tables
        dfs = pd.read_html(response.text)
        if dfs:
            # Return the largest table found (usually the data table)
            return max(dfs, key=len)
    except Exception as e:
        print(f"Error scraping weather: {e}")
        
    return None

if __name__ == "__main__":
    # Ensure data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    # 1. Scrape Holidays
    df_holidays = scrape_holidays()
    if df_holidays is not None and not df_holidays.empty:
        print(f"Successfully scraped {len(df_holidays)} holiday items.")
        print(df_holidays.head())
        df_holidays.to_csv("C:/Users/LENOVO/Desktop/S2/Python for D 2/TrafficFlow/data/holidays.csv", index=False)
        print("Data saved to data/holidays.csv")
    else:
        print("No holiday items found.")

    # 2. Scrape Weather
    df_weather = scrape_weather()
    if df_weather is not None and not df_weather.empty:
        print(f"Successfully scraped {len(df_weather)} weather items.")
        print(df_weather.head())
        df_weather.to_csv("C:/Users/LENOVO/Desktop/S2/Python for D 2/TrafficFlow/data/weather.csv", index=False)
        print("Data saved to data/weather.csv")
    else:
        print("No weather items found.")