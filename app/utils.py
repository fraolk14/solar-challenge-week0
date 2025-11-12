# app/utils.py
import pandas as pd
from pathlib import Path

DATA_DIR = Path("../data")  # adjust if app lives elsewhere

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
