# app/utils.py
import os
import pandas as pd
from pathlib import Path

# Dynamically locate the data folder, even if the script runs from app/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

def load_data(country_name):
    file_map = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierra_clean.csv",
        "Togo": "togo_clean.csv"
    }
    file_path = os.path.join(DATA_DIR, file_map[country_name])
    df = pd.read_csv(file_path)
    return df

def load_country_csv(country_key):
    mapping = {
        'Benin': 'benin_clean.csv',
        'SierraLeone': 'sierraleone_clean.csv',
        'Togo': 'togo_clean.csv'
    }
    path = DATA_DIR / mapping[country_key]
    return pd.read_csv(path, parse_dates=['Timestamp'])

def load_all():
    countries = ['Benin','SierraLeone','Togo']
    dfs = {c: load_country_csv(c) for c in countries}
    for k,v in dfs.items():
        v['country'] = k
    all_df = pd.concat(dfs.values(), ignore_index=True)
    return dfs, all_df
