# scripts/compare_metrics.py
import pandas as pd
from pathlib import Path
from scipy.stats import kruskal, f_oneway, levene
DATA_DIR = Path("data")
files = {
 'Benin': DATA_DIR/'benin-malanville.csv',
 'SierraLeone': DATA_DIR/'sierraleone-bumbuna.csv',
 'Togo': DATA_DIR/'togo-dapaong_qc.csv'
}
dfs = {k: pd.read_csv(p, parse_dates=['Timestamp']) for k,p in files.items()}
metrics=[]
for k, df in dfs.items():
    metrics.append({
        'country':k,
        'GHI_mean': df['GHI'].mean(),
        'GHI_median': df['GHI'].median(),
        'GHI_std': df['GHI'].std()
    })
pd.DataFrame(metrics).to_csv("data/country_ghi_summary.csv", index=False)
# Kruskal test
groups = [dfs[k]['GHI'].dropna().values for k in dfs]
stat, p = kruskal(*groups)
print("Kruskal-Wallis GHI p-value:", p)
